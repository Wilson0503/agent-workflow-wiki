---
title: AI Agent 怎麼做事？從 Loop 到 Graph
audience: 沒學過 AI Agent 的大學生（知道 ChatGPT，但沒聽過 Harness、Loop、Graph）
goal: 看完能說出 Agent = Model + Harness、分辨 Loop 與 Graph、知道為什麼要煞車和人類檢查點
style: 科技深色風、演講演示型（每頁一個重點）
must_cover: all-concepts
updated: 2026-11-23
---
# 大綱（N2 產出 → 人類檢查點 H 審這份）

> 每張投影片都要列「引用」：只能引用 `wiki/` 裡存在的頁面。`[[project]]` 代表本專案自己的流程文件（docs/workflow.md），只用在第 12 張。

## S01｜封面：AI Agent 怎麼做事？
- 型式：cover
- 目標：引起興趣，交代這份簡報要回答的三個問題
- 引用：[[overview]]
- 內容方向：副標「從 Loop 到 Graph」；三個問題：Agent 是什麼？它怎麼安排步驟？人該在哪裡出手？

## S02｜聊天 AI 和 Agent 差在哪？
- 型式：compare（兩欄對照表）
- 目標：建立「Agent 不是更聰明的聊天框」的直覺
- 引用：[[ai-agent]]
- 內容方向：一問一答 vs 多步驟自主執行；只能生文字 vs 能讀寫檔案、用工具；人從「打工仔」變「老闆」

## S03｜Agent = Model + Harness
- 型式：formula（公式圖解）
- 目標：記住整份簡報最重要的公式
- 引用：[[ai-agent]] [[harness-engineering]]
- 內容方向：Model＝大腦；Harness＝按步驟做事的規範、檢查機制、工具介面；模型差距縮小，關鍵在 Harness

## S04｜給 AI 對的資訊：Prompt 與 Context
- 型式：two-layer（兩層堆疊）
- 目標：分清楚「問得好」和「給得夠」
- 引用：[[prompt-engineering]] [[context-engineering]] [[rag]] [[llm-wiki]]
- 內容方向：Prompt＝怎麼問；Context＝給足正確背景資料以免幻覺；兩種做法 RAG、LLM Wiki 的一句話差異

## S05｜三種基本做事方法
- 型式：cards ×3
- 目標：認識 Reflection、Tool Use、Planning
- 引用：[[reflection]] [[tool-use]] [[planning]]
- 內容方向：各一句定義＋第八週範例 07A / 07B / 07C

## S06｜AI 的「思考」其實是打草稿
- 型式：flow（四步驟）
- 目標：破除「AI 有意識在想」的迷思，引出「步驟是人設計的」
- 引用：[[planning]] [[prompt-engineering]]
- 內容方向：07C 打草稿四步驟；步驟由 System Prompt 教；AI 寫的長 Prompt 反而可能壞掉

## S07｜串起來 ①：Reflection Loop
- 型式：loop 圖（作者 ⇄ 審查員）
- 目標：理解固定來回的迴圈
- 引用：[[reflection-loop]] [[reflection]]
- 內容方向：三步驟；客觀放行條件；與第八週單一 Agent 反思的差別

## S08｜迴圈一定要有煞車
- 型式：checklist
- 目標：知道 Loop 的三種停止條件與成本
- 引用：[[stopping-conditions]] [[token-cost]]
- 內容方向：最多 3～5 次、資訊不足即停、成本控管；Agent 多階段呼叫讓 Token 倍增

## S09｜串起來 ②：Graph
- 型式：graph 圖（節點＋回跳箭頭）
- 目標：理解節點與條件跳躍
- 引用：[[graph-workflow]]
- 內容方向：每個節點只做一件事；條件不符就跳回前面節點；s6 的 A 大綱 → B 檢查 → C 報告例子

## S10｜Loop 還是 Graph？先從簡單的開始
- 型式：compare 表＋階梯
- 目標：會選擇，且知道不要過度工程化
- 引用：[[reflection-loop]] [[graph-workflow]] [[over-engineering]]
- 內容方向：固定來回 vs 依條件跳躍；Prompt → Loop → Graph 一層不夠才往下

## S11｜人類該在哪裡出手？
- 型式：timeline（越早修越便宜）
- 目標：理解人類檢查點的位置與理由
- 引用：[[human-checkpoint]] [[planning]]
- 內容方向：大綱階段是最佳檢查點；管理者只抓「大綱審核」與「最終報告」；先計畫後執行（檔案分類器例子）

## S12｜實例：這份簡報是怎麼做出來的
- 型式：graph 圖（本專案流程）
- 目標：把前面概念套到一個真實例子
- 引用：[[project]] [[llm-wiki]] [[graph-workflow]] [[human-checkpoint]] [[stopping-conditions]]
- 內容方向：raw → wiki → 大綱 → 人類檢查 → 逐頁內容 ⇄ 事實審查 → HTML → 驗證；每個 Loop 最多 3 輪；附一個實際執行時被抓到的錯誤

## S13｜把規則寫下來：手冊、Skill、Git
- 型式：cards ×3＋一行工具說明
- 目標：知道怎麼讓 Agent 每次都照同一套做
- 引用：[[agents-md]] [[agent-skills]] [[git-version-control]] [[coding-agent-vs-work-agent]]
- 內容方向：手冊四要素；Skill 讓風格不亂飄；Git 改壞能復原；這些都要靠能操作資料夾的 Coding Agent

## S14｜小測驗
- 型式：quiz ×3（點擊翻開答案）
- 目標：自我檢查
- 引用：[[ai-agent]] [[stopping-conditions]] [[human-checkpoint]]
- 內容方向：① Agent 的公式？② Loop 至少要有哪兩種設計？（放行條件＋煞車）③ 做簡報時人類最該在哪一步檢查？

## S15｜小結與參考資料
- 型式：summary
- 目標：帶走三句話，知道去哪裡讀更多
- 引用：[[overview]] [[s1-rag-demo]] [[s2-agent-demo-notes]] [[s3-three-agent-patterns]] [[s4-harness-and-agents-md]] [[s5-karpathy-llm-wiki]] [[s6-loop-and-graph]]
- 內容方向：三個 takeaway；連到 wiki.html 與六份來源
