---
title: AI 代理（AI Agent）
slug: ai-agent
sources: [s4, s6, s3]
updated: 2026-11-23
---
# AI 代理（AI Agent）

> 會自己多步驟做事、用工具、讀寫檔案的 AI：Model + Harness。

## 重點
- 公式：**AI Agent = AI Model + Harness**；Model 負責理解與生成語言，Harness 負責「怎麼按步驟做事」（s6、s4）。
- 和對話型 AI 的差別：對話型是一問一答、全程要人在場；Agent 是多步驟自主執行，交代完可以離場（s4）。
- Agent 能讀寫本機檔案、建資料夾、開瀏覽器、調用工具，產出的是完整專案成果，而不只是一段回答（s4）。
- 人的角色從「打工仔」變成「管理者／老闆」：只要下達目標與驗收標準（s4）。
- 三種基本做事方法：Reflection、Tool Use、Planning（s3）。

## 例子
- 桌面檔案分類器：Agent 讀目錄、擬分類計畫、等確認後自己搬檔案並回報（s4）。

## 常見誤區
- 以為 Agent 是「更聰明的聊天視窗」。差別不在模型，而在 Harness 讓它能多步驟執行、操作檔案和工具（s4、s6）。

## 相關概念
- [[harness-engineering]] — Agent 的另一半
- [[reflection]]、[[tool-use]]、[[planning]] — Agent 的三種基本做事方法
- [[coding-agent-vs-work-agent]] — 市面上 Agent 工具的兩大類
