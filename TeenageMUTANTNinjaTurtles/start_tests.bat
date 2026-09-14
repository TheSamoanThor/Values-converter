chcp 65001 >nul
cd /d "%~dp0"

set PYTHONIOENCODING=utf-8
set PYTHONUTF8=1

if exist "session.sqlite" del /f /q "session.sqlite"

cosmic-ray init config.toml session.sqlite
cosmic-ray exec config.toml session.sqlite
cr-report session.sqlite > cosmic-ray-report.txt
cr-html session.sqlite > cosmic-ray.html

start "" cosmic-ray.html
pause