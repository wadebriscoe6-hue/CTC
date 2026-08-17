@echo off
title Cloth Talk AI - OpusClip & Jarvis Suite (Desktop Server)
color 0A

echo =======================================================================
echo   💎 CLOTH TALK AI & OPUSCLIP SUITE - 1-CLICK DESKTOP LAUNCHER
echo   Branded for @clothtalk88 | Jarvis Diamond Protocol & Matrix Engine
echo =======================================================================
echo.

python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] Python is not detected in your PATH.
    echo     Please install Python 3.10+ from https://www.python.org/downloads/
    pause
    exit /b
)

if not exist ".venv" (
    echo [*] Setting up isolated Python virtual environment (.venv)...
    python -m venv .venv
)

call .venv\Scripts\activate.bat
pip install -r requirements.txt --quiet --disable-pip-version-check

python test_stability.py

streamlit run app.py --server.port 8501 --server.headless false
pause