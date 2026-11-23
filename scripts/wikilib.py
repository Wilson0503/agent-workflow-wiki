"""共用：解析 wiki 頁面（只用標準函式庫）。"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
RAW = ROOT / "raw"
LINK_RE = re.compile(r"\[\[([a-z0-9-]+)\]\]")
TAG_RE = re.compile(r"s[1-9]\d*")


def parse_frontmatter(text):
    text = text.replace("\r\n", "\n")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}, text
    meta = {}
    for line in m.group(1).splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        v = v.strip()
        if v.startswith("[") and v.endswith("]"):
            v = [x.strip() for x in v[1:-1].split(",") if x.strip()]
        meta[k.strip()] = v
    return meta, text[m.end():]


def sections(body):
    out, cur = {}, None
    for line in body.splitlines():
        if line.startswith("## "):
            cur = line[3:].strip()
            out[cur] = []
        elif cur:
            out[cur].append(line)
    return out


def bullets(lines):
    return [l[2:].strip() for l in lines if l.startswith("- ")]


def load_page(path, kind):
    text = path.read_text(encoding="utf-8")
    meta, body = parse_frontmatter(text)
    title = next((l[2:].strip() for l in body.splitlines() if l.startswith("# ")), "")
    definition = next((l[2:].strip() for l in body.splitlines() if l.startswith("> ") and not l.startswith("> ⚠️")), "")
    return {
        "kind": kind,
        "path": path,
        "rel": path.relative_to(ROOT).as_posix(),
        "slug": path.stem,
        "meta": meta,
        "body": body,
        "title": title,
        "definition": definition,
        "sections": sections(body),
        "links": LINK_RE.findall(body),
    }


def load_all():
    pages = {}
    for kind, folder in (("source", WIKI / "sources"), ("concept", WIKI / "concepts")):
        for p in sorted(folder.glob("*.md")):
            pages[p.stem] = load_page(p, kind)
    ov = WIKI / "overview.md"
    if ov.is_file():
        pages["overview"] = load_page(ov, "overview")
    return pages


def source_id(slug):
    """s6-loop-and-graph -> s6"""
    return slug.split("-", 1)[0]
