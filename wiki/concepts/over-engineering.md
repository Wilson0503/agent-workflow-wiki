---
title: 過度工程化（Over-engineering）
slug: over-engineering
sources: [s6, s3]
updated: 2026-11-23
---
# 過度工程化（Over-engineering）

> 用不必要的複雜流程去解決簡單問題；原則是能簡單就簡單。

## 重點
- 簡單 Prompt 能一次解決的問題，絕不調用 Loop（s6）。
- 標準 Loop 能解決的問題，不要盲目堆疊複雜的 Graph 節點（s6）。
- 好的 Agent 流程應該從人類實際處理事情的自然步驟演化而來（s6）。
- 第八週作業也強調：重點不是做出非常複雜的系統，而是理解方法並讓它實際運作（s3）。

## 例子
- 選工具的順序：Prompt → Loop → Graph，一層不夠才往下一層（s6）。

## 常見誤區
- 一開始就堆疊複雜的 Graph 節點，沒先確認簡單 Prompt 或標準 Loop 是否已經足夠（s6）。

## 相關概念
- [[prompt-engineering]]、[[reflection-loop]]、[[graph-workflow]] — 由簡到繁的三層選擇
- [[token-cost]] — 複雜流程的代價
