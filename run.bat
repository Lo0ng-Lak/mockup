@echo off
REM Tool Mockup Ao - chay bang Python (server local tach ao bang AI)
cd /d %~dp0

where python >nul 2>nul
if errorlevel 1 (
  echo [LOI] Chua thay Python tren may. Cai Python 3.10+ tu python.org,
  echo nho tick o "Add python.exe to PATH" khi cai, roi chay lai file nay.
  pause
  exit /b 1
)

if not exist venv\Scripts\python.exe (
  echo Lan dau chay: dang tao moi truong va cai thu vien, se mat vai phut...
  python -m venv venv
  venv\Scripts\python.exe -m pip install --upgrade pip
  venv\Scripts\python.exe -m pip install -r requirements.txt
  echo Cai dat xong.
)

echo Dang khoi dong tool... trinh duyet se tu mo http://localhost:8765
echo De nguyen cua so nay khi dang dung tool. Dong cua so = tat tool.
venv\Scripts\python.exe app.py
pause
