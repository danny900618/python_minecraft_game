# 第2堂：變數與資料型別

**時間：** 1 小時｜**預備知識：** 第1堂

---

## 今天的目標
- 理解什麼是「變數」
- 認識四種基本資料型別：`int` `float` `str` `bool`
- 能用 `type()` 查看型別
- 知道如何更新變數的值

---

## 複習（5 分鐘）
- `print("Hello")` 怎麼寫？
- `#` 是什麼用途？
- 讓學生秀出上次作業

---

## 概念：什麼是變數？（10 分鐘）

> **類比：** Minecraft 背包的格子。每個格子有一個編號（變數名稱），格子裡放著東西（值）。你隨時可以換格子裡放的東西。

```python
hp     = 20        # 這個格子叫 hp，裡面放著數字 20
name   = "Steve"   # 這個格子叫 name，放著字串 "Steve"
level  = 1         # 等級
weapon = "木劍"
```

**賦值的方向：** `=` 是「把右邊的值，放進左邊的格子」

❓ **問學生：** 「`20 = hp` 可以嗎？」→ 不行，左邊一定是格子名稱。

---

## 四種基本型別（15 分鐘）

### int（整數）
```python
hp    = 20
level = 99
coins = -5    # 可以是負數
```
> 像 Minecraft 的生命值、等級——整數，沒有小數點

### float（浮點數）
```python
speed   = 1.5
hp_regen = 0.5   # 每秒回血 0.5
```
> 像移動速度、回血量——有小數點

### str（字串）
```python
name   = "Steve"
weapon = '鑽石劍'   # 單引號雙引號都可以
biome  = "沙漠"
```
> 像告示牌上的文字——用引號包起來

### bool（布林值）
```python
is_alive     = True
has_diamond  = False
is_daytime   = True
```
> 像 Redstone 訊號——只有「開（True）」或「關（False）」兩種狀態

---

## 用 type() 查看型別（5 分鐘）

```python
print(type(20))          # <class 'int'>
print(type(3.14))        # <class 'float'>
print(type("Steve"))     # <class 'str'>
print(type(True))        # <class 'bool'>
```

**現場讓學生猜型別：**
- `type(100)` → ?
- `type("100")` → ?（數字加了引號就是字串！）
- `type(True)` → ?

---

## 變數命名規則（5 分鐘）

| 規則 | 範例 |
|------|------|
| ✅ 英文字母、數字、底線 | `hp`, `my_sword`, `level2` |
| ✅ 不能以數字開頭 | ~~`2sword`~~ |
| ✅ 不能有空格 | ~~`my sword`~~ |
| ✅ 不能用連字號 | ~~`my-sword`~~ |
| ✅ 大小寫有差異 | `HP` 和 `hp` 是不同變數 |

> **慣例：** 多個單字用底線連接，全部小寫（snake_case）
> `player_name`, `max_hp`, `is_alive`

---

## 更新變數（5 分鐘）

```python
hp = 20
print(hp)   # 20

hp = 15     # 被怪物打了
print(hp)   # 15

hp = hp - 3  # 又被打
print(hp)   # 12

hp += 5      # 吃了食物回血（+= 是 hp = hp + 5 的縮寫）
print(hp)   # 17
```

**其他縮寫運算：**
```python
level += 1    # 升一級
coins -= 10   # 花了 10 金幣
speed *= 2    # 速度變兩倍
```

---

## 課堂練習（10 分鐘）

**練習 1：**
```python
# 建立你的 Minecraft 角色資料
# 要包含：名字(str)、血量(int)、速度(float)、是否有鑽石(bool)
name       = "Alex"
hp         = 20
speed      = 1.5
has_diamond = False

print("名字：", name)
print("血量：", hp)
print("速度：", speed)
print("有鑽石？", has_diamond)
```

**練習 2（一起做）：**
```python
# 模擬一場戰鬥
hp = 20
print("戰鬥開始！血量：", hp)

hp -= 7         # 被殭屍打
print("被殭屍打！血量：", hp)

hp -= 4         # 被骷髏射到
print("被骷髏射到！血量：", hp)

hp += 3         # 吃了金蘋果
print("吃金蘋果！血量：", hp)

print("最終血量：", hp)
```

---

## 常見錯誤

| 錯誤 | 原因 |
|------|------|
| `name = Steve` → NameError | 字串忘加引號，Python 以為 Steve 是個變數 |
| `2hp = 20` → SyntaxError | 變數名不能以數字開頭 |
| `hp = hp + 1`（hp 未定義）→ NameError | 使用變數前要先賦值 |

---

## 作業

**「Minecraft 角色產生器 v1」**

建立以下變數並用 `print()` 印出漂亮的角色卡：
- `name`（你的角色名字）
- `hp`、`max_hp`（目前血量和最大血量）
- `level`（等級）
- `weapon`（武器名稱）
- `is_in_nether`（是否在地獄，True/False）
- `speed`（移動速度，用 float）

**額外挑戰：** 模擬角色受到 5 點傷害後，用 `print()` 印出受傷前和受傷後的血量。

---

## 下堂課預告

「下次學字串操作——怎麼把兩個字串接在一起，還有字串的魔法方法！」
