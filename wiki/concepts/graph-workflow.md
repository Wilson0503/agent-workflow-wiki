---
title: 圖形工作流（Graph）
slug: graph-workflow
sources: [s6]
updated: 2026-11-23
---
# 圖形工作流（Graph）

> 把流程拆成多個節點，依條件在節點之間前進、跳回或重來。

## 重點
- 每個節點（Node）只專注一個獨立任務，例如 A 寫大綱、B 檢查邏輯漏洞、C 輸出評估報告（s6）。
- **動態條件跳躍**：流程不是直線；在 C 發現原始資料遺漏，可以跳回 B，甚至退回 A，補齊後再往前（s6）。
- 和 Loop 的差別：Loop 是固定的「產生 ⇄ 審查」來回；Graph 可以在不同節點間依條件自由跳躍與回溯，彈性更高（s6）。
- 簡報 Graph 範例：大綱 → 逐頁內容 → HTML 渲染 → 自動驗證；驗證不過就跳回逐頁內容或大綱（s6）。
- 驗證節點檢查：圖片路徑是否斷連結、引用是否精準、版面文字是否溢出（s6）。

## 例子
- s6 的四節點簡報流程；本專案在它之上加了 Wiki 檢查、大綱檢查與事實審查。

## 常見誤區
- 一開始就畫複雜 Graph。s6 提醒 Loop 能解決的問題不要過度工程化（見 [[over-engineering]]）。

## 相關概念
- [[reflection-loop]] — 比 Graph 簡單的固定迴圈
- [[human-checkpoint]] — Graph 中人類介入的節點
- [[stopping-conditions]] — 回跳也需要上限
- [[over-engineering]] — 什麼時候不該用 Graph
