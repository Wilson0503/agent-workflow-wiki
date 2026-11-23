---
title: Karpathy — LLM Wiki（idea file）
slug: s5-karpathy-llm-wiki
raw: raw/s5_w09_Karpathy_LLM_Wiki.txt
week: 09
updated: 2026-11-23
---
# s5｜Karpathy《LLM Wiki》

## 這份資料在講什麼
Andrej Karpathy 的 gist（英文原文）：一種讓 LLM 持續建立、維護個人知識庫的模式，以及它和 RAG 的差別、三層架構、三種操作、index / log 兩個特殊檔案。

## 重點摘錄
- RAG 每次提問都從原始文件「重新發現」知識，沒有累積；LLM Wiki 是 LLM **逐步建立並維護的持久 wiki**，知識編譯一次、持續更新。
- 三層：**raw sources**（不可修改，事實來源）→ **wiki**（LLM 全權撰寫維護）→ **schema**（CLAUDE.md / AGENTS.md，規定結構、慣例與流程）。
- schema 讓 LLM 成為「有紀律的 wiki 維護者，而不是一般聊天機器人」，由人和 LLM 一起持續調整。
- 三種操作：**Ingest**（讀來源、討論重點、寫摘要、更新相關頁、記 log）、**Query**（讀 index 找頁面、附引用回答，好答案可存回 wiki）、**Lint**（找矛盾、過時說法、孤兒頁、缺頁）。
- `index.md` 是內容目錄；`log.md` 是只追加的時間序紀錄，用固定前綴 `## [日期] ingest | 標題` 方便 grep。
- 中等規模（約 100 份來源）只靠 index 檔就夠，不需要 embedding RAG。
- 人負責挑資料、引導分析、問好問題；LLM 負責摘要、交叉引用、歸檔等雜務。wiki 就是一個 git repo，有版本歷史。

## 產生／更新的概念
- [[llm-wiki]] — 三層架構、三種操作
- [[rag]] — RAG 沒有累積
- [[agents-md]] — schema 檔的角色
- [[human-checkpoint]] — 作者偏好一次 ingest 一份並親自檢查
- [[git-version-control]] — wiki 就是 git repo

## 轉錄錯誤與疑點
- 無（原文為英文文件）。
