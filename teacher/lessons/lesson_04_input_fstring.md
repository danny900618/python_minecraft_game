# 第4堂：input() & f-string & 型別轉換

**時間：** 1 小時｜**預備知識：** 第1-3堂

---

## 今天的目標
- 用 `input()` 讓使用者輸入資料
- 用 f-string 做漂亮的輸出
- 用 `int()` `float()` `str()` 做型別轉換
- 做出第一個「互動程式」

---

## 複習（5 分鐘）

```python
# 快速猜答案
print("Ha" * 3)          # ?
print(len("creeper"))    # ?
print("ALEX".lower())    # ?
```

---

## input()：讓使用者輸入（15 分鐘）

> **類比：** 就像 Minecraft 的文字框——遊戲暫停，等你打完按 Enter 才繼續

```python
name = input("請輸入你的角色名稱：")
print("歡迎，" + name + "！")
```

**注意：** `input()` **永遠回傳字串（str）**，就算使用者輸入 `20` 也是 `"20"`！

```python
hp = input("輸入你的血量：")
print(type(hp))    # <class 'str'>  ← 不是 int！
```

❓ **問學生：** 「如果我把這個 hp 拿去做數學運算，會發生什麼事？」
→ 讓學生試試 `hp + 5`，看到 `"205"` 就懂了

---

## 型別轉換（10 分鐘）

| 函式 | 用途 | 範例 |
|------|------|------|
| `int()` | 轉成整數 | `int("20")` → `20` |
| `float()` | 轉成浮點數 | `float("3.14")` → `3.14` |
| `str()` | 轉成字串 | `str(20)` → `"20"` |
| `bool()` | 轉成布林 | `bool(1)` → `True` |

```python
hp_str = input("輸入血量：")   # 使用者輸入 "20"
hp     = int(hp_str)           # 轉成整數 20
hp    -= 5                      # 現在可以做數學了！
print("受傷後：", hp)
```

**更常見的一行寫法：**
```python
hp = int(input("輸入血量："))   # 合在一行
```

---

## f-string：格式化輸出（15 分鐘）

> **類比：** 寫信的模板——「親愛的 {名字}，你的血量是 {血量}」，一次填入變數

### 基本語法
```python
name = "Steve"
hp   = 20
print(f"玩家 {name} 的血量是 {hp}")
# 玩家 Steve 的血量是 20
```

只要在字串前面加 `f`，就可以在 `{}` 裡放變數。

### {} 裡可以放運算式
```python
hp     = 20
max_hp = 20
print(f"血量：{hp}/{max_hp} ({hp/max_hp*100:.0f}%)")
# 血量：20/20 (100%)
```

### 對比舊寫法
```python
# 舊寫法（很麻煩）
print("玩家 " + name + " 的血量是 " + str(hp))

# f-string（清楚多了）
print(f"玩家 {name} 的血量是 {hp}")
```

❓ **問學生：** 「哪種比較好讀？」→ 引導他們愛上 f-string

---

## 實作：互動角色卡（5 分鐘示範）

```python
print("=== 創建你的 Minecraft 角色 ===")

name  = input("角色名稱：")
level = int(input("等級（數字）："))
weapon = input("武器：")

print()
print(f"{'='*30}")
print(f"  名稱：{name}")
print(f"  等級：{level}")
print(f"  武器：{weapon}")
print(f"  血量：{level * 2}/{ level * 2}")   # 等級越高血量越多
print(f"{'='*30}")
```

---

## 課堂練習（5 分鐘）

**練習：** 讓使用者輸入兩個數字，印出它們的和

```python
a = int(input("輸入第一個數字："))
b = int(input("輸入第二個數字："))
print(f"{a} + {b} = {a + b}")
```

**Minecraft 版挑戰：**
```python
# 輸入挖到的礦石數量，計算總價值
diamond_count = int(input("挖到幾個鑽石？"))
diamond_price = 10   # 一個鑽石值 10 金幣

total = diamond_count * diamond_price
print(f"你挖到了 {diamond_count} 個鑽石")
print(f"總價值：{total} 金幣")
```

---

## 常見錯誤

| 錯誤 | 原因 |
|------|------|
| `int(input()) + "文字"` → TypeError | int 不能加字串，要 `str()` 轉換 |
| `int("hello")` → ValueError | 無法把非數字字串轉成 int |
| `f"{name"` → SyntaxError | f-string 的 `{}` 要關起來 |
| `int(input())` 輸入 `3.5` → ValueError | 有小數點要用 `float()` |

---

## 作業

**「Minecraft 角色產生器 v2（互動版）」**

讓使用者自己輸入：
- 角色名稱
- 目前血量（int）
- 最大血量（int）
- 等級（int）
- 武器名稱

計算並印出：
- 血量百分比（目前/最大 × 100%）
- 等級對應的攻擊力（等級 × 3）
- 漂亮的角色卡（用 f-string 和 `=` 做邊框）

**額外挑戰：** 讓使用者輸入武器的附魔等級（int），計算總傷害 = 等級×3 + 附魔等級×2

---

## 下堂課預告

「下次學最重要的概念之一：if 判斷式！讓程式學會『做決定』。」
