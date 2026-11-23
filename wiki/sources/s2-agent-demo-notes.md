---
title: 第八週 Agent 實作示範講解（07C Planning）
slug: s2-agent-demo-notes
raw: raw/s2_w08_Agent實作講解.txt
week: 08
updated: 2026-11-23
---
# s2｜第八週 Agent 實作示範講解（07C Planning）

## 這份資料在講什麼
第八週課堂後半段的整理：三個範例 07A Reflection、07B Tool Use（飲料店）、07C Planning（將倒楣事正向轉化的思考生成器），以及老師口頭補充的實務陷阱。

## 重點摘錄
- 07A＝Reflection、07B＝Tool Use（飲料店範例）、07C＝Planning；不熟程式的同學老師推薦 07C。
- **Agent 很燒 Token**：一般問答呼叫一次模型，Agent 是多階段架構（先規劃／打草稿，再正式生成），每階段都呼叫模型，Token 消耗倍數成長。
- Groq 免費 API 容易跑到一半因額度中斷；改用較小模型可降低中斷機率；商業應用要用付費 API。
- 範例程式寫滿預設為 False 的測試開關，避免一執行就燒光額度。
- AI 幫忙寫的 Prompt 常常太長，有些模型吃不下，反而變差，要親自測試並精簡。
- 「AI 思考」的本質是**打草稿**，打草稿的步驟是人類用 System Prompt 教它的（先確認事實 → 評估失落點 → 發想幽默切入點 → 最後生成正文）。

## 產生／更新的概念
- [[planning]] — 07C：先打草稿再生成；思考＝打草稿
- [[token-cost]] — 多階段呼叫讓 Token 倍增、免費 API 限制、測試開關
- [[prompt-engineering]] — AI 寫的長 Prompt 陷阱
- [[tool-use]] — 07B 飲料店範例
- [[reflection]] — 07A 為 Reflection 範例
- [[stopping-conditions]] — 預設 False 的測試開關是程式層的防呆

## 轉錄錯誤與疑點
- 「原因式思考生成器」疑為轉錄錯誤，正確名稱無法從 raw 確認；wiki 一律稱「將倒楣事正向轉化的思考生成器」。
- 原文的範例網址被標成「[suspicious link removed]」，無法得知網址。
- 本整理只涵蓋課堂「五、07C 實作示範」之後；07A、07B 的細節不在這份資料裡。
