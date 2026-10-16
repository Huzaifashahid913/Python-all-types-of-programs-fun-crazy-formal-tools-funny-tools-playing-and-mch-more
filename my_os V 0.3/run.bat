@echo off
setlocal
cd /d "%~dp0"
chcp 65001 >nul
title Huzaifa MyOS V 0.3

py -3 --version >nul 2>nul
if not errorlevel 1 goto use_py
python --version >nul 2>nul
if errorlevel 1 goto no_python
python myos.py
goto finished

:use_py
py -3 myos.py
goto finished

:no_python
echo Python 3 was not found.
echo Install Python from https://www.python.org/downloads/
echo During setup, enable "Add Python to PATH".
pause
exit /b 1

:finished
echo.
echo MyOS has closed.
pause
endlocal
