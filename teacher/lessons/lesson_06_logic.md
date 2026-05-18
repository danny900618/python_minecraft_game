# 第6堂：邏輯運算子 and / or / not & 巢狀 if

**時間：** 1 小時｜**預備知識：** 第1-5堂

---

## 今天的目標
- 用 `and` / `or` / `not` 組合多個條件
- 寫出巢狀 if（if 裡面的 if）
- 做出更複雜的「決策程式」

---

## 複習（5 分鐘）

```python
hp = int(input("血量："))
if hp >= 10:
    print("安全")
elif hp >= 1:
    print("危險")
else:
    print("死亡")
```

快問：`==` 和 `=` 的差別？縮排很重要因為？

---

## and：兩個條件都要成立（10 分鐘）

> **類比：** 合成台的規則——「需要 3 個木頭 AND 2 個石頭」，兩樣都要有

```python
has_sword  = True
has_shield = True

if has_sword and has_shield:
    print("裝備齊全！可以打 Boss！")
else:
    print("裝備不足，先準備一下")
```

**真值表：**
| A | B | A and B |
|---|---|---------|
| True | True | **True** |
| True | False | False |
| False | True | False |
| False | False | False |

```python
hp   = 15
food = 18

if hp >= 10 and food >= 10:
    print("狀態良好，出發！")
else:
    print("有東西不足，先補充")
```

---

## or：其中一個成立就好（10 分鐘）

> **類比：** 「天黑了 OR 下雨了」→ 就要回家，只要一個成立就回

```python
is_night = True
is_raining = False

if is_night or is_raining:
    print("回家！")
else:
    print("繼續探索")
```

**真值表：**
| A | B | A or B |
|---|---|--------|
| True | True | True |
| True | False | **True** |
| False | True | **True** |
| False | False | False |

```python
hp   = 3
food = 2

if hp <= 5 or food <= 5:
    print("⚠️  警告：有生命跡象異常！")
```

---

## not：反轉條件（5 分鐘）

```python
has_key = False

if not has_key:
    print("沒有鑰匙，無法開門")
else:
    print("有鑰匙！進入！")
```

> `not True` → `False`  
> `not False` → `True`

---

## 組合使用（5 分鐘）

```python
hp        = 8
has_sword = True
is_night  = True

if hp >= 5 and has_sword and is_night:
    print("血量夠、有武器、又是夜晚——去打殭屍！")
elif hp < 5 or not has_sword:
    print("不適合戰鬥，先準備")
else:
    print("白天不需要擔心，去挖礦！")
```

---

## 巢狀 if（10 分鐘）

if 裡面再放 if，用來做「分層判斷」。

```python
has_diamond = True
has_sword   = False

if has_diamond:
    print("有鑽石！")
    if has_sword:
        print("  而且有劍，可以打 Boss！")
    else:
        print("  但沒有劍，先去合成鑽石劍！")
else:
    print("沒有鑽石，繼續挖礦")
```

> **類比：** 就像 Minecraft 的條件指令方塊——先判斷一個條件，成立後再判斷下一個

---

## 課堂練習（10 分鐘）

**練習 1：Boss 戰判斷**
```python
hp         = int(input("血量："))
has_sword  = input("有劍？(yes/no)：") == "yes"
has_potion = input("有藥水？(yes/no)：") == "yes"

can_fight = hp >= 10 and has_sword
if can_fight:
    if has_potion:
        print("完美準備！去打末影龍！")
    else:
        print("可以打，但建議帶藥水")
elif hp < 10 and not has_sword:
    print("血量低又沒有武器，趕快補充！")
else:
    print("準備不完整，繼續準備")
```

**練習 2（一起寫）：礦物鑑定師**
```python
ore = input("輸入礦物名稱：")

if ore == "鑽石" or ore == "下界合金":
    print("稀有礦物！好好保存！")
elif ore == "金礦" or ore == "鐵礦":
    print("普通礦物，用來合成工具")
else:
    print("不認識這種礦物")
```

---

## 常見錯誤

```python
# ❌ 用 = 而不是 == 在條件裡
if hp = 10:      # SyntaxError

# ❌ 把 and 寫錯
if hp > 5 AND food > 5:   # NameError（大寫）

# ❌ 重複寫變數名稱
if ore == "鑽石" or "金礦":  # 不會報錯但邏輯錯誤！
# 正確：
if ore == "鑽石" or ore == "金礦":
```

---

## 作業

**「Minecraft 合成台程式」**

讓使用者輸入材料數量：
- 木頭數量、石頭數量、鐵錠數量、鑽石數量

程式判斷可以合成哪些東西（符合才印出）：
- 木劍：需要 2 個木頭
- 石劍：需要 2 個石頭
- 鐵劍：需要 2 個鐵錠
- 鑽石劍：需要 2 個鑽石
- 石鎬：需要 2 個木頭 AND 3 個石頭
- 鐵鎬：需要 2 個木頭 AND 3 個鐵錠

如果什麼都合成不了，印出「材料不足！」

---

## 下堂課預告

「下次學 for 迴圈——讓程式重複做事！就像 Minecraft 的自動農場！」
