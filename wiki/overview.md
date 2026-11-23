---
title: 主題總覽：AI Agent 怎麼做事？
slug: overview
sources: [s1, s2, s3, s4, s5, s6]
updated: 2026-11-23
---
# 主題總覽：AI Agent 怎麼做事？

> 一頁讀懂整個 wiki：Agent = Model + Harness，而 Harness 的核心是「怎麼安排步驟、怎麼檢查」。

## 一條主線
1. **Agent 是什麼**：[[ai-agent]] = Model + [[harness-engineering]]。和對話型 AI 的差別是多步驟自主執行、會用工具、能操作檔案（s4、s6）。
2. **給它對的資訊**：[[prompt-engineering]] 管「怎麼問」，[[context-engineering]] 管「給什麼資料」；做法有 [[rag]] 與 [[llm-wiki]]（s1、s5、s6）。
3. **三種基本做事方法**：[[reflection]]、[[tool-use]]、[[planning]]（s3、s2）。
4. **把步驟串成流程**：固定來回的 [[reflection-loop]]，與可依條件跳躍的 [[graph-workflow]]（s6）。
5. **讓流程可控**：[[stopping-conditions]] 防止無窮迴圈、[[token-cost]] 提醒每一步都要錢、[[human-checkpoint]] 讓人在最划算的時機介入（s2、s6）。
6. **別做過頭**：[[over-engineering]]——Prompt → Loop → Graph，一層不夠才往下一層（s6）。
7. **寫成規則、留下版本**：[[agents-md]]、[[agent-skills]]、[[coding-agent-vs-work-agent]]、[[git-version-control]]（s4、s5、s6）。

## 來源一覽
- [[s1-rag-demo]]、[[s2-agent-demo-notes]]、[[s3-three-agent-patterns]]、[[s4-harness-and-agents-md]]、[[s5-karpathy-llm-wiki]]、[[s6-loop-and-graph]]
