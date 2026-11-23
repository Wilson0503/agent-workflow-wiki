---
title: AI Agent 怎麼做事？從 Loop 到 Graph
from: deck/outline.md（人類已核准）
updated: 2026-11-23
---
# 逐頁內容（N3 產出 → R 事實審查）

> 規則：每點 ≤ 40 字、結尾標（[[slug]]）；每頁「引用」必須與大綱相同。
> `- 圖解：` 描述畫面上的圖、`- 答案：` 是測驗答案、`- 講者備註：` 給講者，三者不受字數限制，但一樣要能在 wiki 找到依據。

## S01｜封面：AI Agent 怎麼做事？
- 引用：[[overview]]
- 從 Loop 到 Graph：看懂 AI Agent 安排步驟的方法（[[overview]]）
- 問題一：Agent 到底是什麼？（[[overview]]）
- 問題二：它怎麼安排、檢查自己的步驟？（[[overview]]）
- 問題三：人類應該在哪裡出手？（[[overview]]）
- 講者備註：整份簡報的內容都來自本專案的 LLM Wiki，每頁右下角標出引用的條目。

## S02｜聊天 AI 和 Agent 差在哪？
- 引用：[[ai-agent]]
- 聊天 AI：一問一答，全程需要人在旁邊（[[ai-agent]]）
- Agent：多步驟自己執行，交代完可以離場（[[ai-agent]]）
- Agent 能讀寫檔案、建資料夾、調用工具（[[ai-agent]]）
- 產出從「一段回答」變成「完整專案成果」（[[ai-agent]]）
- 人的角色：從「打工仔」變成下指令的「老闆」（[[ai-agent]]）
- 圖解：左右兩欄對照表，左「聊天 AI」、右「AI Agent」。

## S03｜Agent = Model + Harness
- 引用：[[ai-agent]] [[harness-engineering]]
- Model：理解與生成語言的大腦（[[ai-agent]]）
- Harness：告訴 AI 如何按步驟做事的規範與流程（[[harness-engineering]]）
- 包含做事方法、檢查機制、工具介面（[[harness-engineering]]）
- 頂級模型差距已縮小，勝負關鍵在 Harness（[[harness-engineering]]）
- 圖解：大字公式「AI Agent = Model + Harness」，Model 畫成大腦方塊，Harness 畫成包住它的框。
- 講者備註：學這些名詞是為了「出外不被話術欺騙」。

## S04｜給 AI 對的資訊：Prompt 與 Context
- 引用：[[prompt-engineering]] [[context-engineering]] [[rag]] [[llm-wiki]]
- Prompt Engineering：設計怎麼問，多輪討論修正（[[prompt-engineering]]）
- Context Engineering：給足正確的背景資料（[[context-engineering]]）
- 資料不夠時 AI 只能猜，容易產生幻覺（[[context-engineering]]）
- RAG：提問時才檢索段落，知識不會累積（[[rag]]）
- LLM Wiki：先整理成互連頁面，持續更新（[[llm-wiki]]）
- 圖解：兩層堆疊，上層「怎麼問」、下層「給什麼資料」，下層再分出 RAG 與 LLM Wiki 兩個方塊。

## S05｜三種基本做事方法
- 引用：[[reflection]] [[tool-use]] [[planning]]
- Reflection：先產生結果，再自己檢查、修改（[[reflection]]）
- Tool Use：依需求選工具，例如計算機、搜尋（[[tool-use]]）
- Planning：先拆解步驟，再照計畫一步步做（[[planning]]）
- 第八週範例：07A 反思、07B 飲料店、07C 規劃（[[reflection]]、[[tool-use]]、[[planning]]）
- 圖解：三張卡片並排，各放一個圖示與一句定義。

## S06｜AI 的「思考」其實是打草稿
- 引用：[[planning]] [[prompt-engineering]]
- AI 的思考沒有神秘靈魂，本質就是打草稿（[[planning]]）
- 步驟是人用 System Prompt（事先給的規則）教的（[[planning]]、[[prompt-engineering]]）
- 教步驟的 Prompt 也別寫太長，模型可能吃不下（[[prompt-engineering]]）
- 圖解：07C 四步驟流程「確認事實 → 評估失落點 → 發想幽默切入點 → 生成正文」。
- 講者備註：07C 是「把倒楣事正向轉化」的思考生成器。

## S07｜串起來 ①：Reflection Loop
- 引用：[[reflection-loop]] [[reflection]]
- ① 作者 Agent 產生初版（[[reflection-loop]]）
- ② 審查員 Agent 依標準列出缺點與建議（[[reflection-loop]]）
- ③ 作者修訂後再送審，反覆來回（[[reflection-loop]]）
- 關鍵：要有客觀的放行條件（[[reflection-loop]]）
- 第八週是自己反思；這裡把作者和審查員分開（[[reflection]]）
- 圖解：作者 ⇄ 審查員的環狀箭頭，出口標「達到放行條件」。

## S08｜迴圈一定要有煞車
- 引用：[[stopping-conditions]] [[token-cost]]
- 最大次數：例如最多修訂 3～5 次就強制停（[[stopping-conditions]]）
- 資訊不足即停：缺原始資料就請人類補（[[stopping-conditions]]）
- 成本控管：避免無效重複修訂浪費 Token（[[stopping-conditions]]）
- Agent 每多一階段就多呼叫一次模型（[[token-cost]]）
- 例如 Groq 免費 API，容易跑到一半因額度中斷（[[token-cost]]）
- 圖解：三個煞車燈號清單。
- 講者備註：Token 可以想成模型的用量；每呼叫一次模型就消耗一次，Agent 階段越多，用量和費用就倍數成長。

## S09｜串起來 ②：Graph
- 引用：[[graph-workflow]]
- 每個節點（Node）只專注做一件事（[[graph-workflow]]）
- 例：A 寫大綱、B 檢查漏洞、C 輸出報告（[[graph-workflow]]）
- 流程不是直線：可依條件跳回前面節點（[[graph-workflow]]）
- C 發現資料遺漏 → 跳回 B，甚至退回 A（[[graph-workflow]]）
- 圖解：A → B → C 三個節點，C 有兩條虛線回跳箭頭到 B 與 A。

## S10｜Loop 還是 Graph？先從簡單的開始
- 引用：[[reflection-loop]] [[graph-workflow]] [[over-engineering]]
- Loop：固定的「產生 ⇄ 審查」來回（[[reflection-loop]]）
- Graph：依條件在不同節點間跳躍、回溯（[[graph-workflow]]）
- 簡單 Prompt 能解決，就不要用 Loop（[[over-engineering]]）
- Loop 能解決，就不要堆複雜 Graph（[[over-engineering]]）
- 流程應從人類實際做事的步驟演化而來（[[over-engineering]]）
- 圖解：三層階梯「Prompt → Loop → Graph」，旁邊小字「一層不夠才往上」。

## S11｜人類該在哪裡出手？
- 引用：[[human-checkpoint]] [[planning]]
- 大綱生成後，是人類的最佳檢查點（[[human-checkpoint]]）
- 在大綱修正，可避免之後重做 HTML 的大成本（[[human-checkpoint]]）
- 管理者只抓兩關：大綱審核、最終檢查報告（[[human-checkpoint]]）
- 動手前先提計畫，讓人審核再執行（[[planning]]）
- 圖解：時間軸「大綱 → 內容 → HTML → 成品」，越往右修正成本越高；人類圖示站在「大綱」。
- 講者備註：例子是檔案分類器，Agent 先提 5 類分類計畫，管理員確認後才搬檔案。

## S12｜實例：這份簡報是怎麼做出來的
- 引用：[[project]] [[llm-wiki]] [[graph-workflow]] [[human-checkpoint]] [[stopping-conditions]]
- 6 份原始課程資料 → 整理成 LLM Wiki（[[llm-wiki]]、[[project]]）
- 節點：Wiki → 大綱 → 逐頁內容 → HTML → 驗證（[[graph-workflow]]、[[project]]）
- 生成過程中，人類只在大綱這一關審核（[[human-checkpoint]]、[[project]]）
- 每個 Loop 最多 3 輪，超過就停下問人（[[stopping-conditions]]、[[project]]）
- 真實錯誤：Wiki 有 7 處和原始資料不符，被審查員抓到（[[project]]）
- 圖解：本專案的 Graph，標出「Wiki 事實抽查」「簡報事實審查」兩個審查員節點與回跳箭頭。
- 講者備註：7 處不符中有 5 處是原始資料根本沒講的事；有 4 處出在「常見誤區」段，因為模板要求至少寫 1 點，作者就自己補了常識。後來改成「沒有就寫來源未提及」，並把事實抽查提前到 Wiki 這一層。最終檢查報告就是 docs/run-log.md。

## S13｜把規則寫下來：手冊、Skill、Git
- 引用：[[agents-md]] [[agent-skills]] [[git-version-control]] [[coding-agent-vs-work-agent]]
- 員工手冊：成果、約束、驗收標準、先計畫（[[agents-md]]）
- Skill：把好流程打包，風格不再隨機波動（[[agent-skills]]）
- Git：AI 把檔案改壞了，可以復原（[[git-version-control]]）
- Coding Agent 綁定專案資料夾，能讀寫檔案、整合 Git（[[coding-agent-vs-work-agent]]）
- 圖解：三張卡片（手冊、Skill、Git），底下一行「Claude Code／Codex／Antigravity」。

## S14｜小測驗
- 引用：[[ai-agent]] [[stopping-conditions]] [[human-checkpoint]]
- Q1：AI Agent 的公式是什麼？（[[ai-agent]]）
- 答案：AI Agent = AI Model + Harness。
- Q2：設計 Loop 時至少要有哪兩種設計？（[[stopping-conditions]]）
- 答案：客觀的放行條件，以及煞車機制（如最多 3～5 次、資訊不足即停）。
- Q3：用 Graph 做簡報，人類最該在哪一步檢查？（[[human-checkpoint]]）
- 答案：大綱生成後。在這裡修正，可以避免之後重做 HTML。

## S15｜小結與參考資料
- 引用：[[overview]] [[s1-rag-demo]] [[s2-agent-demo-notes]] [[s3-three-agent-patterns]] [[s4-harness-and-agents-md]] [[s5-karpathy-llm-wiki]] [[s6-loop-and-graph]]
- Agent = Model + Harness，關鍵在怎麼安排步驟（[[overview]]）
- Loop 要有放行條件和煞車；需要跳回才用 Graph（[[s6-loop-and-graph]]）
- 人類在大綱出手，越早檢查越便宜（[[s6-loop-and-graph]]）
- 圖解：六份來源清單（s1～s6）＋「讀完整 Wiki」按鈕。
