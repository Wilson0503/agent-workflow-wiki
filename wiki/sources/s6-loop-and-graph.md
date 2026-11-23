---
title: 第十週課程：工作流程拆解與 Agent 架構（Loop 與 Graph）
slug: s6-loop-and-graph
raw: raw/s6_w10_Loop與Graph課程說明.txt
week: 10
updated: 2026-11-23
---
# s6｜第十週：Loop 與 Graph

## 這份資料在講什麼
第十週 1:52:00 課程精華整理：Agent = Model + Harness、Prompt / Context Engineering、Work Agent 與 Coding Agent、Reflection Loop 與 Graph 架構、LLM Wiki 建置，以及用 Graph 把 LLM Wiki 轉成 HTML 簡報的四節點流程。

## 重點摘錄
- Harness＝「告訴 AI 如何按步驟做事的機制、規範與工作流程」，品質決定 Agent 能否穩健完成多階段任務。學名詞是為了「出外不被話術欺騙」。
- Prompt Engineering：設計提問、多輪討論修正。Context Engineering：給 AI 足夠且正確的背景資訊（RAG、LLM Wiki），避免它在資訊不足時亂猜或幻覺。
- Coding Agent 不只寫程式，本質是「模仿人類操作電腦專案資料夾」；指令只是快捷鍵，直接用口語交代即可。
- **Reflection Loop**：作者 Agent 產生 → 審查員 Agent 依標準列缺點與建議 → 作者修訂再送審。成功關鍵：客觀放行條件＋煞車機制（最多 3～5 次、資訊不足即停、控管 Token 成本）。
- **Graph**：每個 Node 專注一件事，流程可依條件在節點間跳躍、回溯（例如在輸出報告階段發現資料遺漏，就跳回審查或大綱節點）。
- 設計心法：簡單 Prompt 能解決就不用 Loop；Loop 能解決就不要過度工程化堆 Graph。流程應從人類實際做事的步驟演化而來。
- LLM Wiki 建置前 AI 要先訪談（廣度深度、來源格式、連結風格、語言與公式規則），再產生 agent.md 專案憲法。Obsidian Graph View 可把雙向連結畫成網絡圖。
- 簡報 Graph：Node 1 大綱（**人類最佳檢查點**，在這裡修正可避免重做 HTML）→ Node 2 逐頁內容 → Node 3 HTML/CSS 渲染 → Node 4 自動驗證（圖片路徑、引用、文字溢出），不通過就跳回 Node 2 或 Node 1。
- Git 是本機版本控管、GitHub 是雲端平台；AI 搞砸檔案時可用 Git 復原。

## 產生／更新的概念
- [[harness-engineering]]、[[prompt-engineering]]、[[context-engineering]]
- [[coding-agent-vs-work-agent]]
- [[reflection]]、[[reflection-loop]]、[[stopping-conditions]]、[[token-cost]]
- [[graph-workflow]]、[[human-checkpoint]]、[[over-engineering]]
- [[llm-wiki]]、[[agents-md]]、[[rag]]、[[git-version-control]]、[[ai-agent]]

## 轉錄錯誤與疑點
- 「LOP」應為「Loop」（原文把 Reflection Loop 簡寫成 LOP）。
- 「Grave（Graph／圖形）架構」應為「Graph」。
- 「LM Wiki」應為「LLM Wiki」；「日系可愛粉采風」應為「粉彩風」。
- 「Karpathy 最初亦試圖建置傳統 RAG，但隨後發現…」：s5 原文沒有提到這段經歷，只說中等規模不需要 embedding RAG。wiki 只寫「s6 這樣說」，不當成 Karpathy 的原話。
