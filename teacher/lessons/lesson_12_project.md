# 第12堂：期末專案 — Minecraft 文字冒險遊戲

**時間：** 1 小時｜**預備知識：** 第1-11堂

---

## 今天的目標
- 把所有語法整合成一個完整遊戲
- 學習程式設計的思考方式（拆解問題）
- 完成並展示期末專案
- 了解「下一步」：字典、模組、turtle 繪圖...

---

## 開場：讓學生展示作業（10 分鐘）

請學生展示第11堂的地下城作業，老師給予鼓勵和建議。

---

## 期末專案：Minecraft 文字冒險（45 分鐘）

以下是完整的範本程式碼，老師先說明架構，再和學生一起讀、理解、並嘗試修改。

```python
# ============================================
# Minecraft 文字冒險遊戲 - 期末專案範本
# ============================================

# ── 工具函式 ────────────────────────────────
def show_status(name, hp, max_hp, bag, gold):
    bar = "❤" * min(hp, 10) + "♡" * (10 - min(hp, 10))
    print(f"\n{'='*40}")
    print(f"  {name}  |  [{bar}] {hp}/{max_hp}")
    print(f"  💰 金幣: {gold}  🎒 背包: {', '.join(bag) if bag else '空'}")
    print(f"{'='*40}")

def calc_damage(attack, defense):
    return max(attack - defense, 1)

def fight(player_name, p_hp, p_atk, enemy_name, e_hp, e_atk):
    print(f"\n⚔  與 {enemy_name} 戰鬥開始！")
    round_n = 1
    max_p = p_hp

    while p_hp > 0 and e_hp > 0:
        dmg_to_enemy  = calc_damage(p_atk, 0)
        dmg_to_player = calc_damage(e_atk, 0)

        e_hp -= dmg_to_enemy
        p_hp -= dmg_to_player

        print(f"  回合{round_n}: 你造成{dmg_to_enemy}傷, 受到{dmg_to_player}傷 "
              f"| 敵方剩 {max(e_hp,0)} 血")
        round_n += 1

    return p_hp   # 回傳玩家剩餘血量

# ── 房間設定 ─────────────────────────────────
ROOMS = [
    {
        "name"    : "廢棄礦坑",
        "desc"    : "你走進一個昏暗的礦坑。地上散落著礦石，\n  遠處傳來殭屍的呻吟聲...",
        "enemy"   : ("殭屍",   8,  2),   # (名稱, 血量, 攻擊)
        "reward"  : ("鐵劍",   5, 3),    # (物品, 金幣, 攻擊力加成)
    },
    {
        "name"    : "地下湖邊",
        "desc"    : "你來到一個地下湖。湖面反射著岩漿的紅光，\n  一隻骷髏兵正在瞄準你！",
        "enemy"   : ("骷髏兵", 10, 3),
        "reward"  : ("弓",    10, 2),
    },
    {
        "name"    : "末影傳送門室",
        "desc"    : "你找到了末影傳送門！但守門的末影人\n  已經瞪著你了...",
        "enemy"   : ("末影人", 20, 5),
        "reward"  : ("末影珍珠", 20, 0),
    },
]

# ── 主程式 ───────────────────────────────────
def main():
    print("=" * 40)
    print("  ⛏  Minecraft 文字冒險  ⛏")
    print("  目標：通過三個房間，打開末影傳送門！")
    print("=" * 40)

    name   = input("\n輸入你的角色名稱：")
    hp     = 20
    max_hp = 20
    atk    = 3
    bag    = ["麵包 x2"]
    gold   = 0

    for i, room in enumerate(ROOMS):
        print(f"\n\n{'#'*40}")
        print(f"  【房間 {i+1}/{len(ROOMS)}】{room['name']}")
        print(f"{'#'*40}")
        print(f"\n  {room['desc']}")
        show_status(name, hp, max_hp, bag, gold)

        while True:
            print("\n  你要怎麼做？")
            print("  [1] 戰鬥！")
            print("  [2] 逃跑（扣 3 血，跳到下一個房間）")
            if "麵包 x2" in bag:
                print("  [3] 吃麵包（回血 6，僅限一次）")

            choice = input("  選擇：")

            if choice == "1":
                e_name, e_hp, e_atk = room["enemy"]
                hp = fight(name, hp, atk, e_name, e_hp, e_atk)

                if hp <= 0:
                    print(f"\n💀  {name} 倒下了... 遊戲結束")
                    print(f"   到達了 {i+1}/{len(ROOMS)} 個房間")
                    return

                item, coins, atk_bonus = room["reward"]
                gold  += coins
                atk   += atk_bonus
                bag.append(item)
                print(f"\n✨  獲得：{item}（+{atk_bonus}攻擊）和 {coins} 金幣！")
                show_status(name, hp, max_hp, bag, gold)
                break

            elif choice == "2":
                hp -= 3
                print(f"  你成功逃跑了，但受傷了（-3血）")
                if hp <= 0:
                    print(f"\n💀  逃跑時力竭倒地... 遊戲結束")
                    return
                break

            elif choice == "3" and "麵包 x2" in bag:
                hp = min(hp + 6, max_hp)
                bag.remove("麵包 x2")
                print(f"  吃了麵包！回復 6 血。現在 HP: {hp}")

            else:
                print("  無效的選擇，請重試")

        input("\n  按 Enter 繼續...")

    # ── 通關 ─────────────────────────────────
    print("\n" + "★" * 40)
    print("  🏆  恭喜！你通過了所有試煉！")
    print(f"  末影傳送門在你面前開啟！")
    print(f"  {name} 踏入傳送門，前往末地...")
    show_status(name, hp, max_hp, bag, gold)
    print("\n  ★  挑戰完成！你是 Minecraft 英雄！")
    print("★" * 40)

if __name__ == "__main__":
    main()
```

---

## 架構說明（讓學生理解）

```
程式架構：
├── 工具函式
│   ├── show_status()    → 印出狀態（用了 f-string + min()）
│   ├── calc_damage()    → 計算傷害（用了 max()）
│   └── fight()          → 戰鬥邏輯（用了 while + if）
├── 資料
│   └── ROOMS            → List 裡面放 dict（下一步要學的字典！）
└── 主程式 main()
    └── for room in ROOMS（for 迴圈跑每個房間）
        └── while True（選單迴圈）
            └── if/elif（根據選擇執行）
```

---

## 讓學生嘗試修改（如有時間）

1. 加入第四個房間（打末影龍！）
2. 讓玩家可以在商店買道具
3. 增加怪物的防禦值
4. 加入「暴擊」機制（隨機造成雙倍傷害）

---

## 課程總結：你學到了什麼

| 堂次 | 概念 | 你現在可以做到 |
|------|------|----------------|
| 1 | print() | 讓程式說話 |
| 2 | 變數 & 型別 | 讓程式記住資料 |
| 3-4 | 字串 & input | 和使用者互動 |
| 5-6 | if/and/or | 讓程式做決定 |
| 7 | for 迴圈 | 重複做事 |
| 8 | while 迴圈 | 直到條件成立才停 |
| 9 | List | 管理多筆資料 |
| 10 | Function | 整理、重複使用程式碼 |
| 11-12 | 綜合 | 做出完整的程式！ |

---

## 下一步可以學什麼

- **字典（dict）**：`{"name": "Steve", "hp": 20}`
- **import 模組**：`import random`（製作隨機事件）
- **檔案讀寫**：存檔讀檔功能
- **turtle 模組**：畫圖！可以做 Minecraft 地圖
- **pygame**：做真正的 2D 遊戲

---

## 結語

「你已經從 `print("Hello")` 走到能寫出一個 Minecraft 冒險遊戲了！這就是程式設計最棒的地方——一行一行累積，就能創造出你想要的世界。⛏️」
