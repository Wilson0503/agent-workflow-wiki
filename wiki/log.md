# 知識庫紀錄（wiki/log.md）

> 只能往後追加。查最近 5 筆：`grep "^## \[" wiki/log.md | tail -5`

## [2026-11-23] setup | 建立專案骨架
- 新增：CLAUDE.md、AGENTS.md、templates/、raw/（s1–s6）、docs/raw.sha256

## [2026-11-23] ingest | s1–s6 六份課程資料（批次）
- 新增來源摘要：wiki/sources/s1-rag-demo … s6-loop-and-graph
- 新增概念（19）：ai-agent、harness-engineering、prompt-engineering、context-engineering、rag、llm-wiki、reflection、tool-use、planning、token-cost、reflection-loop、stopping-conditions、graph-workflow、human-checkpoint、over-engineering、agents-md、agent-skills、coding-agent-vs-work-agent、git-version-control
- 新增：wiki/overview.md、wiki/index.md
- 記錄轉錄錯誤：LOP→Loop、Grave→Graph、LM Wiki→LLM Wiki、Graphite Engineering（待確認）

## [2026-11-23] lint | C1 格式檢查 ×5、C1b 事實抽查 ×2
- 修正：3 個定義過長、4 個來源⇄概念不一致、rag 缺 s6 引用
- 修正（審查員）：reflection-loop、rag、over-engineering、tool-use 的常見誤區；agents-md 來源；s2 摘要移除兩處外部資訊
- 規則更新：常見誤區只能寫 raw 有講的；只能用 raw 內容，不可用檔名或常識

## [2026-11-23] publish | 教學簡報 deck/index.html、wiki.html、process.html、首頁
- 新增：deck/outline.md（人類已審）、deck/content.md、deck/index.html、index.html
- 檢查：C2 ×1、R ×2、C4 結構 ×2、C4 截圖 ×4（詳見 docs/run-log.md）
