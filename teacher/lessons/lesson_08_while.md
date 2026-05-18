# 第8堂：while 迴圈

**時間：** 1 小時｜**預備知識：** 第1-7堂

---

## 今天的目標
- 理解 `while` 和 `for` 的差別
- 寫出 `while` 迴圈
- 用 `while True + break` 做互動選單
- 做出戰鬥模擬器

---

## 複習（5 分鐘）

```python
total = 0
for i in range(1, 4):
    total += i
print(total)   # ?

# break 做什麼？continue 做什麼？
```

---

## for vs while（5 分鐘）

| | `for` | `while` |
|-|-------|---------|
| 何時用 | **知道**要跑幾次 | **不知道**要跑幾次 |
| 停止條件 | 跑完就停 | 條件變 False 才停 |
| 例子 | 挖 10 層礦 | 打怪直到死 |

> **類比：**
> - `for`：「我要做 10 個蛋糕，做完就停」
> - `while`：「做蛋糕，直到麵粉用完為止」

---

## while 基本語法（15 分鐘）

```python
hp = 10
while hp > 0:
    print(f"殭屍攻擊！血量：{hp}")
    hp -= 3
print("Steve 死了...")
```

**語法說明：**
- 每次執行前先檢查條件
- 條件成立 → 執行區塊
- 條件不成立 → 跳出迴圈

### ⚠️ 無限迴圈陷阱

```python
# ❌ 這樣會永遠跑下去！
hp = 10
while hp > 0:
    print("攻擊！")
    # 忘了 hp -= 某個數字 → hp 永遠是 10

# 如果跑了，按 Ctrl+C 停止
```

**修正：** 確保每次迴圈都讓條件「往停止方向走」

---

## while True + break（10 分鐘）

`while True` 是「永遠成立的迴圈」，搭配 `break` 在特定時機跳出。

```python
while True:
    cmd = input("輸入指令（挖礦/回家/退出）：")
    if cmd == "退出":
        print("掰掰！")
        break
    elif cmd == "挖礦":
        print("開始挖礦！")
    elif cmd == "回家":
        print("回到基地！")
    else:
        print("不認識的指令")
# 輸入「退出」才會停
```

> **類比：** 就像 Minecraft 的遊戲主迴圈——一直在跑，直到你按 Esc 或關閉遊戲

---

## 計數器 while（5 分鐘）

```python
count = 0
while count < 5:
    print(f"挖掘中... {count + 1}/5")
    count += 1  # 一定要更新！
print("挖完了！")
```

---

## 課堂練習（15 分鐘）

**練習 1：猜數字遊戲（一起寫）**
```python
secret = 64       # 鑽石最好挖的 Y 座標
guess_count = 0

while True:
    guess = int(input("猜猜鑽石層的 Y 座標："))
    guess_count += 1

    if guess == secret:
        print(f"正確！你猜了 {guess_count} 次！")
        break
    elif guess > secret:
        print("太高了！往下挖！")
    else:
        print("太低了！往上走！")
```

**練習 2：戰鬥模擬器**
```python
player_hp  = 20
zombie_hp  = 10
player_atk = 4
zombie_atk = 2
round_num  = 1

while player_hp > 0 and zombie_hp > 0:
    print(f"\n--- 第 {round_num} 回合 ---")
    zombie_hp  -= player_atk
    player_hp  -= zombie_atk
    print(f"玩家攻擊！殭屍剩 {max(zombie_hp,0)} 血")
    print(f"殭屍攻擊！玩家剩 {max(player_hp,0)} 血")
    round_num  += 1

print()
if player_hp > 0:
    print("🏆 玩家獲勝！")
else:
    print("💀 殭屍獲勝...")
```

**練習 3（挑戰）：背包選單**
```python
bag = []
while True:
    print("\n[1] 新增物品  [2] 查看背包  [3] 離開")
    choice = input("選擇：")
    if choice == "1":
        item = input("物品名稱：")
        bag.append(item)
        print(f"已加入 {item}")
    elif choice == "2":
        print("背包：", bag)
    elif choice == "3":
        break
```

---

## 常見錯誤

| 錯誤 | 原因 |
|------|------|
| 無限迴圈 | 忘了更新讓條件走向 False 的變數 |
| `while hp > 0` 條件永遠 False | 初始值設定錯誤，迴圈從未執行 |
| `break` 縮排錯誤 | break 要在 while 區塊內 |

---

## 作業

**「Minecraft 生存模擬器」**

玩家初始：血量 20、食物值 20、金幣 0

用 `while True` 做選單，玩家每回合選一個行動：
1. **挖礦**：金幣 +5，食物值 -2
2. **狩獵**：金幣 +3，食物值 +5，有機率（食物值>15）遇到殭屍（血量-4）
3. **吃東西**：食物值 +8，需要金幣 3（不夠就提示）
4. **結束遊戲**：顯示統計後結束

條件：
- 血量 ≤ 0 或食物值 ≤ 0：「遊戲結束！你沒有撐過去」
- 金幣達到 50：「恭喜！你已經收集到足夠的資源！」

---

## 下堂課預告

「下次學 List 串列——讓程式可以管理一整個背包的物品！」
