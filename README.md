# ⛏️ Minecraft Python 學習遊戲

Python 初學者課程配套遊戲，以 Minecraft 為主題。

---

## 📁 資料夾結構

```
python_minecraft_game/
│
├── 🎮 學生使用的檔案（給學生這幾個）
│   ├── minecraft_quiz.py     遊戲主程式
│   ├── question_bank.py      題庫
│   ├── game_config.json      難度設定
│   └── 開始遊戲.bat          雙擊啟動（Windows）
│
└── 📚 teacher/               老師專用
    ├── lessons/              12 堂課講義（.md）
    ├── teacher_codes.md      解鎖碼對照表
    ├── Python課綱_Minecraft版.xlsx  課綱 Excel
    └── create_curriculum.py  重新產生 Excel 的腳本
```

---

## 🚀 學生使用方式

1. 下載這個 repo（右上角 Code → Download ZIP）
2. 解壓縮
3. 把 `minecraft_quiz.py`、`question_bank.py`、`game_config.json`、`開始遊戲.bat` 放在同一個資料夾
4. 雙擊 `開始遊戲.bat`

> 需要先安裝 Python：https://www.python.org/downloads/（記得勾選 Add Python to PATH）

---

## 🔓 關卡解鎖

第一關預設解鎖。後續關卡由老師上課後傳解鎖碼，在遊戲主選單按 **[U]** 輸入。

---

## ⚙️ 難度調整（老師用）

編輯 `game_config.json`：

| 設定 | 預設 | 說明 |
|------|------|------|
| `questions_per_chapter` | 5 | 每關出幾題 |
| `max_lives` | 2 | 每次挑戰幾條命 |
| `show_explain_on_wrong` | true | 答錯後顯示解說 |
