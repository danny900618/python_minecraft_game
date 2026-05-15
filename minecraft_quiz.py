"""
Minecraft Python 學習遊戲 v3
─────────────────────────────
執行方式  ：python minecraft_quiz.py
關卡解鎖  ：老師上完課後傳解鎖碼給學生，在主選單輸入即可
難度設定  ：編輯 game_config.json（題數 / 生命值）
學生進度  ：自動儲存於 player_save.json
新增題目  ：在 question_bank.py 對應章節加入新題目 dict
"""

import hashlib
import json
import os
import random
import sys
import time
from pathlib import Path

# ── 路徑 ──────────────────────────────────────────────────
BASE_DIR   = Path(__file__).parent
CONFIG_F   = BASE_DIR / "game_config.json"
SAVE_F     = BASE_DIR / "player_save.json"

# ── 啟用 Windows ANSI 顏色 ────────────────────────────────
try:
    import ctypes
    ctypes.windll.kernel32.SetConsoleMode(
        ctypes.windll.kernel32.GetStdHandle(-11), 7)
except Exception:
    pass

R  = "\033[0m"
B  = "\033[1m"
GR = "\033[92m"
YL = "\033[93m"
RD = "\033[91m"
CY = "\033[96m"
BL = "\033[94m"
PR = "\033[95m"
GY = "\033[90m"
WH = "\033[97m"

COLOR_MAP = {
    "green" : GR, "yellow": YL, "red"   : RD,
    "cyan"  : CY, "blue"  : BL, "purple": PR,
}

def c(text, color_str):
    return f"{color_str}{text}{R}"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def slow_print(text, delay=0.025):
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(delay)
    print()

def press_enter(msg="  [ 按 Enter 繼續 ]"):
    input(c(f"\n{msg}", GY))

# ── 解鎖碼（SHA-256，無法從檔案反推原始代碼）───────────────────
def _h(code: str) -> str:
    return hashlib.sha256(code.upper().encode()).hexdigest()

def _build_unlock_table():
    _raw = [
        ("STONE04",  ["io"],        "💬 第二關：輸入輸出 & 字串"),
        ("IRON06",   ["if"],        "⚔️  第三關：條件判斷"),
        ("GOLD07",   ["for"],       "🔄  第四關：for 迴圈"),
        ("LAPIS08",  ["while"],     "🔁  第五關：while 迴圈"),
        ("ENDER09",  ["list"],      "🎒  第六關：串列 List"),
        ("NETHER10", ["function"],  "🔧  第七關：函式 Function"),
        ("DRAGON12", ["mixed"],     "🏆  BOSS關：綜合練習"),
    ]
    table = {_h(code): (chapters, name) for code, chapters, name in _raw}
    del _raw   # 原始代碼從記憶體移除
    return table

UNLOCK_CODES = _build_unlock_table()

# ── 設定 & 存檔 ────────────────────────────────────────────
DEFAULT_CONFIG = {
    "questions_per_chapter": 5,
    "max_lives"            : 3,
    "diamonds_per_correct" : 1,
    "show_explain_on_wrong": True,
}

DEFAULT_SAVE = {
    "player_name"       : "",
    "total_diamonds"    : 0,
    "completed_chapters": [],
    "best_scores"       : {},
    "unlocked_chapters" : ["variables"],   # 第一關預設解鎖
}

def load_json(path, default):
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        # merge any missing keys from default
        for k, v in default.items():
            if k not in data:
                data[k] = v
        return data
    except FileNotFoundError:
        return dict(default)
    except json.JSONDecodeError:
        print(c(f"  ⚠️  {path.name} 格式有誤，使用預設值。", RD))
        return dict(default)

def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def load_config():
    raw = load_json(CONFIG_F, DEFAULT_CONFIG)
    return {k: v for k, v in raw.items() if not k.startswith("_")}

def load_save():
    return load_json(SAVE_F, DEFAULT_SAVE)

def write_save(save):
    save_json(SAVE_F, save)

# ── 載入題庫 ───────────────────────────────────────────────
def load_bank():
    try:
        import question_bank as qb
        return qb.CHAPTERS, qb.CHAPTER_ORDER
    except ImportError:
        print(c("  ❌ 找不到 question_bank.py！請確認檔案在同一個資料夾。", RD))
        sys.exit(1)

# ── UI 元件 ────────────────────────────────────────────────
LOGO = f"""
{GR}  ██╗██████╗ ██╗   ██╗████████╗██╗  ██╗{R}  {YL}⛏  Python 學習冒險  ⛏{R}
{GR}  ██║██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║{R}
{GR}  ██║██████╔╝ ╚████╔╝    ██║   ███████║{R}  {CY}按 1/2/3/4 回答選擇題{R}
{GR}  ██║██╔═══╝   ╚██╔╝     ██║   ██╔══██║{R}  {GY}答錯扣心臟，歸零重來！{R}
{GR}  ██║██║        ██║      ██║   ██║  ██║{R}
{GR}  ╚═╝╚═╝        ╚═╝      ╚═╝   ╚═╝  ╚═╝{R}
"""

def hearts(current, maximum):
    full  = c("❤ " * current,  RD)
    empty = c("♡ " * (maximum - current), GY)
    return full + empty

def draw_header(name, diamonds, lives, max_lives, chapter_title, q_no, q_total):
    print(c("─" * 62, GY))
    print(
        f"  {c(name, WH)}  "
        f"{c('💎', CY)}{c(str(diamonds), YL)}  "
        f"{hearts(lives, max_lives)}"
    )
    print(f"  {c(chapter_title, YL)}  {c(f'題目 {q_no}/{q_total}', GY)}")
    print(c("─" * 62, GY))

# ── 問題渲染 ───────────────────────────────────────────────
CODE_PREFIXES = (
    "def ", "for ", "while ", "if ", "elif ", "else",
    "hp", "bag", "items", "i ", "n ", "name", "total",
    "ores", "count", "level", "dmg", "ore", "num",
    "result", "a ", "b ", "x ", "is_", "has_", "print(",
    "return", "    ", "item", "bag", "sword",
)

def render_question(qdata, q_no, total, chapter_title, player, diamonds,
                    lives, max_lives):
    clear()
    draw_header(player, diamonds, lives, max_lives, chapter_title, q_no, total)
    print()
    lines = qdata["q"].split("\n")
    for line in lines:
        stripped = line.strip()
        if any(stripped.startswith(p) for p in CODE_PREFIXES):
            print(c(f"    {line}", CY))
        else:
            print(f"  {line}")
    print()
    for i, opt in enumerate(qdata["opts"], 1):
        tag = c(f"  [{i}]", YL)
        print(f"{tag} {opt}")
    print()

def get_answer_input():
    while True:
        raw = input(c("  你的答案（1-4）或 0 回主選單：", WH)).strip()
        if raw in ("1", "2", "3", "4"):
            return int(raw)
        if raw == "0":
            return 0
        print(c("  ⚠️  請輸入 1~4，或 0 回主選單！", RD))

# ── 關卡遊玩邏輯 ───────────────────────────────────────────
def play_chapter(chapter_key, chapter_data, config, save):
    title       = chapter_data["title"]
    color_name  = chapter_data.get("color_name", "yellow")
    color       = COLOR_MAP.get(color_name, YL)
    all_qs      = chapter_data["questions"]
    n           = config["questions_per_chapter"]
    max_lives   = config["max_lives"]
    player      = save["player_name"]
    diamonds    = save["total_diamonds"]

    attempt     = 0

    while True:
        attempt += 1
        lives   = max_lives
        correct = 0
        used_qs = []

        # 每次嘗試重新隨機抽題
        pool = all_qs.copy()
        random.shuffle(pool)
        questions = pool[:n]

        # ── 關卡開場 ──────────────────────────────────────
        clear()
        print(c("\n" + "═" * 62, color))
        print(c(f"  {title}", color))
        print(c("═" * 62, color))
        if attempt > 1:
            slow_print(c(f"  第 {attempt} 次挑戰！新題目等著你 🔄", YL))
        print(f"\n  共 {c(str(n), YL)} 題，每題答對得 {c('1 顆鑽石 💎', CY)}")
        print(f"  生命值：{hearts(lives, max_lives)}")
        print(f"  答錯扣一顆心，歸零後重新抽題挑戰")
        print(c("  輸入 0 可隨時回主選單（已得鑽石不會消失）", GY))
        press_enter()

        for idx, q in enumerate(questions, 1):
            # ── 出題 ──────────────────────────────────────
            render_question(q, idx, n, title, player,
                            diamonds, lives, max_lives)
            chosen = get_answer_input()

            if chosen == 0:
                slow_print(c("\n  👋  已離開關卡（已獲得的鑽石保留）", GY), 0.02)
                press_enter()
                return save

            if chosen == q["ans"]:
                # ── 答對 ──────────────────────────────────
                correct   += 1
                diamonds  += config["diamonds_per_correct"]
                save["total_diamonds"] = diamonds
                write_save(save)
                slow_print(c("\n  ✅  正確！獲得一顆鑽石 💎", GR), 0.02)
            else:
                # ── 答錯 ──────────────────────────────────
                lives -= 1
                slow_print(c(f"\n  ❌  答錯了！正確答案是 [{q['ans']}]", RD), 0.02)

            if config.get("show_explain_on_wrong", True) or chosen == q["ans"]:
                print(c(f"  📖 {q['explain']}", GY))

            if lives <= 0 and idx < n:
                # ── 生命歸零，提前結束 ────────────────────
                print(c(f"\n  💀  生命歸零！", RD))
                print(c(f"     答對 {correct}/{idx} 題", GY))
                press_enter("  [ 按 Enter 重新挑戰（新題目）]")
                break
            else:
                press_enter()
        else:
            # ── 通關：跑完所有題目 ────────────────────────
            clear()
            print(c(f"\n  ★  {title}  完成！", YL))
            print(f"  答對：{c(str(correct), GR)} / {n}  "
                  f"剩餘心臟：{hearts(lives, max_lives)}")

            pct = correct / n * 100
            if pct == 100:
                slow_print(c("\n  🏆  完美通關！你是 Minecraft Python 大師！", YL))
            elif pct >= 60:
                slow_print(c(f"\n  👍  {pct:.0f}% 正確，繼續加油！", GR))
            else:
                slow_print(c(f"\n  💪  {pct:.0f}% 正確，多練習就會更強！", RD))

            # 更新最佳紀錄
            prev = save["best_scores"].get(chapter_key, 0)
            if correct > prev:
                save["best_scores"][chapter_key] = correct
            if chapter_key not in save["completed_chapters"]:
                save["completed_chapters"].append(chapter_key)
            write_save(save)
            press_enter()
            return save

        # 生命歸零 → 繼續 while True 重新挑戰

# ── 解鎖碼輸入 ────────────────────────────────────────────
def enter_unlock_code(save):
    clear()
    print(LOGO)
    print(c("  🔓  輸入解鎖碼", YL))
    print(c("  老師上完課後會傳給你一組代碼，輸入後永久解鎖新關卡", GY))
    print(c("  （代碼不分大小寫）", GY))
    print()

    code      = input(c("  解鎖碼：", WH)).strip()
    code_hash = _h(code)

    if code_hash in UNLOCK_CODES:
        chapters_to_unlock, chapter_name = UNLOCK_CODES[code_hash]
        already = all(ch in save["unlocked_chapters"] for ch in chapters_to_unlock)
        if already:
            slow_print(c(f"\n  ℹ️  這個關卡已經解鎖了！", CY))
        else:
            for ch in chapters_to_unlock:
                if ch not in save["unlocked_chapters"]:
                    save["unlocked_chapters"].append(ch)
            write_save(save)
            slow_print(c(f"\n  🎉  解鎖成功！", GR))
            slow_print(c(f"     {chapter_name}  已開放！", YL))
    else:
        slow_print(c(f"\n  ❌  代碼錯誤，請向老師確認", RD))

    press_enter()
    return save

# ── 主選單 ─────────────────────────────────────────────────
def main_menu(chapters, chapter_order, config, save):
    all_keys = [k for k in chapter_order if k in chapters]

    while True:
        # 從 save 讀取已解鎖關卡（而非 config）
        unlocked  = save.get("unlocked_chapters", ["variables"])
        available = [k for k in chapter_order if k in unlocked and k in chapters]
        locked_cnt = len(all_keys) - len(available)

        clear()
        print(LOGO)
        print(c(f"  玩家：{save['player_name']}  "
                f"💎 {save['total_diamonds']}  "
                f"完成：{len(save['completed_chapters'])}/{len(available)} 關",
                YL))
        print()
        print(c("  ╔══════════════════════════════════════════╗", GY))
        print(c("  ║             選擇關卡                     ║", GY))
        print(c("  ╠══════════════════════════════════════════╣", GY))

        for i, key in enumerate(available, 1):
            t     = chapters[key]["title"]
            done  = "✓" if key in save["completed_chapters"] else " "
            best  = save["best_scores"].get(key, 0)
            n     = config["questions_per_chapter"]
            score = f"{best}/{n}" if key in save["best_scores"] else "---"
            line  = f"  ║  [{i}] {done} {t:<34} {score} ║"
            col   = GR if done == "✓" else WH
            print(c(line, col))

        print(c("  ╠══════════════════════════════════════════╣", GY))
        if len(available) > 1:
            print(c("  ║  [9] 🎲 隨機挑戰！                       ║", GY))
        print(c("  ║  [U] 🔓 輸入老師給的解鎖碼                ║", CY))
        print(c("  ║  [0] 離開遊戲                             ║", GY))
        print(c("  ╚══════════════════════════════════════════╝", GY))

        if locked_cnt > 0:
            print(c(f"  （還有 {locked_cnt} 個關卡等待解鎖，繼續上課加油！）", GY))

        choice = input(c("\n  你的選擇：", WH)).strip().upper()

        if choice == "0":
            break
        elif choice == "U":
            save = enter_unlock_code(save)
        elif choice == "9" and len(available) > 1:
            key  = random.choice(available)
            save = play_chapter(key, chapters[key], config, save)
        elif choice.isdigit() and 1 <= int(choice) <= len(available):
            key  = available[int(choice) - 1]
            save = play_chapter(key, chapters[key], config, save)
        else:
            print(c("  ⚠️  無效的選擇！", RD))
            time.sleep(0.8)

# ── 新玩家設定 ─────────────────────────────────────────────
def setup_new_player(save):
    clear()
    print(LOGO)
    slow_print(c("  歡迎來到 Minecraft Python 學習冒險！", GR))
    slow_print(c("  答對題目收集鑽石 💎，挑戰所有關卡！", YL))
    print()
    name = input(c("  請輸入你的角色名稱：", WH)).strip()
    save["player_name"] = name if name else "Steve"
    write_save(save)
    return save

# ── 遊戲結束畫面 ───────────────────────────────────────────
def show_end_screen(save, total_possible):
    clear()
    print(LOGO)
    d   = save["total_diamonds"]
    pct = d / max(total_possible, 1) * 100
    print(c(f"\n  {save['player_name']} 的冒險結束！", YL))
    print(f"\n  累積鑽石：{c(str(d), CY)} 顆")
    print(f"  完成關卡：{c(str(len(save['completed_chapters'])), GR)} 關")
    if pct >= 80:
        slow_print(c("\n  🏆  你是真正的 Minecraft Python 大師！", YL))
    elif pct >= 50:
        slow_print(c("\n  ⭐  很棒！繼續練習就能打敗末影龍！", GR))
    else:
        slow_print(c("\n  💪  加油！每次練習都讓你更強！", RD))
    print(c("\n  再見！⛏️\n", GY))

# ── 主程式 ─────────────────────────────────────────────────
def main():
    chapters, chapter_order = load_bank()
    config  = load_config()
    save    = load_save()

    # 計算題庫總鑽石上限（所有題目數）
    total_possible = sum(
        len(chapters[k]["questions"])
        for k in chapter_order if k in chapters
    )

    if not save["player_name"]:
        save = setup_new_player(save)
    else:
        clear()
        print(LOGO)
        slow_print(c(f"  歡迎回來，{save['player_name']}！", YL), 0.02)
        time.sleep(0.4)

    main_menu(chapters, chapter_order, config, save)
    show_end_screen(save, total_possible)

if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print(c("\n\n  遊戲中斷，再見！⛏️\n", GY))
        sys.exit(0)
