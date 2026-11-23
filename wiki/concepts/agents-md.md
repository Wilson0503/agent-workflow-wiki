---
title: 員工手冊（AGENTS.md / CLAUDE.md）
slug: agents-md
sources: [s4, s5, s6]
updated: 2026-11-23
---
# 員工手冊（AGENTS.md / CLAUDE.md）

> 放在專案資料夾裡的規則檔，告訴 AI 這個專案要做什麼、怎麼做、做到什麼程度。

## 重點
- 常見檔名：agent.md（通用慣例）、claude.md（Claude）、gemini.md（Gemini）；模型載入資料夾時會自動讀取（s4）。Karpathy 也舉 CLAUDE.md、AGENTS.md 為例（s5）。
- 好的交辦四要素：**成果定義**、**約束條件**、**驗收標準**、**先計畫後執行**（s4）。
- 在 LLM Wiki 裡它是 schema 層：讓 LLM 成為有紀律的 wiki 維護者，由人和 LLM 一起持續調整（s5）。
- 第十週稱它為「專案憲法與員工作業手冊」，規範目錄結構（agent.md、papers/、wiki/、assets/）（s6）。

## 例子
- 約束條件例子：絕對不可刪除原始檔；無法分類的放進「待確認」資料夾（s4）。

## 常見誤區
- 把規則散落在對話裡；s4 指出應寫成規格書，取代散亂的對話提示詞。

## 相關概念
- [[harness-engineering]] — 員工手冊是 Harness 的書面形式
- [[llm-wiki]] — schema 層
- [[agent-skills]] — 手冊寫原則，Skill 寫具體 SOP
