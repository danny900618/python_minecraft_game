# Python 家教專案 — AI 閱讀用上下文

## 專案背景
這是一個 Python 家教課程，學生是 Minecraft 愛好者、Windows 電腦、完全初學者。
所有題目、比喻、作業都以 Minecraft 為主題。每堂課 1 小時，共 12 堂。

---

## 檔案結構

```
python_class/
├── minecraft_quiz.py     # 遊戲主程式（學生執行這個）
├── question_bank.py      # 題庫模組（所有題目在這裡）
├── game_config.json      # 難度設定（老師調整）
├── 開始遊戲.bat           # 學生雙擊啟動遊戲（Windows）
├── player_save.json      # 自動生成，儲存學生進度（gitignore）
├── teacher_codes.md      # 老師專用：解鎖碼對照表（gitignore）
├── CLAUDE.md             # 本檔案（gitignore）
├── lessons/              # 12 堂課教材 .md（gitignore）
│   ├── lesson_01_intro.md
│   ├── lesson_02_variables.md
│   ├── lesson_03_strings.md
│   ├── lesson_04_input_fstring.md
│   ├── lesson_05_if.md
│   ├── lesson_06_logic.md
│   ├── lesson_07_for.md
│   ├── lesson_08_while.md
│   ├── lesson_09_list.md
│   ├── lesson_10_function.md
│   ├── lesson_11_mixed.md
│   └── lesson_12_project.md
├── Python課綱_Minecraft版.xlsx  # Excel 課綱（gitignore）
└── create_curriculum.py         # 重新產生 Excel 用（gitignore）
```

---

## 遊戲架構

### 關卡章節（question_bank.py 的 CHAPTER_ORDER）
```
variables → io → if → for → while → list → function → mixed
```

### 解鎖機制
- 第一關 `variables` 預設解鎖
- 其他關卡需要老師給學生「解鎖碼」
- 學生在遊戲主選單按 `[U]` 輸入代碼
- 解鎖碼在 `minecraft_quiz.py` 以 **SHA-256 hash** 儲存（無法從程式碼反推）
- 解鎖狀態存在 `player_save.json` 的 `unlocked_chapters` 欄位

### 解鎖碼對照（明碼，不推 git）
| 上完後 | 代碼 | 解鎖章節 |
|--------|------|---------|
| 第4堂  | `STONE04`  | io |
| 第6堂  | `IRON06`   | if |
| 第7堂  | `GOLD07`   | for |
| 第8堂  | `LAPIS08`  | while |
| 第9堂  | `ENDER09`  | list |
| 第10堂 | `NETHER10` | function |
| 第12堂 | `DRAGON12` | mixed |

### 生命值系統
- 每關預設 3 條命（`game_config.json` 可調）
- 答錯扣 1 條命
- 歸零後重新隨機抽題再挑戰（不是重複同一組題目）
- 答對得 1 顆鑽石，存入 `player_save.json`

---

## 題庫結構（question_bank.py）

每個章節格式：
```python
"chapter_key": {
    "title"     : "顯示名稱",
    "color_name": "yellow",   # green/yellow/red/cyan/blue/purple
    "questions" : [
        {
            "q"      : "題目文字（支援 \\n 換行）",
            "opts"   : ["選項1", "選項2", "選項3", "選項4"],
            "ans"    : 2,        # 1~4，正確答案的編號
            "explain": "解說文字",
            "diff"   : 1,        # 1=簡單 2=普通 3=挑戰
        },
    ]
}
```

目前每章節有 12 題，每次遊玩隨機抽 5 題（`questions_per_chapter` 可調）。

---

## 新增內容的方式

### 新增題目
在 `question_bank.py` 對應章節的 `questions` 列表加入新 dict，格式如上。

### 新增章節（如第13堂以後）
1. `question_bank.py`：在 `CHAPTERS` 加入新 key，在 `CHAPTER_ORDER` 列表末尾加入該 key
2. `minecraft_quiz.py`：在 `_build_unlock_table()` 函式的 `_raw` 列表加入新代碼：
   ```python
   ("新代碼", ["新chapter_key"], "關卡顯示名稱"),
   ```
3. `teacher_codes.md`：記錄新代碼

### 調整難度
編輯 `game_config.json`：
```json
{
  "questions_per_chapter": 5,    // 每關出幾題
  "max_lives": 2,                 // 每次挑戰幾條命
  "diamonds_per_correct": 1,
  "show_explain_on_wrong": true  // 答錯是否顯示解說
}
```

### 重置學生進度
刪除 `player_save.json`，遊戲重新執行時自動建立新的。

---

## 發佈流程（GitHub）

老師推送：
```bash
git add .
git commit -m "說明"
git push
```

學生更新：
1. GitHub → Download ZIP → 解壓縮成新資料夾
2. 把舊資料夾的 `player_save.json` 複製到新資料夾
3. 老師另外傳解鎖碼（LINE）
4. 學生在遊戲按 `[U]` 輸入碼

---

## 課程大綱（12 堂 × 1 小時）

| 堂次 | 主題 | 對應遊戲章節 |
|------|------|------------|
| 第1堂 | 認識 Python & print() | — |
| 第2堂 | 變數 & 資料型別 | variables |
| 第3堂 | 字串操作 | — |
| 第4堂 | input() & f-string & 型別轉換 | io |
| 第5堂 | if / elif / else | — |
| 第6堂 | 邏輯運算子 & 巢狀 if | if |
| 第7堂 | for 迴圈 | for |
| 第8堂 | while 迴圈 | while |
| 第9堂 | 串列 List | list |
| 第10堂 | 函式 Function | function |
| 第11堂 | 綜合練習 | — |
| 第12堂 | 期末專案：文字冒險 | mixed |

---

## 後續 12 堂（第13~24堂）規劃方向
以實用 Python 工程師技能為主，方向已確認：
字典 → 進階函式 → List/Dict Comprehension → 常用模組 →
例外處理 → 檔案讀寫 → CSV 處理 → pip/venv →
Class 基礎 → requests/API → 自動化腳本 → 實戰專案
