---
title: 上下文工程（Context Engineering）
slug: context-engineering
sources: [s6, s1]
updated: 2026-11-23
---
# 上下文工程（Context Engineering）

> 把足夠而且正確的背景資料交給 AI，讓它不用亂猜。

## 重點
- 聚焦在如何構建並傳遞「足夠充分且正確的背景資訊」給 AI（s6）。
- 核心目的是避免 AI 在資訊不足時盲目猜測或產生幻覺（s6）。
- 常見做法：傳統 RAG，以及本課程實作的 LLM Wiki（s6）。
- RAG 把檢索到的背景資料和問題一起放進 Prompt，讓 LLM 像做「閱讀測驗」一樣作答（s1）。

## 例子
- 第七週 RAG 機器人測試時要確認它「嚴格根據資料回答，而不是自行幻想」（s1）。

## 常見誤區
- 只顧著改問法（Prompt），卻沒給 AI 需要的資料；資料不夠時 AI 只能猜（s6）。

## 相關概念
- [[prompt-engineering]] — 上一層：怎麼問
- [[rag]]、[[llm-wiki]] — 兩種提供 context 的做法
- [[harness-engineering]] — Context Engineering 是 Harness 的一環
