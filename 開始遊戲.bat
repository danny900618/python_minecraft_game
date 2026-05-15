@echo off
chcp 65001 >nul
title ⛏  Minecraft Python 學習遊戲
cd /d "%~dp0"

:: 檢查 Python 是否安裝
python --version >nul 2>&1
if errorlevel 1 (
    cls
    echo.
    echo  ============================================
    echo    Python 尚未安裝！
    echo  ============================================
    echo.
    echo    請先到以下網址下載並安裝 Python：
    echo    https://www.python.org/downloads/
    echo.
    echo    安裝時記得勾選「Add Python to PATH」！
    echo.
    echo  ============================================
    echo.
    pause
    exit
)

:: 檢查 question_bank.py 是否存在
if not exist "question_bank.py" (
    cls
    echo.
    echo  ============================================
    echo    找不到遊戲檔案！
    echo  ============================================
    echo.
    echo    請確認以下檔案都在同一個資料夾：
    echo      - minecraft_quiz.py
    echo      - question_bank.py
    echo      - game_config.json
    echo.
    echo  ============================================
    echo.
    pause
    exit
)

:start
cls
python minecraft_quiz.py

echo.
echo  ==============================
echo    遊戲已結束
echo  ==============================
echo.
echo    按 R 重新開始，其他鍵離開...
choice /c RC /n >nul
if errorlevel 2 exit
if errorlevel 1 goto start
