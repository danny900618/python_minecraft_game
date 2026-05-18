# 第7堂：for 迴圈

**時間：** 1 小時｜**預備知識：** 第1-6堂

---

## 今天的目標
- 理解「迴圈」的概念
- 用 `for` 和 `range()` 重複執行程式碼
- 用 `break` 和 `continue` 控制迴圈
- 做出挖礦計數器、星號圖案等

---

## 複習（5 分鐘）

```python
# 猜結果
hp = 7
if hp >= 10 and not False:
    print("A")
elif hp >= 5 or True:
    print("B")
else:
    print("C")
# 答案？
```

---

## 為什麼需要迴圈？（5 分鐘）

**沒有迴圈的版本（很痛苦）：**
```python
print("挖第 1 個方塊")
print("挖第 2 個方塊")
print("挖第 3 個方塊")
# ... 要挖 100 個呢？
```

**有迴圈的版本：**
```python
for i in range(100):
    print(f"挖第 {i+1} 個方塊")
```

> **類比：** 就像 Minecraft 的自動農場——設定好規則，它就一直重複幫你收割

---

## for 基本語法（10 分鐘）

```python
for i in range(5):
    print(i)
# 印出 0, 1, 2, 3, 4
```

**語法說明：**
- `i` 是迴圈變數（每次迴圈會自動更新）
- `range(5)` 產生 0, 1, 2, 3, 4（不含 5）
- 縮排的程式碼每次都會執行

### range() 的三種寫法

```python
range(5)          # 0, 1, 2, 3, 4
range(1, 6)       # 1, 2, 3, 4, 5   （start, stop）
range(0, 20, 5)   # 0, 5, 10, 15    （start, stop, step）
range(10, 0, -1)  # 10, 9, 8...1    （倒數！）
```

**現場示範：**
```python
# 挖礦計數器
for layer in range(1, 11):
    print(f"正在挖第 {layer} 層...")
print("挖完了！")
```

---

## for 迴圈搭配 if（10 分鐘）

```python
# 找到鑽石層（Y=12）
for y in range(1, 20):
    if y == 12:
        print(f"Y={y} 是鑽石層！★")
    else:
        print(f"Y={y}：普通岩石")
```

### 累加器（Accumulator）

```python
total = 0
for i in range(1, 6):
    total += i                  # 1+2+3+4+5
    print(f"加了 {i}，現在是 {total}")
print(f"總共：{total}")         # 15
```

> **類比：** 就像背包——每挖到一個礦就放進去，最後算總數

---

## break 和 continue（10 分鐘）

### break：立刻跳出迴圈
```python
for i in range(1, 11):
    if i == 5:
        print("找到鑽石！停止挖掘！")
        break
    print(f"挖第 {i} 格：沒有鑽石...")
# i==5 時 break，6,7,8... 不會執行
```

### continue：跳過這一圈，繼續下一圈
```python
for i in range(1, 8):
    if i == 4:
        print(f"第 {i} 層：跳過（已知空洞）")
        continue
    print(f"第 {i} 層：挖掘中...")
# i==4 的那次被跳過，其他照常執行
```

---

## % 取餘數運算子（進階，5 分鐘）

`%` 是「取餘數」——除法的尾巴。

```python
10 % 3   # 1   （10 除以 3，商 3 餘 1）
7  % 2   # 1   （7 除以 2，商 3 餘 1）
6  % 2   # 0   （6 除以 2，整除，餘 0）
```

**最常見用途：判斷奇偶數**

```python
for i in range(1, 6):
    if i % 2 == 0:
        print(f"{i} 是偶數")
    else:
        print(f"{i} 是奇數")
```

> **類比：** 你有 10 顆鑽石要平分給 3 個人，每人拿 3 顆，剩下 10 % 3 = 1 顆

---

## 巢狀 for（進階，5 分鐘）

```python
# 印出 3x3 農場格子
for row in range(3):
    for col in range(3):
        print(f"[{row},{col}]", end=" ")
    print()     # 每行結束換行
```

輸出：
```
[0,0] [0,1] [0,2]
[1,0] [1,1] [1,2]
[2,0] [2,1] [2,2]
```

---

## 課堂練習（10 分鐘）

**練習 1：挖礦報告**
```python
diamonds = 0
for layer in range(1, 17):
    if layer <= 5:
        print(f"Y={layer}: 岩漿層，危險！")
    elif layer <= 12:
        print(f"Y={layer}: 鑽石層 💎")
        diamonds += 1
    else:
        print(f"Y={layer}: 普通石頭")
print(f"\n共經過 {diamonds} 個鑽石層！")
```

**練習 2（一起）：加總挖到的礦物**
```python
total_ore = 0
for i in range(5):
    ore = int(input(f"第 {i+1} 次挖到幾個礦？"))
    total_ore += ore
print(f"總共挖到 {total_ore} 個礦！")
```

**練習 3（挑戰）：印出血量條**
```python
hp = int(input("輸入血量（0-20）："))
bar = "❤" * hp + "♡" * (20 - hp)
print(f"[{bar}] {hp}/20")
```

---

## 常見錯誤

```python
# ❌ for 迴圈忘記縮排
for i in range(5):
print(i)          # IndentationError

# ❌ range 的邊界搞混
for i in range(1, 5):
    print(i)      # 印出 1,2,3,4（不含5！）

# ❌ 修改迴圈變數（沒有意義）
for i in range(5):
    i = 10        # 這樣不會影響迴圈次數！
```

---

## 作業

**「自動礦物統計機」**

讓使用者輸入「要挖幾層（N）」，程式用 for 迴圈模擬挖掘 1~N 層：
- 每層用以下規則判斷：
  - Y 1-5：「岩漿層，跳過！」（用 continue）
  - Y 6-12：「鑽石層！」（計數 +1）
  - Y 13-20：「鐵礦層！」（計數 +1，另一個變數）
  - Y 21+：「普通石頭」
- 最後印出：挖到幾個鑽石層、幾個鐵礦層

**額外挑戰：** 如果鑽石層計數超過 5，印出「鑽石礦脈！停止挖掘報告！」並用 `break` 結束

---

## 下堂課預告

「下次學 while 迴圈——for 是跑固定次數，while 是『直到...才停』！」
