"""C1：Wiki 檢查（CLAUDE.md 第 4、5 節）。用法：python scripts/check_wiki.py

全部通過印出 WIKI CHECK PASSED；否則列出錯誤並 exit 1。
"""
import hashlib
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from wikilib import LINK_RE, RAW, ROOT, TAG_RE, WIKI, bullets, load_all, source_id  # noqa: E402

errors = []
err = errors.append

# ---------- 0. raw 唯讀：雜湊比對 ----------
recorded = {}
for line in (ROOT / "docs" / "raw.sha256").read_text(encoding="utf-8").splitlines():
    h, name = line.split(maxsplit=1)
    recorded[name.lstrip("*")] = h
actual = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in RAW.iterdir() if p.is_file()}
for name in sorted(set(recorded) | set(actual)):
    if recorded.get(name) != actual.get(name):
        err(f"raw/{name}: 與 docs/raw.sha256 不符（raw 被修改、新增或刪除）")

pages = load_all()
sources = {s: p for s, p in pages.items() if p["kind"] == "source"}
concepts = {s: p for s, p in pages.items() if p["kind"] == "concept"}
source_ids = {source_id(s): s for s in sources}

# ---------- 1. 共通：frontmatter、slug、連結 ----------
for slug, p in pages.items():
    m = p["meta"]
    if p["kind"] != "overview" and m.get("slug") != slug:
        err(f"{p['rel']}: frontmatter slug 與檔名不一致")
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", slug):
        err(f"{p['rel']}: slug 必須是英文小寫 kebab-case")
    for key in ("title", "updated"):
        if not m.get(key):
            err(f"{p['rel']}: 缺少 frontmatter `{key}`")
    for link in p["links"]:
        if link not in pages:
            err(f"{p['rel']}: 連結 [[{link}]] 找不到對應頁面")

# ---------- 2. 來源摘要 ----------
for slug, p in sources.items():
    if not re.fullmatch(r"s\d+-.+", slug):
        err(f"{p['rel']}: 檔名必須是 sN-xxx")
    raw = p["meta"].get("raw", "")
    if not (ROOT / raw).is_file():
        err(f"{p['rel']}: raw 檔不存在 `{raw}`")
    for sec in ("這份資料在講什麼", "重點摘錄", "產生／更新的概念", "轉錄錯誤與疑點"):
        if sec not in p["sections"]:
            err(f"{p['rel']}: 缺少段落「{sec}」")

# ---------- 3. 概念條目 ----------
for slug, p in concepts.items():
    m, sec = p["meta"], p["sections"]
    declared = m.get("sources") or []
    if not declared:
        err(f"{p['rel']}: frontmatter `sources` 不可為空")
    for sid in declared:
        if sid not in source_ids:
            err(f"{p['rel']}: sources 列了不存在的來源 {sid}")
    if not p["definition"]:
        err(f"{p['rel']}: 缺少一句話定義（> 開頭）")
    elif len(p["definition"]) > 40:
        err(f"{p['rel']}: 一句話定義 {len(p['definition'])} 字，超過 40 字")
    for name in ("重點", "例子", "常見誤區", "相關概念"):
        if name not in sec:
            err(f"{p['rel']}: 缺少段落「{name}」")
    points = bullets(sec.get("重點", []))
    if not 3 <= len(points) <= 6:
        err(f"{p['rel']}: 「重點」要 3～6 點，目前 {len(points)} 點")
    for i, b in enumerate(points, 1):
        if not re.search(r"（[^（）]*s\d[^（）]*）[。.]?\s*$", b):
            err(f"{p['rel']}: 重點第 {i} 點結尾沒有標來源（sN）")
    used = set(TAG_RE.findall("\n".join(points + bullets(sec.get("例子", [])) + bullets(sec.get("常見誤區", [])))))
    for sid in used - set(declared):
        err(f"{p['rel']}: 內文引用 {sid}，但 frontmatter sources 沒有列")
    for sid in set(declared) - used:
        err(f"{p['rel']}: frontmatter 列了 {sid}，但內文沒有任何一點引用它")
    if not LINK_RE.findall("\n".join(sec.get("相關概念", []))):
        err(f"{p['rel']}: 「相關概念」至少要 1 個 [[連結]]")

# ---------- 4. 來源 ⇄ 概念 雙向一致、孤兒頁 ----------
for sslug, sp in sources.items():
    sid = source_id(sslug)
    listed = set(LINK_RE.findall("\n".join(sp["sections"].get("產生／更新的概念", []))))
    for c in listed:
        if c in concepts and sid not in (concepts[c]["meta"].get("sources") or []):
            err(f"{sp['rel']}: 列了 [[{c}]]，但 {c}.md 的 sources 沒有 {sid}")
    for c, cp in concepts.items():
        if sid in (cp["meta"].get("sources") or []) and c not in listed:
            err(f"{cp['rel']}: sources 有 {sid}，但 {sslug}.md「產生／更新的概念」沒有列 [[{c}]]")

inbound = {s: 0 for s in pages}
for p in pages.values():
    for link in set(p["links"]):
        if link in inbound and link != p["slug"]:
            inbound[link] += 1
for slug, n in inbound.items():
    if n == 0 and slug != "overview":
        err(f"{pages[slug]['rel']}: 孤兒頁，沒有任何頁面連到它")

# ---------- 5. index.md / log.md ----------
index_md = (WIKI / "index.md").read_text(encoding="utf-8")
for slug in sorted(pages):
    if f"[[{slug}]]" not in index_md:
        err(f"wiki/index.md: 沒有列出 [[{slug}]]")
for link in LINK_RE.findall(index_md):
    if link not in pages:
        err(f"wiki/index.md: [[{link}]] 找不到對應頁面")
for line in (WIKI / "log.md").read_text(encoding="utf-8").splitlines():
    if line.startswith("## ") and not re.match(
        r"^## \[\d{4}-\d{2}-\d{2}\] (setup|ingest|lint|query|publish) \| .+", line
    ):
        err(f"wiki/log.md: 標題格式錯誤 `{line}`")

# ---------- 結果 ----------
print(f"pages: {len(sources)} sources, {len(concepts)} concepts, overview={'overview' in pages}")
if errors:
    print(f"\nWIKI CHECK FAILED — {len(errors)} 個錯誤：")
    for e in errors:
        print("  ✗", e)
    sys.exit(1)
print("WIKI CHECK PASSED")
