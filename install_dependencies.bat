@echo off
REM VirusTotal CLI Tool - Dependency Installer for Windows
REM This script installs all required Python packages with a progress bar

setlocal enabledelayedexpansion

title VirusTotal CLI Tool - Installing Dependencies

echo.
echo ========================================
echo VirusTotal CLI Tool - Setup
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH
    echo Please install Python from https://www.python.org
    pause
    exit /b 1
)

echo [SUCCESS] Python detected:
python --version
echo.

REM Install vt-py package with progress bar
echo Installing vt-py...
echo.

cls
echo ========================================
echo VirusTotal CLI Tool - Setup
echo ========================================
echo.
echo Installing: vt-py
echo.
echo Progress: 50%%
echo [#########################           ]
echo.

pip install vt-py

if errorlevel 1 (
    echo.
    echo [ERROR] Failed to install vt-py
    pause
    exit /b 1
)

REM Final success screen
cls
echo ========================================
echo VirusTotal CLI Tool - Setup
echo ========================================
echo.
echo [###########################] 100%%
echo.
echo [SUCCESS] All dependencies installed!
echo.
echo Next steps:
echo 1. Create API_KEY.json with your VirusTotal API key
echo 2. Run: python vt_cli.py
echo.
pause
