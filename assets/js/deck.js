// deck.js — 全站唯一 JS：翻頁、頁碼、路線圖、講義模式（CLAUDE.md 第 6 節）
(function () {
  const slides = Array.from(document.querySelectorAll(".slide"));
  if (!slides.length) return;
  const route = document.querySelector(".route");
  const pos = document.querySelector("[data-pos]");
  const handoutBtn = document.querySelector('[data-act="handout"]');
  let cur = 0;

  // 路線圖：每張投影片一個節點
  const dots = slides.map((s, i) => {
    const a = document.createElement("a");
    a.href = "#" + s.id;
    a.setAttribute("aria-label", `第 ${i + 1} 頁：${s.querySelector("h1, h2").textContent}`);
    a.addEventListener("click", (e) => { e.preventDefault(); show(i); });
    route && route.appendChild(a);
    return a;
  });

  function show(i) {
    cur = Math.max(0, Math.min(slides.length - 1, i));
    slides.forEach((s, k) => s.classList.toggle("active", k === cur));
    dots.forEach((d, k) => {
      d.classList.toggle("seen", k <= cur);
      d.classList.toggle("current", k === cur);
      if (k === cur) d.setAttribute("aria-current", "step"); else d.removeAttribute("aria-current");
    });
    if (pos) pos.textContent = `${cur + 1} / ${slides.length}`;
    history.replaceState(null, "", "#" + slides[cur].id);
  }

  document.addEventListener("keydown", (e) => {
    if (document.body.classList.contains("handout")) return;
    if (["ArrowRight", "PageDown", " "].includes(e.key)) { e.preventDefault(); show(cur + 1); }
    if (["ArrowLeft", "PageUp"].includes(e.key)) { e.preventDefault(); show(cur - 1); }
    if (e.key === "Home") show(0);
    if (e.key === "End") show(slides.length - 1);
  });
  document.querySelectorAll('[data-act="prev"]').forEach((b) => b.addEventListener("click", () => show(cur - 1)));
  document.querySelectorAll('[data-act="next"]').forEach((b) => b.addEventListener("click", () => show(cur + 1)));

  function setHandout(on) {
    document.body.classList.toggle("handout", on);
    if (handoutBtn) {
      handoutBtn.textContent = on ? "回到投影片" : "講義模式";
      handoutBtn.setAttribute("aria-pressed", String(on));
    }
  }
  handoutBtn && handoutBtn.addEventListener("click", () => setHandout(!document.body.classList.contains("handout")));

  const start = slides.findIndex((s) => "#" + s.id === location.hash);
  show(start >= 0 ? start : 0);
  window.deck = { show, count: slides.length, setHandout };
})();
