---
title: 檢索增強生成（RAG）
slug: rag
sources: [s1, s5, s4, s6]
updated: 2026-11-23
---
# 檢索增強生成（RAG）

> 先從資料庫找出相關段落，再讓 LLM 根據段落回答。

## 重點
- 流程：資料切塊 → 內文做 Embedding 轉向量 → 存進向量資料庫（FAISS）→ 提問時檢索 → 把段落和問題組合成 Prompt 交給 LLM（s1）。
- 打包向量庫前，要先用測試問題驗證檢索結果是否準確（s1）。
- 缺點一：每次提問都從原始文件重新拼湊，知識沒有累積（s5）。
- 缺點二：向量檢索像黑盒子，找對找錯不容易看出來（s4）。
- 中等規模的知識庫，用 index 檔就夠，不一定需要 embedding RAG（s5）。
- 第十週把 RAG 和 LLM Wiki 並列為 Context Engineering 的常見做法（s6）。

## 例子
- 第七週「勞動部工讀生權益」示範：R01 建向量庫、R02 做 Gradio 對話機器人（s1）。

## 常見誤區
- 跳過打包前的檢索驗證，沒確認向量搜尋抓到的文本與 Metadata 是否準確（s1）。

## 相關概念
- [[context-engineering]] — RAG 是提供 context 的一種方式
- [[llm-wiki]] — 不需要向量、可解釋性更高的替代方案
