# AI Agent 怎麼做事？從 Loop 到 Graph

生成式 AI 課程第十週作業：先建立一個 **LLM Wiki**，再以 Wiki 為唯一知識來源，透過一條**有檢查點的 Graph 流程**，產出給初學者看的**教學 HTML 簡報**。

- 🌐 網站：https://wilson0503.github.io/agent-workflow-wiki/
- 📽️ 簡報：https://wilson0503.github.io/agent-workflow-wiki/deck/
- 📚 Wiki：https://wilson0503.github.io/agent-workflow-wiki/wiki.html
- 🔁 流程與紀錄：https://wilson0503.github.io/agent-workflow-wiki/process.html

## 架構（Karpathy LLM Wiki）

```
raw/（6 份課程資料，唯讀）→ wiki/（6 來源摘要＋19 概念＋總覽）→ deck/（outline → content → index.html）
```

| 路徑 | 說明 |
|---|---|
| `CLAUDE.md` / `AGENTS.md` | 規則：結構、格式、Graph 流程、煞車、禁止事項 |
| `raw/` | 第 7～10 週課程影片整理與 Karpathy《LLM Wiki》，`docs/raw.sha256` 鎖定內容 |
| `wiki/` | `index.md` 目錄、`log.md` 紀錄、`sources/`、`concepts/`、`overview.md`（Obsidian 可開） |
| `deck/` | `outline.md`（人類審核）、`content.md`（逐頁內容＋引用）、`index.html`（簡報） |
| `docs/` | `workflow.md` 流程設計、`run-log.md` 執行紀錄、`reflection.md` 反思、`screenshots/` |
| `scripts/` | 檢查腳本與網頁產生器 |

## 重跑所有檢查

```bash
python scripts/check_wiki.py              # C1  → WIKI CHECK PASSED
python scripts/check_deck.py --stage html # C2＋內容＋C4 結構 → DECK CHECK PASSED
python scripts/build_site.py              # 產生 wiki.html、process.html
python scripts/render_check.py            # C4 截圖（需 playwright＋Chrome/Edge）→ RENDER CHECK PASSED
```
