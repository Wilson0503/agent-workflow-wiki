---
title: Coding Agent 與 Work Agent
slug: coding-agent-vs-work-agent
sources: [s6, s4]
updated: 2026-11-23
---
# Coding Agent 與 Work Agent

> Work Agent 在對話框工作，Coding Agent 能操作專案資料夾。

## 重點
- Work Agent：ChatGPT / Claude 標準對話介面、CoWork、OpenWorker；不能直接讀寫本機資料夾，沒有原生版本控管（s6）。
- Coding Agent：Google AntiGravity、Claude Code、ChatGPT Codex；綁定專案資料夾，可直接讀寫檔案，整合 Git（s6）。
- Coding Agent 的本質不只是寫程式，而是**模仿人類操作電腦專案資料夾**（s6）。
- 指令只是快捷鍵，不用背，直接用口語交代需求即可（s6）。
- 需要斷線安全與資料隱私時，可用 OpenWorker + Ollama 跑本地小模型，但表現仍不如頂級雲端模型（s4）。

## 例子
- 建 LLM Wiki、自動產生網頁簡報這類任務適合 Coding Agent（s6）。

## 常見誤區
- 看到 "Coding" 就以為只能寫程式（s6）。

## 相關概念
- [[ai-agent]] — 兩者都是 Agent
- [[git-version-control]] — Coding Agent 的優勢之一
- [[tool-use]] — 專案資料夾就是 Coding Agent 的工具
