# AGENTS.md

本專案的完整規則在 **[`CLAUDE.md`](CLAUDE.md)**。任何 AI Agent（Codex、Gemini / Antigravity、OpenCode…）請**先讀完 CLAUDE.md 再動手**，衝突時以 CLAUDE.md 為準。

最重要的五條：

1. `raw/` 唯讀；wiki 只能寫 raw 裡有的事，簡報只能用 wiki 裡有的事。
2. 做簡報一定照 CLAUDE.md 第 5 節的 Graph：N1 → C1 → C1b → N2 → C2 → **H 人類檢查點** → N3 ⇄ R → N4 → C4 → N5。
3. 事實審查（R）要交給另一個 Agent，不能自己審自己。
4. 每個 Loop 最多 3 輪；wiki 跟 raw 都沒有的資訊就停下來問人類。
5. 每個節點的結果（含失敗）都要追加到 `docs/run-log.md`。
