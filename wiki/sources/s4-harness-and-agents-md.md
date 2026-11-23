---
title: 第九週課程大綱：Agent 原理、Harness 與專案構建
slug: s4-harness-and-agents-md
raw: raw/s4_w09_Harness與AGENTS課程大綱.txt
week: 09
updated: 2026-11-23
---
# s4｜第九週：Agent 原理、Harness 與專案構建

## 這份資料在講什麼
第九週簡報文件整理：從「對話型 LLM」到「代理型 AI Agent」的範式轉移、Harness Engineering、專案資料夾與 agent.md / claude.md 員工手冊、Skill 打包、工具比較、三個實務案例，以及 SIMA 研究與神經網路訓練的複習（後兩者與本主題無關，未收錄）。

## 重點摘錄
- 使用者角色從手動整理資料的「打工仔」，變成只下達目標與驗收標準的「管理者／老闆（出一張嘴）」。
- 對話型 AI：一問一答、全程需人工在場、只在對話框內生成文字。Agent：多步驟自主執行、交代任務後可離場、可讀寫本機檔案、調用工具，產出完整專案成果。
- **AI Agent = AI Model（LLM 大腦）+ Harness**；頂級模型基礎實力差距縮小，決定優劣的是 Harness（引導 AI 做事的方法、檢查機制、工具介面）。Harness 涵蓋 Prompt、RAG、機制的設計。
- 員工手冊 agent.md / claude.md / gemini.md：寫清楚**成果定義、約束條件、驗收標準、先計畫後執行**。
- 做出滿意的流程後，可請 AI 把 SOP 打包成 **Skill**，之後反覆調用，品質與風格不會隨機波動。
- 案例「桌面檔案分類器」：Agent 先擬 5 類分類計畫 → 管理員確認 → 才建資料夾、搬檔案 → 回報結果。
- LLM Wiki 比向量 RAG 更可解釋：人和 LLM 都能直接讀 `index.md` 與條目，「找對找錯一目瞭然」。
- 簡報要求：首頁 `index.html` 集中連結所有簡報；GitHub 要上傳完整專案（規則檔、assets、中間產物），評分看規則檔與專案引導結構。

## 產生／更新的概念
- [[ai-agent]] — 對話型 AI 與 Agent 的比較
- [[harness-engineering]] — Agent = Model + Harness
- [[agents-md]] — 員工手冊的四個要素
- [[agent-skills]] — 把 SOP 打包成 Skill
- [[human-checkpoint]] — 先計畫後執行、管理員確認
- [[llm-wiki]] — 可解釋性、index.md
- [[rag]] — 向量 RAG 的黑盒子缺點
- [[tool-use]] — Agent 調用工具
- [[planning]] — 先計畫後執行
- [[coding-agent-vs-work-agent]] — OpenWorker + Ollama 本地方案

## 轉錄錯誤與疑點
- 「LMWiki」應為「LLM Wiki」。
- 「RAG Engineering 與 Graphite Engineering 等均屬於 Harness 的分支」：「Graphite Engineering」疑為轉錄錯誤（可能指第十週的 Graph），無法從 raw 確認，wiki 不採用此名詞。
- 「與 AI 討訪」應為「討論」。
