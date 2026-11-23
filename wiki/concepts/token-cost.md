---
title: Token 成本（Token Cost）
slug: token-cost
sources: [s2, s6]
updated: 2026-11-23
---
# Token 成本（Token Cost）

> Agent 每多一個階段就多呼叫一次模型，用量和費用會倍數成長。

## 重點
- 一般問答只呼叫一次模型；Agent 是多階段架構，每階段都呼叫，Token 呈倍數成長（s2）。
- Groq 免費 API 容易跑到一半因額度中斷；改用較小模型可降低中斷機率；商業級應用要用付費 API（s2）。
- 範例程式用預設 False 的測試開關，避免一執行就燒光額度（s2）。
- Loop 要設煞車，防止無效的重複修訂浪費 Token（s6）。

## 例子
- 07C 先打草稿、再生成正文，至少兩次模型呼叫（s2）。

## 常見誤區
- 迴圈設計得越多輪越好——每一輪都要花錢，也可能卡在無窮迴圈（s6）。

## 相關概念
- [[stopping-conditions]] — 控制成本的煞車
- [[planning]] — 多階段架構的例子
- [[over-engineering]] — 流程越複雜越燒錢
