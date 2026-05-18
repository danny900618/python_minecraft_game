# 第9堂：串列 List

**時間：** 1 小時｜**預備知識：** 第1-8堂

---

## 今天的目標
- 理解 List 的概念
- 建立、讀取、修改 List
- 常用方法：`append` `remove` `pop` `sort`
- 用 `in` 檢查元素
- 搭配 for 迴圈

---

## 複習（5 分鐘）

```python
hp = 10
while hp > 0:
    hp -= 3
print(hp)   # ?（考驗學生）

# while True + break 的場景是？
```

---

## 什麼是 List？（5 分鐘）

> **類比：** 就是 Minecraft 的背包！可以放很多格東西，每格有一個編號（從 0 開始）

```
背包：  [0]木頭   [1]石頭   [2]鑽石
List：  ["木頭",  "石頭",   "鑽石"]
```

```python
bag = ["木頭", "石頭", "鑽石"]
```

---

## 建立 List（3 分鐘）

```python
# 空 list
bag = []

# 有初始內容的 list
tools    = ["鎬子", "斧頭", "鏟子"]
numbers  = [1, 2, 3, 4, 5]
mixed    = ["Steve", 20, True]   # 可以放不同型別（但一般不建議混用）
```

---

## 讀取元素：索引（Index）（10 分鐘）

```python
bag = ["木頭", "石頭", "鑽石", "金礦"]
#       [0]     [1]     [2]     [3]

print(bag[0])    # 木頭
print(bag[2])    # 鑽石
print(bag[-1])   # 金礦（從後面數，-1 是最後一個）
print(bag[-2])   # 鑽石（倒數第二個）
```

❓ **問學生：** `bag[4]` 會怎樣？→ IndexError！

---

## 修改 List（10 分鐘）

### append()：加到最後
```python
bag = []
bag.append("木頭")
bag.append("石頭")
print(bag)    # ["木頭", "石頭"]
```

### remove()：刪除指定元素
```python
bag = ["木頭", "石頭", "鑽石"]
bag.remove("石頭")
print(bag)    # ["木頭", "鑽石"]
```

### pop()：移除並回傳最後一個（或指定位置）
```python
bag = ["木頭", "石頭", "鑽石"]
item = bag.pop()       # 拿出最後一個
print(item)    # 鑽石
print(bag)     # ["木頭", "石頭"]
```

### 修改指定位置
```python
bag = ["木頭", "石頭"]
bag[0] = "鑽石"         # 把第 0 格換掉
print(bag)    # ["鑽石", "石頭"]
```

---

## 常用功能（5 分鐘）

```python
bag = ["木頭", "石頭", "鑽石"]

print(len(bag))         # 3（幾個元素）

print("鑽石" in bag)    # True（有沒有）
print("金礦" in bag)    # False

bag.sort()              # 排序（字母順序）
numbers = [5, 2, 8, 1]
numbers.sort()
print(numbers)          # [1, 2, 5, 8]
```

---

## List 切片 Slice（5 分鐘）

```python
bag = ["木頭", "石頭", "鑽石", "金礦", "煤炭"]
#       [0]     [1]     [2]     [3]     [4]

print(bag[1:3])     # ["石頭", "鑽石"]（1到2，不含3）
print(bag[:2])      # ["木頭", "石頭"]（從頭到1）
print(bag[2:])      # ["鑽石", "金礦", "煤炭"]（2到最後）
```

---

## for 迴圈遍歷 List（5 分鐘）

```python
bag = ["木頭", "石頭", "鑽石"]

for item in bag:
    print(f"背包裡有：{item}")
```

```python
# 計算背包裡有幾個鑽石
bag = ["木頭", "鑽石", "石頭", "鑽石", "鑽石"]
diamond_count = 0
for item in bag:
    if item == "鑽石":
        diamond_count += 1
print(f"共有 {diamond_count} 個鑽石")
```

---

## 課堂練習（10 分鐘）

**練習 1：簡單背包**
```python
bag = []
bag.append("木頭")
bag.append("鑽石")
bag.append("鐵錠")

print(f"背包有 {len(bag)} 個物品")
print("物品清單：")
for item in bag:
    print(f"  - {item}")

if "鑽石" in bag:
    print("有鑽石！可以合成武器！")
```

**練習 2（一起）：背包選單**
```python
bag = ["木劍", "麵包"]

while True:
    print(f"\n背包：{bag}")
    print("[1]新增  [2]刪除  [3]查詢  [4]離開")
    choice = input("選擇：")

    if choice == "1":
        item = input("加入什麼？")
        bag.append(item)
    elif choice == "2":
        item = input("刪除什麼？")
        if item in bag:
            bag.remove(item)
        else:
            print("背包裡沒有這個物品")
    elif choice == "3":
        item = input("查詢什麼？")
        print("有！" if item in bag else "沒有")
    elif choice == "4":
        break
```

---

## 常見錯誤

| 錯誤 | 原因 |
|------|------|
| `bag[5]` 但只有 3 個元素 | IndexError：超出範圍 |
| `bag.remove("不存在的物品")` | ValueError：找不到元素 |
| `bag = bag.append("物品")` | append() 不回傳新 list！這樣 bag 會變 None |

---

## 作業

**「Minecraft 完整背包系統」**

功能：
1. 新增物品（不能加超過 9 格：bag 長度 < 9）
2. 丟棄物品（輸入名稱刪除）
3. 查看所有物品（用 for 迴圈，每行印一個）
4. 搜尋物品（顯示在哪個格子，即索引）
5. 排序背包
6. 離開

初始背包：`["木頭", "石頭", "麵包"]`

---

## 下堂課預告

「下次學函式（Function）——把重複用的程式碼包起來，超級實用！」
