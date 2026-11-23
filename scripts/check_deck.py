"""C2 / N3 / C4：簡報檢查（CLAUDE.md 第 5、6 節）。

用法：
  python scripts/check_deck.py --stage outline   # C2：檢查 deck/outline.md
  python scripts/check_deck.py --stage content   # N3 自檢：deck/content.md 與大綱、wiki 是否對得上
  python scripts/check_deck.py --stage html      # C4：deck/index.html 結構、引用同步、連結
每個 stage 會先跑前面的 stage（html 會連 outline、content 一起檢查）。
"""
import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from wikilib import LINK_RE, ROOT, load_all, parse_frontmatter  # noqa: E402

DECK = ROOT / "deck"
PSEUDO = {"project"}  # 本專案自己的流程文件 docs/workflow.md
MAX_BULLETS = 5
MAX_BULLET_LEN = 40

errors = []
err = errors.append
pages = load_all()
concepts = {s for s, p in pages.items() if p["kind"] == "concept"}
valid = set(pages) | PSEUDO


def split_slides(body):
    """回傳 [(id, title, lines)]，以 `## Snn｜標題` 切開。"""
    out = []
    for line in body.splitlines():
        m = re.match(r"^## (S\d{2})｜(.+)$", line)
        if m:
            out.append((m.group(1), m.group(2).strip(), []))
        elif out:
            out[-1][2].append(line)
    return out


def field(lines, name):
    for l in lines:
        m = re.match(rf"^- {name}：(.*)$", l) or re.match(rf"^{name}：(.*)$", l)
        if m:
            return m.group(1).strip()
    return None


# ---------- outline ----------
def check_outline():
    path = DECK / "outline.md"
    meta, body = parse_frontmatter(path.read_text(encoding="utf-8"))
    for k in ("title", "audience", "goal", "must_cover"):
        if not meta.get(k):
            err(f"outline.md: 缺少 frontmatter `{k}`")
    slides = split_slides(body)
    if not 12 <= len(slides) <= 16:
        err(f"outline.md: 投影片要 12～16 張，目前 {len(slides)} 張")
    cited = set()
    result = {}
    for i, (sid, title, lines) in enumerate(slides, 1):
        if sid != f"S{i:02d}":
            err(f"outline.md: 第 {i} 張編號應為 S{i:02d}，卻是 {sid}")
        for f in ("型式", "目標", "引用", "內容方向"):
            if not field(lines, f):
                err(f"outline.md {sid}: 缺少「{f}」")
        cites = LINK_RE.findall(field(lines, "引用") or "")
        if not cites:
            err(f"outline.md {sid}: 至少要引用 1 個 wiki 頁面")
        for c in cites:
            if c not in valid:
                err(f"outline.md {sid}: 引用 [[{c}]] 在 wiki 不存在 → wiki 缺內容，應跳回 N1")
        cited |= set(cites)
        result[sid] = {"title": title, "cites": cites, "type": field(lines, "型式") or ""}
    if slides:
        if not result[slides[0][0]]["type"].startswith("cover"):
            err("outline.md: 第一張必須是 cover")
        if not result[slides[-1][0]]["type"].startswith("summary"):
            err("outline.md: 最後一張必須是 summary")
    if meta.get("must_cover") == "all-concepts":
        for c in sorted(concepts - cited):
            err(f"outline.md: 概念 [[{c}]] 沒有被任何投影片引用（must_cover: all-concepts）")
    return result


# ---------- content ----------
BULLET_CITE = re.compile(r"（((?:\[\[[a-z0-9-]+\]\][、 ]?)+)）$")


def check_content(outline):
    path = DECK / "content.md"
    if not path.is_file():
        err("deck/content.md 不存在（N3 尚未執行）")
        return {}
    _, body = parse_frontmatter(path.read_text(encoding="utf-8"))
    slides = split_slides(body)
    result = {}
    if [s[0] for s in slides] != list(outline):
        err(f"content.md: 投影片編號與大綱不一致（大綱 {len(outline)} 張，內容 {len(slides)} 張）")
    for sid, title, lines in slides:
        o = outline.get(sid)
        if o and title != o["title"]:
            err(f"content.md {sid}: 標題「{title}」與大綱「{o['title']}」不同 → 改標題要回 N2")
        cites = LINK_RE.findall(field(lines, "引用") or "")
        if o and set(cites) != set(o["cites"]):
            err(f"content.md {sid}: 引用 {sorted(cites)} 與大綱 {sorted(o['cites'])} 不一致 → 新增引用要回 N2")
        bl = [l[2:].strip() for l in lines if l.startswith("- ") and not re.match(r"^- (引用|講者備註|圖解|答案)：", l)]
        if len(bl) > MAX_BULLETS:
            err(f"content.md {sid}: 條列 {len(bl)} 點，超過 {MAX_BULLETS} 點")
        for b in bl:
            m = BULLET_CITE.search(b)
            if not m:
                err(f"content.md {sid}: 這點沒有在結尾標引用（[[slug]]）：{b[:30]}…")
                continue
            for c in LINK_RE.findall(m.group(1)):
                if c not in cites:
                    err(f"content.md {sid}: 條列引用 [[{c}]] 不在本頁「引用」清單")
            text = b[: m.start()].strip()
            if len(text) > MAX_BULLET_LEN:
                err(f"content.md {sid}: 條列 {len(text)} 字，超過 {MAX_BULLET_LEN} 字：{text[:20]}…")
        result[sid] = {"title": title, "cites": cites}
    return result


# ---------- html ----------
def check_html(content):
    try:
        from html_checks import check_html_file
    except ImportError:
        err("scripts/html_checks.py 尚未建立（N4 尚未執行）")
        return
    for e in check_html_file(DECK / "index.html", content, valid):
        err(e)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", choices=["outline", "content", "html"], required=True)
    stage = ap.parse_args().stage
    outline = check_outline()
    if stage in ("content", "html"):
        content = check_content(outline)
        if stage == "html":
            check_html(content)
    print(f"stage: {stage}；投影片 {len(outline)} 張")
    if errors:
        print(f"\nDECK CHECK FAILED — {len(errors)} 個錯誤：")
        for e in errors:
            print("  ✗", e)
        sys.exit(1)
    print("DECK CHECK PASSED")


if __name__ == "__main__":
    main()
