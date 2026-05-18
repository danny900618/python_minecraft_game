# 第11堂：綜合練習 — for + if + while + list + function

**時間：** 1 小時｜**預備知識：** 第1-10堂

---

## 今天的目標
- 複習所有概念
- 把所有語法混合使用
- 找出並修正 bug
- 完成一個小程式

---

## 複習快問快答（5 分鐘）

老師唸程式碼，學生猜輸出：

```python
# Q1
def f(x):
    return x * 2
print(f(f(3)))       # ?  → 12

# Q2
bag = [1, 2, 3, 4, 5]
total = 0
for n in bag:
    if n % 2 != 0:
        total += n
print(total)          # ?  → 9 (1+3+5)

# Q3
i = 0
while i < 3:
    i += 1
    if i == 2:
        continue
    print(i)          # ?  → 1, 3
```

---

## 範例 1：礦物統計機（全語法混合）（15 分鐘）

老師現場帶著寫，讓學生補空格：

```python
def analyze_layer(y):
    """判斷某層有什麼礦"""
    if y <= 0:
        return "無效層數"
    elif y <= 5:
        return "岩漿層"
    elif y <= 12:
        return "鑽石層 💎"
    elif y <= 20:
        return "鐵礦層 ⛏"
    else:
        return "普通石頭"

def mine(start_y, end_y):
    """模擬挖礦，回傳各層的礦物統計"""
    results = {}
    for y in range(start_y, end_y + 1):
        ore = analyze_layer(y)
        if ore not in results:
            results[ore] = 0
        results[ore] += 1
    return results

# 主程式
start = int(input("從第幾層開始挖？"))
end   = int(input("挖到第幾層？"))

if start > end:
    print("起始層不能大於終止層！")
else:
    stats = mine(start, end)
    print("\n=== 挖礦報告 ===")
    for ore_type, count in stats.items():
        print(f"  {ore_type}: {count} 層")
```

---

## 範例 2：Debug 練習（10 分鐘）

老師給出有 bug 的程式，學生找錯誤：

```python
# Bug 版本 — 找出 3 個錯誤！
def count_diamonds(bag):
    count = 0
    for item in bag
        if item = "鑽石":
            count += 1
    return count

my_bag = ["木頭", "鑽石", "石頭", "鑽石"]
result = count_diamonds(my_bag)
print(f"有 {result} 個鑽石")
```

**Bug 解答：**
1. `for item in bag` 後面少了冒號 `:`
2. `if item = "鑽石"` 要用 `==` 而不是 `=`
3. 縮排問題（`count += 1` 要在 if 裡面）

---

## 練習：Minecraft RPG 戰鬥系統（25 分鐘）

和學生一起從零寫起：

```python
def show_status(name, hp, max_hp):
    bar = "❤" * hp + "♡" * (max_hp - hp)
    print(f"{name}: [{bar}] {hp}/{max_hp}")

def attack(attacker_atk, defender_def):
    damage = max(attacker_atk - defender_def, 1)   # 至少造成 1 傷害
    return damage

def battle(player_name, p_hp, p_atk,
           enemy_name,  e_hp, e_atk, e_def=0):
    max_p = p_hp
    max_e = e_hp
    round_n = 1

    while p_hp > 0 and e_hp > 0:
        print(f"\n── 第 {round_n} 回合 ──")
        show_status(player_name, max(p_hp,0), max_p)
        show_status(enemy_name,  max(e_hp,0), max_e)

        # 玩家攻擊
        dmg = attack(p_atk, e_def)
        e_hp -= dmg
        print(f"⚔  {player_name} 攻擊 {enemy_name}，造成 {dmg} 傷害")

        if e_hp <= 0:
            break

        # 敵人攻擊
        dmg2 = attack(e_atk, 0)
        p_hp -= dmg2
        print(f"💀 {enemy_name} 反擊 {player_name}，造成 {dmg2} 傷害")

        round_n += 1

    print()
    if p_hp > 0:
        print(f"🏆 {player_name} 獲勝！共 {round_n} 回合")
    else:
        print(f"💀 {enemy_name} 獲勝...")

# 主程式
print("=== Minecraft 戰鬥模擬器 ===")
player = input("玩家名稱：")
p_atk  = int(input("攻擊力："))

enemies = [
    ("殭屍",    10, 2, 0),
    ("骷髏兵",  8,  3, 1),
    ("末影人",  20, 5, 2),
]

for name, hp, atk, defense in enemies:
    print(f"\n遇到了 {name}！")
    battle(player, 20, p_atk, name, hp, atk, defense)
    input("按 Enter 繼續...")
```

---

## 常見卡關點

- **`dict.items()`** 可以同時拿到 key 和 value，很方便
- **`max(value, 0)`** 確保數值不會小於 0
- 函式要**先定義後呼叫**
- `break` 只跳出**最近的**那層迴圈

---

## 作業

**「Minecraft 地下城探索」**

設計一個有 3 個房間的地下城：
- 每個房間有一個怪物和一個寶箱
- 玩家有血量（20）和武器（影響攻擊力）
- 每個房間：玩家可選擇「戰鬥」或「逃跑」
  - 戰鬥：用函式計算戰鬥結果
  - 逃跑：直接到下一房間，但扣 2 血
- 打敗怪物後可以開寶箱（獲得武器升級或回血）
- 通過所有房間 → 印出勝利訊息
- 血量歸零 → 遊戲結束

---

## 下堂課預告

「下次是最後一堂！做一個完整的 Minecraft 文字冒險遊戲，把所有學到的東西全部用上！」
