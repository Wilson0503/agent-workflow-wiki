---
title: 控制工程（Harness Engineering）
slug: harness-engineering
sources: [s6, s4]
updated: 2026-11-23
---
# 控制工程（Harness Engineering）

> 設計「告訴 AI 怎麼按步驟做事」的規範、檢查機制與工作流程。

## 重點
- Harness＝告訴 AI 如何按步驟做事的機制、規範與工作流程；它的品質決定 Agent 能不能穩健完成多階段任務（s6）。
- 頂級模型的基礎實力差距已經縮小，實際應用好壞的關鍵在 Harness（s4）。
- Harness 包含引導 AI 做事的方法、檢查機制、工具介面；涵蓋 Prompt、RAG 與機制的設計（s4）。
- Loop、Graph 這些流程設計，都是 Harness 的一部分（s6）。
- 學這些名詞的目的：建立技術認知，「出外不被話術欺騙」（s6）。

## 例子
- 本專案的 CLAUDE.md、檢查腳本、簡報 Graph，就是一套 Harness（s6 的簡報流程）。

## 常見誤區
- 以為換更強的模型就能解決問題。s4 指出模型差距縮小，差別在 Harness。

## 相關概念
- [[ai-agent]] — Agent = Model + Harness
- [[prompt-engineering]]、[[context-engineering]] — Harness 裡處理「問什麼」與「給什麼資料」的部分
- [[reflection-loop]]、[[graph-workflow]] — Harness 裡的流程控制
- [[agents-md]] — Harness 寫成文件的樣子
