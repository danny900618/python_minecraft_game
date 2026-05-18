# 第10堂：函式 Function

**時間：** 1 小時｜**預備知識：** 第1-9堂

---

## 今天的目標
- 理解「函式」的概念
- 用 `def` 定義函式
- 使用參數（parameter）和回傳值（return）
- 理解為什麼要用函式

---

## 複習（5 分鐘）

```python
bag = ["木頭", "鑽石", "石頭"]
count = 0
for item in bag:
    if item == "鑽石":
        count += 1
print(count)   # ?
```

`bag[-1]` 是什麼？`bag[1:3]` 是什麼？

---

## 為什麼需要函式？（5 分鐘）

**沒有函式的問題：**
```python
# 計算玩家A的傷害
damage_a = 10 - 3
print(f"玩家A造成 {damage_a} 傷害")

# 計算玩家B的傷害（一樣的邏輯，重複寫）
damage_b = 15 - 5
print(f"玩家B造成 {damage_b} 傷害")
```

**有函式的版本：**
```python
def calc_damage(attack, defense):
    return attack - defense

print(f"玩家A造成 {calc_damage(10, 3)} 傷害")
print(f"玩家B造成 {calc_damage(15, 5)} 傷害")
```

> **類比：** 函式就像 Minecraft 的合成配方——一次定義好「材料→產物」，之後每次需要就直接用，不用重新想

---

## def 語法（10 分鐘）

```python
def 函式名稱(參數1, 參數2):
    程式碼
    return 回傳值
```

### 最簡單的函式
```python
def say_hello():
    print("Hello, Minecrafter!")

say_hello()    # 呼叫函式
say_hello()    # 可以重複呼叫！
```

### 有參數的函式
```python
def greet(name):
    print(f"歡迎，{name}！準備好冒險了嗎？")

greet("Steve")   # 歡迎，Steve！準備好冒險了嗎？
greet("Alex")    # 歡迎，Alex！準備好冒險了嗎？
```

---

## return 回傳值（10 分鐘）

```python
def calc_damage(attack, defense):
    result = attack - defense
    if result < 0:
        result = 0    # 傷害不能是負數
    return result

dmg = calc_damage(10, 3)
print(f"造成 {dmg} 傷害")       # 7

print(calc_damage(3, 10))       # 0（不是負數）
```

**沒有 return 的函式**
```python
def show_hp(hp):
    print(f"HP: {'❤' * hp}")
    # 沒有 return，回傳 None

result = show_hp(5)
print(result)    # None
```

### return 多個值
```python
def battle_result(player_atk, zombie_hp):
    remaining_hp = zombie_hp - player_atk
    killed = remaining_hp <= 0
    return remaining_hp, killed

hp_left, is_dead = battle_result(8, 10)
print(f"殭屍剩 {hp_left} 血，死了嗎？{is_dead}")
```

---

## 預設參數值（5 分鐘）

```python
def level_up(name, levels=1):    # 預設升1級
    print(f"{name} 升了 {levels} 級！")

level_up("Steve")        # Steve 升了 1 級！
level_up("Alex", 3)      # Alex 升了 3 級！
```

---

## 函式呼叫函式（3 分鐘）

```python
def calc_damage(atk, defense):
    return max(atk - defense, 0)

def fight(player_hp, zombie_hp, player_atk, zombie_atk):
    while player_hp > 0 and zombie_hp > 0:
        zombie_hp -= calc_damage(player_atk, 2)
        player_hp -= calc_damage(zombie_atk, 0)
    return "勝利" if player_hp > 0 else "失敗"

print(fight(20, 10, 5, 3))
```

---

## 課堂練習（10 分鐘）

**練習 1：合成函式**
```python
def can_craft(wood, stone, item):
    if item == "木劍" and wood >= 2:
        return True
    elif item == "石劍" and stone >= 2:
        return True
    return False

print(can_craft(3, 1, "木劍"))    # True
print(can_craft(1, 3, "木劍"))    # False
print(can_craft(2, 3, "石劍"))    # True
```

**練習 2（一起）：角色卡函式**
```python
def show_character(name, hp, level, weapon="木劍"):
    print(f"{'='*25}")
    print(f"  名稱：{name}")
    print(f"  等級：{level}")
    print(f"  血量：{'❤'*min(hp,10)}")
    print(f"  武器：{weapon}")
    print(f"{'='*25}")

show_character("Steve", 20, 5)
show_character("Alex", 15, 8, "鑽石劍")
```

---

## 常見錯誤

| 錯誤 | 原因 |
|------|------|
| 函式定義後沒呼叫 | 定義函式不會執行，要用 `函式名()` 呼叫 |
| `result = show_hp(5)` 卻用 `result` | 沒有 return 的函式回傳 None |
| 參數順序錯誤 | `calc_damage(defense, attack)` 傳錯位置 |
| 函式名稱和變數名稱相同 | 會互相覆蓋，小心命名 |

---

## 作業

**「Minecraft RPG 工具包」**

寫以下 5 個函式：

1. `show_status(name, hp, max_hp, level)` — 印出角色狀態卡
2. `calc_damage(attack, defense)` — 計算傷害（最小為 0）
3. `is_alive(hp)` — 回傳 True/False
4. `can_craft(bag, recipe)` — 判斷 bag 裡有沒有 recipe 裡的所有材料（兩者都是 list）
5. `level_up(current_level, xp)` — 每 100 xp 升一級，回傳 (新等級, 剩餘xp)

最後用 `while True` 選單把這些函式組合起來用。

---

## 下堂課預告

「下次做綜合練習——把 for、if、while、list、function 全部混在一起用！」
