---
title: 第七週 RAG 作業範例講解
slug: s1-rag-demo
raw: raw/s1_w07_RAG範例講解.txt
week: 07
updated: 2026-11-23
---
# s1｜第七週 RAG 作業範例講解

## 這份資料在講什麼
課程影片 1:22:02～1:49:50 的整理：老師用「勞動部工讀生權益」示範資料集，講解兩支 Colab 程式——R01 建立並匯出向量資料庫、R02 載入向量庫做 RAG 對話機器人並用 Gradio 展示，以及作業哪些地方不能照抄。

## 重點摘錄
- 資料集先切成一塊塊 `.txt`，每塊有標題、Metadata、要做 Embedding 的內文、練習檢索問題。
- R01：安裝 sentence-transformers 與 FAISS → 載入 Embedding 模型 → 內文轉向量 → **打包前先用測試問題驗證檢索結果** → 匯出 zip。
- R02：用 API 呼叫 LLM（範例用 Groq）→ 載入向量庫 → System Prompt＋User Prompt 把檢索到的資料和問題結合，讓 LLM 像做「閱讀測驗」一樣回答。
- 測試時要確認機器人「嚴格根據資料回答，而不是自行幻想（Hallucination）」。
- 找不到資料時的回應要改成符合情境的句子（例如「本資料庫中查無相關規定」）。
- R02 必須自動下載向量庫，助教按「全部執行」就能跑。

## 產生／更新的概念
- [[rag]] — RAG 的完整流程與「先驗證檢索再打包」
- [[context-engineering]] — 把檢索到的背景資料放進 Prompt，避免幻覺
- [[prompt-engineering]] — System Prompt / User Prompt 的分工、找不到資料時的回應

## 轉錄錯誤與疑點
- 「公讀也有特休嗎」應為「工讀」。
- 「轉為向向量」應為「向量」。
- 「Embedding Gemma 2」：原文寫法，模型正確名稱無法從 raw 確認，wiki 不引用模型名稱。
