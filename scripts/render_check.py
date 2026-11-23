"""C4 的畫面檢查：用無頭瀏覽器實際打開網頁、截圖、偵測文字溢出（課程 Node 4：版面文字是否溢出）。

用法：python scripts/render_check.py
需要：pip install playwright，並且電腦上有 Chrome 或 Edge（不需要 playwright install）。
截圖存到 docs/screenshots/。
"""
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
SHOTS = ROOT / "docs" / "screenshots"
errors = []
err = errors.append

# 找出投影片內「超出投影片邊界」或「壓到頁尾」的元素
OVERFLOW_JS = """
(slide) => {
  const box = slide.getBoundingClientRect();
  const foot = slide.querySelector('footer').getBoundingClientRect();
  const out = [];
  for (const el of slide.querySelectorAll('*')) {
    if (el.closest('footer') || el.closest('defs') || el.closest('.speaker')) continue;
    const r = el.getBoundingClientRect();
    if (!r.width || !r.height) continue;
    const name = el.tagName.toLowerCase() + (el.className && el.className.baseVal === undefined && el.className ? '.' + String(el.className).split(' ')[0] : '');
    const txt = (el.textContent || '').trim().slice(0, 18);
    if (r.right > box.right + 1 || r.left < box.left - 1 || r.top < box.top - 1)
      out.push(`${name}「${txt}」超出投影片邊界`);
    else if (r.bottom > foot.top + 1 && !el.contains(slide.querySelector('footer')))
      out.push(`${name}「${txt}」壓到頁尾引用列（下緣 ${Math.round(r.bottom - foot.top)}px）`);
  }
  // 只回報最外層的問題元素，避免同一個溢出被子元素重複列出
  return [...new Set(out)].slice(0, 4);
}
"""


# SVG 圖解：文字不可壓在箭頭線上、文字之間不可互相重疊（第一次視覺檢查發現腳本漏掉這類問題後新增）
SVG_OVERLAP_JS = """
(slide) => {
  const out = [];
  for (const svg of slide.querySelectorAll('svg.diagram')) {
    const texts = [...svg.querySelectorAll('text')].map(t => ({t, b: t.getBBox()}));
    const inside = (b, x, y, pad) => x > b.x - pad && x < b.x + b.width + pad && y > b.y - pad && y < b.y + b.height + pad;
    for (const path of svg.querySelectorAll('path.fwd, path.ret')) {
      const len = path.getTotalLength();
      for (const {t, b} of texts) {
        for (let s = 0; s <= len; s += 3) {
          const pt = path.getPointAtLength(s);
          if (inside(b, pt.x, pt.y, 1)) { out.push(`圖解文字「${t.textContent}」壓到箭頭線`); break; }
        }
      }
    }
    for (let i = 0; i < texts.length; i++) for (let j = i + 1; j < texts.length; j++) {
      const a = texts[i].b, c = texts[j].b;
      if (a.x < c.x + c.width && c.x < a.x + a.width && a.y < c.y + c.height && c.y < a.y + a.height)
        out.push(`圖解文字「${texts[i].t.textContent}」與「${texts[j].t.textContent}」重疊`);
    }
  }
  return [...new Set(out)];
}
"""


def launch(p):
    for channel in ("chrome", "msedge"):
        try:
            return p.chromium.launch(channel=channel)
        except Exception:  # noqa: BLE001
            continue
    raise SystemExit("找不到 Chrome 或 Edge")


def collect_console(page, label):
    page.on("console", lambda m: m.type == "error" and err(f"{label}: console error：{m.text}"))
    page.on("pageerror", lambda e: err(f"{label}: JS 例外：{e}"))


def main():
    SHOTS.mkdir(parents=True, exist_ok=True)
    deck_url = (ROOT / "deck" / "index.html").as_uri()
    with sync_playwright() as p:
        browser = launch(p)

        # ---- 桌機：逐頁截圖＋溢出偵測 ----
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        collect_console(page, "desktop")
        page.goto(deck_url)
        page.wait_for_load_state("networkidle")
        page.evaluate("document.fonts.ready")
        n = page.evaluate("window.deck.count")
        for i in range(n):
            page.evaluate(f"window.deck.show({i})")
            page.wait_for_timeout(120)
            slide = page.locator(".slide.active")
            sid = slide.get_attribute("id")
            for problem in slide.evaluate(OVERFLOW_JS) + slide.evaluate(SVG_OVERLAP_JS):
                err(f"desktop {sid}: {problem}")
            slide.screenshot(path=str(SHOTS / f"desktop-{sid}.png"))

        # ---- 鍵盤翻頁、講義模式 ----
        page.evaluate("window.deck.show(0)")
        page.keyboard.press("ArrowRight")
        if page.locator(".slide.active").get_attribute("id") != "S02":
            err("desktop: 按 → 沒有翻到 S02")
        page.keyboard.press("ArrowLeft")
        if page.locator(".slide.active").get_attribute("id") != "S01":
            err("desktop: 按 ← 沒有回到 S01")
        page.click('[data-act="handout"]')
        visible = page.evaluate("[...document.querySelectorAll('.slide')].filter(s => s.offsetParent !== null).length")
        if visible != n:
            err(f"desktop: 講義模式應顯示 {n} 張，實際 {visible} 張")
        page.screenshot(path=str(SHOTS / "desktop-handout.png"), full_page=True)
        page.close()

        # ---- 手機：不可有橫向捲動、元素不可超出投影片 ----
        mpage = browser.new_page(viewport={"width": 390, "height": 844}, device_scale_factor=2)
        collect_console(mpage, "mobile")
        mpage.goto(deck_url)
        mpage.wait_for_load_state("networkidle")
        if mpage.evaluate("document.documentElement.scrollWidth > window.innerWidth + 1"):
            err("mobile: 簡報頁出現橫向捲動")
        for sid in mpage.evaluate("[...document.querySelectorAll('.slide')].map(s => s.id)"):
            for problem in mpage.locator(f"#{sid}").evaluate(OVERFLOW_JS.replace("r.bottom > foot.top + 1", "false")):
                err(f"mobile {sid}: {problem}")
        mpage.screenshot(path=str(SHOTS / "mobile-deck.png"), full_page=True)

        # ---- 其他頁面 ----
        for name in ("index.html", "wiki.html", "process.html"):
            mpage.goto((ROOT / name).as_uri())
            mpage.wait_for_load_state("networkidle")
            if mpage.evaluate("document.documentElement.scrollWidth > window.innerWidth + 1"):
                err(f"mobile {name}: 出現橫向捲動")
            mpage.screenshot(path=str(SHOTS / f"mobile-{name.replace('.html', '')}.png"))
        browser.close()

    print(f"截圖：{SHOTS.relative_to(ROOT)}/（{n} 張桌機投影片＋講義模式＋手機）")
    if errors:
        print(f"\nRENDER CHECK FAILED — {len(errors)} 個錯誤：")
        for e in errors:
            print("  ✗", e)
        sys.exit(1)
    print("RENDER CHECK PASSED")


if __name__ == "__main__":
    main()
