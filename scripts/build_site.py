"""N5：從 Markdown 產生網頁（禁止手改產出的 HTML）。

  wiki.html     ← wiki/index.md（目錄）＋ overview ＋ 全部來源摘要與概念條目，每頁一個錨點 #slug
  process.html  ← docs/workflow.md ＋ docs/run-log.md ＋ docs/reflection.md

用法：python scripts/build_site.py
"""
import html
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from wikilib import ROOT, WIKI, load_all, source_id  # noqa: E402

PAGES = load_all()
DOC_ANCHORS = {"workflow.md": "#workflow", "run-log.md": "#run-log", "reflection.md": "#reflection"}


def title_of(slug):
    p = PAGES.get(slug)
    return p["meta"].get("title", slug) if p else slug


def inline(text, wiki_prefix):
    t = html.escape(text, quote=False)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", t)

    def link(m):
        label, href = m.group(1), m.group(2)
        href = DOC_ANCHORS.get(href, href)
        return f'<a href="{href}">{label}</a>'

    t = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", link, t)
    t = re.sub(
        r"\[\[([a-z0-9-]+)\]\]",
        lambda m: f'<a href="{wiki_prefix}#{m.group(1)}">{html.escape(title_of(m.group(1)), quote=False)}</a>',
        t,
    )
    return t


def render(md, wiki_prefix="", shift=1):
    """極簡 Markdown：標題、段落、條列、引用、表格、程式碼區塊（mermaid 另外處理）。"""
    out, lines, i = [], md.replace("\r\n", "\n").split("\n"), 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("```"):
            lang = line[3:].strip()
            buf = []
            i += 1
            while i < len(lines) and not lines[i].startswith("```"):
                buf.append(lines[i])
                i += 1
            code = html.escape("\n".join(buf), quote=False)
            out.append(f'<pre class="mermaid">{code}</pre>' if lang == "mermaid" else f"<pre>{code}</pre>")
        elif m := re.match(r"^(#{1,4}) (.+)$", line):
            lv = min(len(m.group(1)) + shift, 6)
            out.append(f"<h{lv}>{inline(m.group(2), wiki_prefix)}</h{lv}>")
        elif line.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-{2,}:?", c) for c in cells):
                    rows.append(cells)
                i += 1
            i -= 1
            head, *body = rows
            out.append("<table><thead><tr>" + "".join(f"<th>{inline(c, wiki_prefix)}</th>" for c in head) + "</tr></thead><tbody>")
            out += ["<tr>" + "".join(f"<td>{inline(c, wiki_prefix)}</td>" for c in r) + "</tr>" for r in body]
            out.append("</tbody></table>")
        elif line.startswith("> "):
            buf = []
            while i < len(lines) and lines[i].startswith(">"):
                buf.append(lines[i][1:].strip())
                i += 1
            i -= 1
            cls = ' class="warn"' if any("⚠️" in b for b in buf) else ""
            out.append(f"<blockquote{cls}>" + "<br>".join(inline(b, wiki_prefix) for b in buf) + "</blockquote>")
        elif re.match(r"^(- |\d+\. )", line):
            tag = "ol" if re.match(r"^\d+\. ", line) else "ul"
            items = []
            while i < len(lines) and re.match(r"^(- |\d+\. )", lines[i]):
                items.append(re.sub(r"^(- |\d+\. )", "", lines[i]))
                i += 1
            i -= 1
            out.append(f"<{tag}>" + "".join(f"<li>{inline(x, wiki_prefix)}</li>" for x in items) + f"</{tag}>")
        elif line.strip():
            out.append(f"<p>{inline(line, wiki_prefix)}</p>")
        i += 1
    return "\n".join(out)


def strip_h1(body):
    return re.sub(r"^# .+\n", "", body.lstrip("\n"), count=1)


HEAD = """<!doctype html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600&family=Noto+Sans+TC:wght@400;500;700;900&display=swap">
<link rel="stylesheet" href="assets/css/deck.css">
</head>
<body>
<main class="page">
<nav class="top"><a href="index.html">首頁</a><a href="deck/index.html">教學簡報</a><a href="wiki.html">LLM Wiki</a><a href="process.html">流程與紀錄</a></nav>
"""
NOTE = "<!-- 本檔由 scripts/build_site.py 產生，請勿手動編輯 -->\n"


def entry(p):
    slug, m = p["slug"], p["meta"]
    meta = []
    if p["kind"] == "concept":
        srcs = [s for s in PAGES if PAGES[s]["kind"] == "source" and source_id(s) in (m.get("sources") or [])]
        meta.append("來源：" + "、".join(f'<a href="#{s}">{source_id(s)}</a>' for s in srcs))
    if p["kind"] == "source":
        meta.append(f'原始檔：<a href="{m.get("raw")}">{html.escape(m.get("raw", ""))}</a>')
    meta.append(f"更新：{m.get('updated', '')}")
    meta.append(f'<a href="https://github.com/Wilson0503/agent-workflow-wiki/blob/main/{p["rel"]}">Markdown 原檔</a>')
    return (
        f'<article class="entry" id="{slug}">\n<h2>{html.escape(m.get("title", slug))}</h2>\n'
        f'<p class="meta">{" ｜ ".join(meta)}</p>\n{render(strip_h1(p["body"]), shift=1)}\n</article>'
    )


def build_wiki():
    index_md = (WIKI / "index.md").read_text(encoding="utf-8")
    toc = render(strip_h1(index_md), shift=1)
    order = ["overview"] + [s for s in PAGES if PAGES[s]["kind"] == "concept"] + [s for s in PAGES if PAGES[s]["kind"] == "source"]
    # 依 index.md 的順序排列概念
    listed = re.findall(r"\[\[([a-z0-9-]+)\]\]", index_md)
    order = [s for s in listed if s in PAGES] + [s for s in order if s not in listed]
    body = HEAD.format(title="LLM Wiki｜AI Agent 工作流程") + NOTE
    body += (
        "<h1>AI Agent 工作流程｜LLM Wiki</h1>\n"
        '<p class="muted">由 6 份課程資料（第 7～10 週）整理成的知識庫：6 頁來源摘要、19 個概念條目、1 頁總覽。'
        "每一點都標出來源（s1～s6），教學簡報的每一頁都連回這裡。用 Obsidian 開啟 <code>wiki/</code> 資料夾可看到關聯圖。</p>\n"
        f'<section class="toc-wrap">{toc}</section>\n'
    )
    body += "\n".join(entry(PAGES[s]) for s in dict.fromkeys(order))
    body += "\n</main>\n</body>\n</html>\n"
    (ROOT / "wiki.html").write_text(body, encoding="utf-8")


def build_process():
    parts = []
    for anchor, name in (("workflow", "workflow.md"), ("run-log", "run-log.md"), ("reflection", "reflection.md")):
        p = ROOT / "docs" / name
        if not p.is_file():
            continue
        md = p.read_text(encoding="utf-8")
        h1 = re.match(r"^# (.+)$", md, re.M)
        parts.append(
            f'<article class="entry" id="{anchor}">\n<h2>{html.escape(h1.group(1) if h1 else name)}</h2>\n'
            f'{render(strip_h1(md), wiki_prefix="wiki.html", shift=1)}\n</article>'
        )
    body = HEAD.format(title="流程與紀錄｜AI Agent 工作流程") + NOTE
    body += "<h1>Loop / Graph 設計與實際執行紀錄</h1>\n" + "\n".join(parts)
    body += (
        '\n</main>\n<script type="module">import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs";'
        'mermaid.initialize({startOnLoad:true,theme:"dark"});</script>\n</body>\n</html>\n'
    )
    (ROOT / "process.html").write_text(body, encoding="utf-8")


if __name__ == "__main__":
    build_wiki()
    build_process()
    print("built: wiki.html, process.html")
