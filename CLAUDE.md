# CLAUDE.md — AI Agent 工作流程 LLM Wiki（員工手冊）

> 本文件是專案的**唯一規則來源**。任何 AI（Claude Code、Codex、Gemini / Antigravity…）動手前必須讀完。
> `AGENTS.md` 只是入口，衝突時以本文件為準。

---

## 0. 一句話說明

把「生成式 AI」課堂上講過的 Agent 相關內容（第 7～10 週課程影片整理）**編譯**成一套主題式 LLM Wiki，
再以 Wiki 為**唯一知識來源**，透過一條有檢查點的 Graph 流程，產出給初學者看的教學 HTML 簡報
**「AI Agent 怎麼做事？從 Loop 到 Graph」**。

- 人類（管理者）：挑資料、審大綱（人類檢查點）、驗收。
- AI（員工）：ingest、寫 wiki、擬大綱、寫逐頁內容、渲染 HTML、跑所有檢查、寫紀錄。

---

## 1. 三層架構（Karpathy LLM Wiki）

```
raw/  ──(N1 ingest)──▶  wiki/  ──(N2–N4 deck graph)──▶  deck/index.html
原始資料（唯讀）           知識庫（AI 維護）              教學簡報（GitHub Pages）
```

| 層 | 路徑 | 誰寫 | 規則 |
|---|---|---|---|
| 原始資料 | `raw/` | 人類 | **AI 不可修改、改名、刪除**。`docs/raw.sha256` 記錄雜湊，`check_wiki.py` 會驗證。 |
| 知識庫 | `wiki/` | AI | 每句話都要能追溯回 `raw/`（frontmatter `sources`）。 |
| 簡報 | `deck/` | AI | 只能用 `wiki/` 裡有的內容；每張投影片都要標出引用的 wiki 條目。 |

---

## 2. 資料夾結構

```
agent-workflow-wiki/
├── CLAUDE.md / AGENTS.md / README.md
├── index.html                 ← 首頁：簡報、Wiki、流程說明的入口
├── wiki.html                  ← 由 scripts/build_wiki_html.py 產生（禁止手改）
├── raw/sN_wNN_<名稱>.txt      ← 原始資料（唯讀）
├── wiki/
│   ├── index.md               ← 總目錄（每次 ingest 必更新）
│   ├── log.md                 ← 只能追加的時間序紀錄
│   ├── overview.md            ← 主題總覽（綜合所有來源）
│   ├── sources/<slug>.md      ← 每份 raw 一頁來源摘要
│   └── concepts/<slug>.md     ← 一個概念一頁
├── deck/
│   ├── outline.md             ← N2 產出：大綱（人類檢查點審這份）
│   ├── content.md             ← N3 產出：逐頁內容＋引用
│   └── index.html             ← N4 產出：教學簡報
├── assets/css/deck.css        ← 全站唯一樣式表
├── assets/js/deck.js          ← 簡報翻頁、測驗互動
├── templates/                 ← concept.md / source.md 模板
├── scripts/
│   ├── wikilib.py             ← 共用解析
│   ├── check_wiki.py          ← C1：Wiki 檢查
│   ├── check_deck.py          ← C2 / C4：大綱、內容、HTML 檢查（--stage outline|content|html）
│   ├── render_check.py        ← C4：用無頭瀏覽器截圖、偵測文字溢出
│   └── build_wiki_html.py     ← 產生 wiki.html
└── docs/
    ├── workflow.md            ← loop / graph 設計說明（流程圖）
    ├── run-log.md             ← 實際執行與檢查紀錄（只能追加）
    ├── reflection.md          ← 反思
    └── screenshots/           ← render_check 截圖
```

---

## 3. 命名規則

| 東西 | 規則 | 範例 |
|---|---|---|
| raw 檔 | `sN_wNN_<中文名>.txt`，N 為來源編號 | `s6_w10_Loop與Graph課程說明.txt` |
| 來源摘要 | `wiki/sources/sN-<english-kebab>.md` | `s6-loop-and-graph.md` |
| 概念 | `wiki/concepts/<english-kebab>.md` | `reflection-loop.md` |

- slug 一旦建立不可改名（`wiki.html#slug` 與簡報引用依賴它）。
- 新增概念前先查 `wiki/index.md`，已存在就更新。

---

## 4. Wiki 頁面格式

### 4.1 概念條目（照 `templates/concept.md`）

```markdown
---
title: 中文名稱（English）
slug: reflection-loop
sources: [s6, s3]
updated: YYYY-MM-DD
---
# 中文名稱（English）

> 一句話定義（40 字內、白話、初學者看得懂）。

## 重點
- 3～6 點；每點結尾標來源 `（s6）`

## 例子
- 課堂上的實際例子（沒有就寫「來源未提供例子」，不可自己編）

## 常見誤區
- 只能寫 raw 明確提到的誤區；raw 沒有就寫「來源未提及。」（不可自己推論補常識）

## 相關概念
- [[其他-slug]] — 為什麼相關
```

### 4.2 來源摘要（照 `templates/source.md`）

frontmatter：`title`、`slug`、`raw`（raw 檔路徑）、`week`、`updated`。
內文：`## 這份資料在講什麼`、`## 重點摘錄`、`## 產生／更新的概念`（列 `[[slug]]`）、`## 轉錄錯誤與疑點`。

### 4.3 連結與矛盾

- 內部連結一律 `[[slug]]`（Obsidian 相容）。
- 每個概念至少 1 個「相關概念」，且至少被 1 個來源摘要引用（不可有孤兒）。
- 課程整理是語音轉錄，會有錯字（例如把 Loop 寫成 LOP、Graph 寫成 Grave）。**wiki 用正確名稱，但在來源摘要的「轉錄錯誤與疑點」記錄原文**，不可默默改掉。
- 來源互相矛盾時，加 `> ⚠️ 矛盾：...` 並註明兩邊來源。
- **只能使用 raw 檔的「內容」**：檔名、資料夾裡的其他檔案、AI 自己的常識都不算來源。

### 4.4 `index.md` / `log.md`

- `index.md`：分「總覽」「來源」「概念」三區，每行 `- [[slug]] — 一句話摘要`。
- `log.md` 只能追加：`## [YYYY-MM-DD] <動作> | <說明>`，動作限 `setup`、`ingest`、`lint`、`query`、`publish`。

---

## 5. 簡報生成 Graph（AI 必須照這個流程做）

完整說明與流程圖見 `docs/workflow.md`。摘要：

```
N0 取得資料 → N1 Ingest → C1 Wiki 檢查 ──fail──▶ N1
                              │pass
                              ▼
                        C1b Wiki 事實抽查（審查員 Agent 比對 wiki ⇄ raw）──fail──▶ N1
                              │pass
                              ▼
                N2 擬大綱 → C2 大綱檢查 ──fail(格式/引用)──▶ N2
                              │            └─fail(wiki 缺內容)──▶ N1
                              ▼pass
                        H 人類檢查點 ──要修改──▶ N2
                              │OK
                              ▼
                N3 逐頁內容 ⇄ R 事實審查 Loop（審查員 Agent，最多 3 輪）
                              │pass        └─wiki 沒有這件事──▶ N1（raw 也沒有→停下問人類）
                              ▼
                N4 HTML 渲染 → C4 驗證（結構＋截圖）
                              │            ├─fail(版面/連結)──▶ N4
                              │            └─fail(內容對不上)──▶ N3
                              ▼pass
                        N5 發佈（首頁、log、git commit）
```

### 5.1 每個節點的輸入 / 輸出 / 通過條件

| 節點 | 輸入 | 輸出 | 通過條件 |
|---|---|---|---|
| N0 取得資料 | 人類指定的檔案 | `raw/`、`docs/raw.sha256` | 檔案齊全 |
| N1 Ingest | `raw/` | `wiki/` | — |
| C1 Wiki 檢查 | `wiki/` | 錯誤清單 | `python scripts/check_wiki.py` 印出 `WIKI CHECK PASSED` |
| C1b Wiki 事實抽查 | `wiki/`＋`raw/` | 審查報告 | 審查員回 `VERDICT: PASS`（另一個 Agent；檢查不支持／曲解／標錯來源／外部知識） |
| N2 擬大綱 | `wiki/index.md` → 條目 | `deck/outline.md` | — |
| C2 大綱檢查 | `outline.md` | 錯誤清單 | `check_deck.py --stage outline` 通過 |
| H 人類檢查點 | `outline.md` | 人類回覆 | 人類說 OK |
| N3 逐頁內容 | `outline.md`＋引用的條目 | `deck/content.md` | `check_deck.py --stage content` 通過 |
| R 事實審查 | `content.md`＋引用的條目 | 審查報告 | 審查員回 `PASS`（**審查員必須是另一個 Agent，不能自己審自己**） |
| N4 渲染 | `content.md` | `deck/index.html` | — |
| C4 驗證 | `deck/index.html` | 錯誤清單＋截圖 | `check_deck.py --stage html` 與 `render_check.py` 都通過 |
| N5 發佈 | 全部 | `index.html`、`wiki.html`、log、commit | `python scripts/build_wiki_html.py` 後所有檢查重跑通過 |

### 5.2 煞車（停止條件）

1. 任何一個 Loop（C1↔N1、C1b↔N1、C2↔N2、N3↔R、C4↔N4）**最多 3 輪**，第 3 輪仍失敗就停下，把錯誤回報給人類。
2. 審查發現 wiki 沒有、raw 也沒有的資訊 → **不准補寫**，停下來請人類補資料。
3. 同一個錯誤連續出現 2 次 → 不要再原地重試，檢查是不是上游節點的問題（往前跳）。

### 5.3 紀錄

每跑完一個節點或檢查，在 `docs/run-log.md` 追加一行：時間、節點、結果（PASS / FAIL＋原因）、下一步跳到哪裡。**失敗也要記，不能只記成功。**

---

## 6. 簡報規格（科技深色風）

- 只用 `assets/css/deck.css`、`assets/js/deck.js`；HTML 內不可寫 `<style>` 或 `style=""`。
- 字體：`Noto Sans TC`（內文）、`JetBrains Mono`（程式感標籤），Google Fonts 載入。
- 色票只能用 CSS `:root` 已定義的變數，不可新增色碼。
- 每張投影片 `<section class="slide" data-cites="slug-a slug-b">`，`data-cites` 必須與 `content.md` 該頁的引用一致；頁尾顯示引用 chip，連到 `../wiki.html#slug`。
- 每張投影片條列 ≤ 5 點、每點 ≤ 40 字；圖解用 HTML/CSS（`.flow`、`.loop`、`.graph`）繪製，不用外部圖片。
- 必須支援：← → 翻頁、頁碼、講義模式（全部展開）、手機寬度可讀。
- 所有連結用**相對路徑**；根目錄放 `.nojekyll`。

---

## 7. 禁止事項

1. ❌ 修改 `raw/`。
2. ❌ 在 wiki 或簡報放入 raw 裡沒有的知識（不要自己補充業界資料）。
3. ❌ 跳過人類檢查點 H 直接做 N3。
4. ❌ 由寫內容的同一個 Agent 自己做事實審查。
5. ❌ 手改 `wiki.html`；改 `run-log.md`、`log.md` 的舊紀錄。
6. ❌ 放入 API 金鑰、密碼、他人個資。

---

## 8. 完成標準

- [ ] `python scripts/check_wiki.py` → `WIKI CHECK PASSED`
- [ ] `python scripts/check_deck.py --stage html` → `DECK CHECK PASSED`
- [ ] `python scripts/render_check.py` → `RENDER CHECK PASSED`
- [ ] 人類檢查點與事實審查都有記錄在 `docs/run-log.md`
- [ ] `index.html` 能連到簡報、`wiki.html`、`docs/workflow.md`
