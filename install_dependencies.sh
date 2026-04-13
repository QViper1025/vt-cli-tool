#!/bin/bash

# VirusTotal CLI Tool - Dependency Installer for Linux/Mac
# This script installs all required Python packages with a progress bar

clear

echo "========================================"
echo "VirusTotal CLI Tool - Setup"
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] Python 3 is not installed"
    echo "Please install Python 3 from https://www.python.org"
    exit 1
fi

echo "[SUCCESS] Python detected:"
python3 --version
echo ""

# Install vt-py package
echo "Installing vt-py..."
echo ""

clear
echo "========================================"
echo "VirusTotal CLI Tool - Setup"
echo "========================================"
echo ""
echo "Installing: vt-py"
echo ""
echo "Progress: 50%"
printf "["
for ((i = 0; i < 13; i++)); do
    printf "#"
done
for ((i = 13; i < 20; i++)); do
    printf " "
done
printf "]\n"
echo ""

# Install the package
pip3 install vt-py

if [ $? -ne 0 ]; then
    echo ""
    echo "[ERROR] Failed to install vt-py"
    exit 1
fi

# Final success screen
clear
echo "========================================"
echo "VirusTotal CLI Tool - Setup"
echo "========================================"
echo ""
echo "[####################] 100%"
echo ""
echo "[SUCCESS] All dependencies installed!"
echo ""
echo "Next steps:"
echo "1. Create API_KEY.json with your VirusTotal API key"
echo "2. Run: python3 vt_cli.py"
echo ""
