---
title: 提示工程（Prompt Engineering）
slug: prompt-engineering
sources: [s6, s1, s2]
updated: 2026-11-23
---
# 提示工程（Prompt Engineering）

> 設計怎麼問 AI，並透過多輪討論修正，提煉出最好的產出。

## 重點
- 聚焦在設計提問指令，以及和 AI 多輪反覆討論、互動修正的技巧（s6）。
- System Prompt 放角色與規則，User Prompt 放使用者問題；RAG 會把檢索資料和問題組合進 Prompt（s1）。
- Prompt 也要設計「找不到資料時怎麼回答」，並改成符合情境的句子（s1）。
- AI 幫忙寫的 Prompt 常常過長，有些模型吃不下反而變差，要親自測試並精簡（s2）。
- 簡單 Prompt 能一次解決的問題，就不需要 Loop（s6）。

## 例子
- 07C 用 System Prompt 教 AI 打草稿的步驟：先確認事實 → 評估失落點 → 發想幽默切入點 → 生成正文（s2）。

## 常見誤區
- 「Prompt 越長越詳細越好」——s2 提醒過長反而會壞掉。

## 相關概念
- [[context-engineering]] — 下一層：不只問得好，還要給足資料
- [[over-engineering]] — Prompt 能解決就不要用 Loop
- [[planning]] — 打草稿的步驟是靠 Prompt 教的
