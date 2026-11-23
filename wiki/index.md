# 知識庫總目錄（wiki/index.md）

> AI 回答問題或做簡報前，先讀這份目錄再進入條目。格式：`- [[頁面代號]] — 一句話摘要`

## 總覽
- [[overview]] — 一頁讀懂：Agent = Model + Harness，以及 Loop / Graph 的主線

## 來源（6 份課程資料）
- [[s1-rag-demo]] — 第七週 RAG 作業範例講解（R01 向量庫、R02 對話機器人）
- [[s2-agent-demo-notes]] — 第八週 07C Planning 示範、Token 成本、思考＝打草稿
- [[s3-three-agent-patterns]] — 第八週作業：Reflection / Tool Use / Planning 定義
- [[s4-harness-and-agents-md]] — 第九週：Agent 範式轉移、Harness、員工手冊、Skill
- [[s5-karpathy-llm-wiki]] — Karpathy LLM Wiki：三層架構、Ingest / Query / Lint
- [[s6-loop-and-graph]] — 第十週：Reflection Loop、Graph、簡報四節點流程

## 概念

### 基礎
- [[ai-agent]] — 多步驟自主執行、會用工具的 AI，Model + Harness
- [[harness-engineering]] — 告訴 AI 怎麼按步驟做事的規範與流程
- [[prompt-engineering]] — 設計怎麼問、多輪修正
- [[context-engineering]] — 給 AI 足夠且正確的背景資料，避免幻覺
- [[rag]] — 先檢索段落再回答；知識不累積、像黑盒子
- [[llm-wiki]] — LLM 維護的互連 Markdown 知識庫

### 三種做事方法
- [[reflection]] — 先產生、再檢查、再修改
- [[tool-use]] — 依需求選擇並呼叫工具
- [[planning]] — 先拆步驟、打草稿再執行

### 流程控制
- [[reflection-loop]] — 作者 ⇄ 審查員反覆修訂
- [[graph-workflow]] — 節點＋條件跳躍的流程
- [[stopping-conditions]] — 次數上限、資訊不足即停、成本控管
- [[human-checkpoint]] — 大綱階段是人類最佳檢查點
- [[token-cost]] — 多階段呼叫讓用量倍增
- [[over-engineering]] — Prompt → Loop → Graph，能簡單就簡單

### 專案化
- [[agents-md]] — 員工手冊：成果、約束、驗收、先計畫
- [[agent-skills]] — 把好流程打包成可重用 SOP
- [[coding-agent-vs-work-agent]] — 對話視窗 vs 操作專案資料夾
- [[git-version-control]] — 本機版本控管，AI 改壞可復原

## 待確認
- s4 的「Graphite Engineering」疑為轉錄錯誤，未收錄，需人類確認原意。
