# 第3堂：字串操作

**時間：** 1 小時｜**預備知識：** 第1-2堂

---

## 今天的目標
- 用 `+` 串接字串
- 用 `len()` 計算字串長度
- 使用常見字串方法：`upper()` `lower()` `replace()` `strip()`
- 用 `*` 重複字串

---

## 複習（5 分鐘）

快速問答：
- 四種資料型別是？
- `hp += 5` 等於？
- `type("20")` 回傳？（答案：`str`，不是 `int`！）

---

## 字串串接 `+`（10 分鐘）

> **類比：** 就像在 Minecraft 告示牌上把兩行文字拼在一起

```python
first = "末影"
last  = "龍"
boss  = first + last        # "末影龍"
print(boss)

name     = "Steve"
greeting = "Hello, " + name + "!"
print(greeting)             # Hello, Steve!
```

❗ **注意：** 字串只能和字串相加，不能直接加數字
```python
# print("血量：" + 20)   ← 這樣會錯！
print("血量：" + str(20))  # 要先用 str() 轉換
```

---

## 字串重複 `*`（5 分鐘）

```python
print("=" * 20)          # ====================
print("❤ " * 5)          # ❤ ❤ ❤ ❤ ❤
print("挖！" * 3)          # 挖！挖！挖！
```

**實用：** 做漂亮的分隔線
```python
print("=" * 30)
print("  Minecraft 角色卡")
print("=" * 30)
```

---

## len()：字串長度（5 分鐘）

```python
name = "creeper"
print(len(name))         # 7

print(len("Minecraft"))  # 9
print(len(""))           # 0（空字串）
```

❓ **問學生：** `len("末影龍")` 是幾？（答案：3，中文每個字算一個）

---

## 字串方法（15 分鐘）

> **類比：** 方法就像 Minecraft 附魔書，套在字串上就能產生效果

### upper() / lower()
```python
name = "steve"
print(name.upper())      # STEVE
print(name.lower())      # steve

shout = "CREEPER INCOMING"
print(shout.lower())     # creeper incoming
```

### replace()
```python
sentence = "我愛 Minecraft"
new = sentence.replace("Minecraft", "Python")
print(new)               # 我愛 Python
```

### strip()
```python
messy = "   Steve   "    # 前後有空白
clean = messy.strip()
print(clean)             # "Steve"（空白被清掉）
```

### 連續使用方法（Chaining）
```python
name = "  STEVE  "
result = name.strip().lower()
print(result)            # "steve"
```

---

## 字串索引（進階，可跳過）（5 分鐘）

字串裡每個字都有一個位置（從 0 開始）：
```python
name = "Steve"
#       01234
print(name[0])    # S
print(name[1])    # t
print(name[-1])   # e（從後面數）
```

> **類比：** 就像背包的格子編號，從 0 號格開始

---

## 課堂練習（10 分鐘）

**練習 1：**
```python
# 做一個 Minecraft 告示牌
line = "-" * 20
title = "Minecraft 商店"
print(line)
print(title)
print(line)
```

**練習 2：**
```python
# 字串操作練習
player = "  alex  "
# 1. 去掉空格
# 2. 轉成大寫
# 3. 印出結果和長度
clean = player.strip()
upper = clean.upper()
print(upper)
print("長度：", len(upper))
```

**練習 3（挑戰）：**
```python
# 把武器名稱加上附魔效果
weapon = "鑽石劍"
enchant = "鋒利 V"
full_name = weapon + " [" + enchant + "]"
print(full_name)           # 鑽石劍 [鋒利 V]
```

---

## 小遊戲：猜測輸出

老師念出程式，學生猜結果：

```python
print("ha" * 3)            # hahaha
print(len("diamond"))      # 7
print("CREEPER".lower())   # creeper
print("x" + "y" + "z")    # xyz
```

---

## 常見錯誤

| 錯誤 | 原因 |
|------|------|
| `"HP:" + 20` → TypeError | 字串不能直接加數字，用 `str(20)` |
| `name.Upper()` → AttributeError | 方法名稱大小寫有差，是 `upper()` |
| `len(20)` → TypeError | `len()` 只能用在字串和 list，不能用在數字 |

---

## 作業

**「附魔武器產生器」**

寫一個程式，建立以下變數後印出漂亮的武器介紹：
- 武器名稱（如：鑽石劍）
- 附魔名稱（如：鋒利）
- 附魔等級（如：5）

印出格式：
```
==============================
  武器：鑽石劍
  附魔：鋒利 5
  名稱長度：3 個字
  大寫版本：鑽石劍
==============================
```

**額外挑戰：** 用 `replace()` 把武器描述裡的「鑽石」換成「下界合金」

---

## 下堂課預告

「下次學 `input()` 讓使用者自己輸入資料，還有神奇的 f-string！」
