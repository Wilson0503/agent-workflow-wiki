---
title: 反思迴圈（Reflection Loop）
slug: reflection-loop
sources: [s6]
updated: 2026-11-23
---
# 反思迴圈（Reflection Loop）

> 作者 Agent 產生、審查員 Agent 挑錯，反覆修訂直到合格或觸發煞車。

## 重點
- 三步驟：作者 Agent 產生初版 → 審查員 Agent 依品質標準列缺點與修正建議 → 作者修訂後再送審（s6）。
- 設計 Agent 時，重點已從寫單次 Prompt 轉向設計 Prompt Loop（s6）。
- 成功關鍵一：**客觀的放行條件**，審查員才知道什麼時候可以放行（s6）。
- 成功關鍵二：**煞車機制**，避免無窮迴圈和浪費 Token（s6）。
- 流程是固定的「產生 ⇄ 審查」來回，不會跳到其他步驟（s6，與 Graph 對比）。

## 例子
- 來源未提供課堂實例；本專案簡報的 N3 ⇄ R 事實審查就是一個 Reflection Loop。

## 常見誤區
- 沒有分工、也沒有客觀放行條件時，審查員無從判斷何時可以放行（s6）。

## 相關概念
- [[reflection]] — 第八週的單一 Agent 版本
- [[stopping-conditions]] — Loop 必備的煞車
- [[graph-workflow]] — 更有彈性的流程架構
- [[harness-engineering]] — Loop 是 Harness 的一部分
