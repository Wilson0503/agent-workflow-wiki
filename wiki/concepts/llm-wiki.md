---
title: LLM 知識庫（LLM Wiki）
slug: llm-wiki
sources: [s5, s6, s4]
updated: 2026-11-23
---
# LLM 知識庫（LLM Wiki）

> 讓 LLM 把原始資料整理成互相連結的 Markdown 頁面，並持續維護。

## 重點
- 三層：raw（原始資料，不可修改）→ wiki（LLM 撰寫維護）→ schema（CLAUDE.md / AGENTS.md 規則）（s5）。
- 三種操作：Ingest（吸收新資料）、Query（查詢並附引用）、Lint（健康檢查：矛盾、孤兒頁、缺頁）（s5）。
- 和 RAG 不同：知識「編譯一次、持續更新」，交叉引用和矛盾都已整理好，會越來越豐富（s5）。
- 不用轉向量，靠 `index.md` 目錄讓 Agent 直接找到頁面；人和 LLM 都看得懂，找對找錯一目瞭然（s6、s4）。
- 建置前 AI 要先訪談：研究廣度深度、來源格式、連結風格、語言與公式規則（s6）。
- 用 Obsidian 開啟 wiki 資料夾，Graph View 會把雙向連結畫成網絡圖（s6、s5）。

## 例子
- 本專案就是一個 LLM Wiki：6 份課程資料 → 來源摘要＋概念條目 → 教學簡報。

## 常見誤區
- 以為 LLM Wiki 是給人線性閱讀的文章；它主要是讓 AI 在 context 中檢索、提取（s6）。

> ⚠️ 來源差異：s6 說 Karpathy「最初也試圖建置傳統 RAG，後來發現…」，但 s5（Karpathy 原文）沒有提到這段經歷。本 wiki 不把這段當成 Karpathy 的說法。

## 相關概念
- [[rag]] — 對照組
- [[context-engineering]] — LLM Wiki 是提供 context 的方法
- [[agents-md]] — LLM Wiki 的 schema 層
- [[git-version-control]] — wiki 就是一個 git repo
