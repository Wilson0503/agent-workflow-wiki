"""C4 的結構檢查（由 check_deck.py --stage html 呼叫）。

檢查 deck/index.html：
- 基本：lang、viewport、不可有 <style> / style=""、只能用 deck.css / deck.js
- 資產：所有 src / href 指到的本機檔案都要存在（課程 Node 4：圖片路徑不可斷），不可外連圖片
- 對應：投影片編號、data-cites、頁尾引用 chip 與 content.md 一致；content.md 每一點文字都要出現在該頁
- 錨點：../wiki.html#slug 的 slug 必須真的存在於 wiki.html
"""
import re
from html.parser import HTMLParser
from pathlib import Path

ALLOWED_EXTERNAL = ("https://fonts.googleapis.com", "https://fonts.gstatic.com")
PSEUDO_TARGET = {"project": "../process.html#workflow"}


class Parser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.html_lang = None
        self.viewport = False
        self.style_tags = 0
        self.style_attrs = []
        self.refs = []          # (tag, attr, value)
        self.slides = []        # dict(id, cites, text, chips)
        self.depth = 0
        self.slide_depth = None
        self.in_footer = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag not in ("meta", "link", "br", "img", "input", "path", "rect", "line", "circle", "polyline", "source"):
            self.depth += 1
        if tag == "html":
            self.html_lang = a.get("lang")
        if tag == "meta" and a.get("name") == "viewport":
            self.viewport = True
        if tag == "style":
            self.style_tags += 1
        if "style" in a:
            self.style_attrs.append(tag)
        for attr in ("href", "src"):
            if a.get(attr):
                self.refs.append((tag, attr, a[attr], a.get("rel", ""), a.get("class", "")))
        cls = (a.get("class") or "").split()
        if tag == "section" and "slide" in cls:
            self.slides.append({"id": a.get("id"), "cites": (a.get("data-cites") or "").split(), "text": "", "chips": []})
            self.slide_depth = self.depth
        if self.slide_depth is not None:
            if tag == "footer":
                self.in_footer = True
            if tag == "a" and "cite" in cls:
                self.slides[-1]["chips"].append(a.get("href", ""))

    def handle_endtag(self, tag):
        if tag == "footer":
            self.in_footer = False
        if tag not in ("meta", "link", "br", "img", "input", "path", "rect", "line", "circle", "polyline", "source"):
            if self.slide_depth is not None and self.depth == self.slide_depth and tag == "section":
                self.slide_depth = None
            self.depth -= 1

    def handle_data(self, data):
        if self.slide_depth is not None and not self.in_footer:
            self.slides[-1]["text"] += data


def norm(s):
    """比對用：忽略空白與全形冒號（版面會把「標題：內容」拆成標題元素＋內容元素）。"""
    return re.sub(r"[\s：]+", "", s)


def wiki_anchors(root):
    p = root / "wiki.html"
    if not p.is_file():
        return None
    return set(re.findall(r'id="([a-z0-9-]+)"', p.read_text(encoding="utf-8")))


def check_html_file(path, content, valid):
    errors = []
    err = errors.append
    if not path.is_file():
        return [f"{path.name} 不存在（N4 尚未執行）"]
    root = path.parent.parent
    p = Parser()
    p.feed(path.read_text(encoding="utf-8"))
    name = "deck/index.html"

    if p.html_lang != "zh-Hant":
        err(f"{name}: <html lang> 必須是 zh-Hant")
    if not p.viewport:
        err(f"{name}: 缺少 <meta name=viewport>")
    if p.style_tags:
        err(f"{name}: 不可使用 <style>")
    if p.style_attrs:
        err(f"{name}: 不可使用 style=\"\"（出現在 {sorted(set(p.style_attrs))}）")

    css = [v for t, at, v, rel, _ in p.refs if t == "link" and "stylesheet" in rel and not v.startswith(ALLOWED_EXTERNAL)]
    if css != ["../assets/css/deck.css"]:
        err(f"{name}: 樣式表只能是 ../assets/css/deck.css，目前 {css}")
    js = [v for t, at, v, *_ in p.refs if t == "script"]
    if js != ["../assets/js/deck.js"]:
        err(f"{name}: JS 只能是 ../assets/js/deck.js，目前 {js}")

    anchors = wiki_anchors(root)
    if anchors is None:
        err("wiki.html 不存在 → 先執行 python scripts/build_site.py")
    for tag, attr, val, *_ in p.refs:
        if val.startswith(("http://", "https://")):
            if tag in ("img", "source") or not val.startswith(ALLOWED_EXTERNAL):
                err(f"{name}: 不可外連 <{tag} {attr}={val}>")
            continue
        if val.startswith(("#", "mailto:", "url(#")):
            continue
        target, _, frag = val.partition("#")
        f = (path.parent / target).resolve()
        if not f.exists():
            err(f"{name}: <{tag} {attr}=\"{val}\"> 指到不存在的檔案（斷連結）")
        elif f.name == "wiki.html" and frag and anchors is not None and frag not in anchors:
            err(f"{name}: {val} 的錨點 #{frag} 在 wiki.html 不存在")

    ids = [s["id"] for s in p.slides]
    if ids != list(content):
        err(f"{name}: 投影片 id {ids} 與 content.md {list(content)} 不一致")
    for s in p.slides:
        c = content.get(s["id"])
        if not c:
            continue
        sid = s["id"]
        if set(s["cites"]) != set(c["cites"]):
            err(f"{name} {sid}: data-cites {sorted(s['cites'])} 與 content.md {sorted(c['cites'])} 不一致 → 回 N3/N4")
        for slug in s["cites"]:
            if slug not in valid:
                err(f"{name} {sid}: data-cites 的 {slug} 不存在")
        expected = {PSEUDO_TARGET.get(slug, f"../wiki.html#{slug}") for slug in c["cites"]}
        if set(s["chips"]) != expected:
            err(f"{name} {sid}: 頁尾引用 chip {sorted(s['chips'])} 應為 {sorted(expected)}")
        text = norm(s["text"])
        for b in c.get("bullets", []) + c.get("answers", []):
            if norm(b) not in text:
                err(f"{name} {sid}: content.md 的這句沒有出現在投影片上：{b[:24]}…")
    return errors
