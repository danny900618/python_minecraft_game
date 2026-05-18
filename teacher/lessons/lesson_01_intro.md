# 第1堂：認識 Python & 第一個程式

**時間：** 1 小時｜**對象：** 完全初學者

---

## 今天的目標
- 知道 Python 是什麼、能做什麼
- 安裝 Python 和 VS Code（或 IDLE）
- 能寫出第一個 `print()` 程式
- 認識 `#` 註解

---

## 開場暖身（5 分鐘）

問學生：「你玩 Minecraft 的時候有沒有想過，那些怪物 AI、自動農場、甚至 Mod，都是用程式寫的？」

> **類比：** 程式就像 Minecraft 的指令方塊（Command Block）。你寫一行指令，電腦就照著做。Python 就是我們下指令用的語言。

---

## 安裝環境（15 分鐘）

### Step 1：安裝 Python
1. 到 python.org 下載最新版（Windows）
2. 安裝時 **一定要勾選 "Add Python to PATH"**
3. 打開 CMD 或 PowerShell，輸入：
   ```
   python --version
   ```
   看到版本號就成功了！

### Step 2：安裝 VS Code（推薦）
1. 到 code.visualstudio.com 下載
2. 安裝 Python 擴充套件（Extensions → 搜尋 Python）
3. 新建一個 `.py` 檔案開始寫程式

> 如果時間不夠，也可以直接用 **IDLE**（Python 安裝時附帶）

---

## 概念講解（20 分鐘）

### 什麼是 print()？

`print()` 就像 Minecraft 聊天框 `/say` 指令，叫電腦「說話」（印出文字）。

```python
print("Hello, Minecraft!")
print("我是 Steve！")
print("今天開始學 Python 🐍")
```

**現場示範：** 一行一行輸入，按執行，讓學生看到輸出。

---

### 字串（String）

用引號包起來的文字，就叫「字串」。

```python
print("這是雙引號字串")
print('這是單引號字串')
```

> **類比：** 字串就像 Minecraft 告示牌上的文字，被方框圍起來。

❓ **問學生：** 「如果我忘記加引號，結果會怎樣？」  
→ 讓學生試試 `print(Hello)`，看錯誤訊息。

---

### 註解（Comment）

`#` 後面的文字，Python 會直接忽略。用來寫給人看的說明。

```python
# 這是我的第一個 Python 程式
print("Steve 的冒險開始！")  # 這行會印出文字

# print("這行被註解掉，不會執行")
```

> **類比：** 就像 Minecraft 的地圖筆記，給自己看的提醒，不影響遊戲。

---

### print() 的多個參數

```python
print("血量：", 20)           # 用逗號分開，會自動加空格
print("玩家", "Steve", "上線") # 可以放很多個
```

---

## 課堂練習（15 分鐘）

一起完成，老師帶著寫：

**練習 1（超簡單）：**  
印出你的 Minecraft 角色名稱和喜歡的武器
```python
# 參考答案
print("角色名稱：Steve")
print("最愛武器：鑽石劍")
print("目前等級：1")
```

**練習 2：**  
印出一個 Minecraft 角色卡（用多行 print）
```
====================
  角色：Steve
  等級：10
  血量：20
====================
```
```python
# 參考答案
print("====================")
print("  角色：Steve")
print("  等級：10")
print("  血量：20")
print("====================")
```

**練習 3（挑戰）：**  
試著讓印出來的文字像一個 Minecraft 血條
```python
print("HP: [**********] 20/20")
print("HP: [*****     ] 10/20")
```

---

## 常見錯誤

| 錯誤 | 原因 | 修正 |
|------|------|------|
| `print(Hello)` → NameError | 忘了加引號 | `print("Hello")` |
| `Print("Hi")` → NameError | 大小寫錯誤 | `print("Hi")` |
| `print("Hi"` → SyntaxError | 忘了關括號 | `print("Hi")` |
| 中文出現亂碼 | 檔案編碼問題 | 確認存成 UTF-8 |

---

## 作業

**「Minecraft 自我介紹」**

寫一個程式，用 `print()` 印出你的 Minecraft 角色介紹，至少包含：
- 角色名稱
- 最愛的 Minecraft 活動（挖礦/蓋房/打怪）
- 最想要的武器
- 一句話目標

範例輸出：
```
=== 我的 Minecraft 角色 ===
名稱  ：Alex
活動  ：喜歡挖礦和探險
武器  ：鑽石劍 + 附魔弓
目標  ：打敗末影龍！
==========================
```

---

## 下堂課預告

「下次我們會學習『變數』——讓電腦記住東西！就像 Minecraft 的背包格子。」
