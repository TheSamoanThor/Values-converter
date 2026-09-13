@echo off
chcp 65001 >nul
cd /d "%~dp0"

pytest test_temperature.py -v ^
    --cov=converter.temperature ^
    --cov=converter.helpers ^
    --cov-report=term-missing ^
    --cov-report=html

pause