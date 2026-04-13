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
    echo "Please install Python 3 from https://www.python.org/"
    exit 1
fi

echo "[SUCCESS] Python detected:"
python3 --version
echo ""

# Array of dependencies
packages=("vt-py")
total=${#packages[@]}
current=0

echo "Installing dependencies..."
echo ""

# Install each package
for package in "${packages[@]}"; do
    ((current++))
    percent=$((current * 100 / total))
    
    # Draw progress bar
    clear
    echo "========================================"
    echo "VirusTotal CLI Tool - Setup"
    echo "========================================"
    echo ""
    echo "Installing: $package"
    echo ""
    echo "Progress: $percent%"
    printf "["
    for ((i = 0; i < percent / 5; i++)); do
        printf "#"
    done
    for ((i = percent / 5; i < 20; i++)); do
        printf " "
    done
    printf "]\n"
    echo ""
    
    # Install the package silently
    pip3 install "$package" -q 2>/dev/null
    
    if [ $? -ne 0 ]; then
        echo ""
        echo "[ERROR] Failed to install $package"
        exit 1
    fi
done

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
