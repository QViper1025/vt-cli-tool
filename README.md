# vt-cli-tool

vt-cli tool is a python scan tool with most features of TotalVirus that utilizes the TotalVirus API.

## Installation

To install dependencies, run:

- For Windows: `install_dependencies.bat`
- For Linux/Mac: `install_dependencies.sh`

## Configuration

Make sure to provide your API key in the `API_KEY.json` file.

## Usage

# VirusTotal CLI Tool

A powerful command-line interface for interacting with VirusTotal API v3. Scan files, URLs, domains, and IP addresses with 70+ antivirus products.

## Features

- 🔍 **Upload files for scanning** - Analyze files with VirusTotal's 70+ detection engines
- 📊 **Get file reports by hash** - Query MD5, SHA1, or SHA256 hashes
- 🌐 **Scan URLs** - Analyze URLs for malicious content
- 📄 **Get URL reports** - Retrieve detailed analysis for URLs
- 🔗 **Get domain reports** - Analyze domain reputation
- 🖥️ **Get IP reports** - Check IP address threats
- 🔐 **Automatic hash calculation** - Calculate MD5, SHA1, and SHA256 hashes

## Installation

### Windows
```bash
install_dependencies.bat
```

### Linux / Mac
```bash
chmod +x install_dependencies.sh
./install_dependencies.sh
```

Or install manually:
```bash
pip install vt-py
```

## Setup

1. Get your VirusTotal API key from [virustotal.com](https://www.virustotal.com/gui/home/upload)
2. Create `API_KEY.json` in the same directory:
```json
{
  "api_key": "YOUR_API_KEY_HERE"
}
```

3. Run the tool:
```bash
python vt_cli.py
```

## Usage

The CLI provides an interactive menu with 6 main options:

### 1. Upload a file for scanning
- Analyze your file with 70+ antivirus products
- Automatically calculates MD5, SHA1, and SHA256 hashes
- Provides analysis ID and status

### 2. Get a file report by hash
- Query reports using MD5, SHA1, or SHA256 hash
- Returns file information and threat analysis
- Shows malicious, suspicious, and undetected counts

### 3. Scan URL
- Submit URLs for scanning
- Leverages 70+ antivirus products
- Returns analysis ID for tracking

### 4. Get a URL analysis report
- Retrieve detailed analysis for previously scanned URLs
- Shows threat reputation and context
- Displays detection counts from security tools

### 5. Get a domain report
- Analyze domain reputation
- Check domain threat status
- View security tool detections

### 6. Get an IP address report
- Check IP address threats
- Retrieve IP reputation analysis
- View detection counts and threat context

## File Hash Support

The tool automatically calculates three types of hashes using efficient stream-based processing:

- **MD5** - 128-bit hash (legacy support)
- **SHA1** - 160-bit hash (legacy support)
- **SHA256** - 256-bit hash (recommended)

Hashes are calculated without loading entire files into memory, making it efficient for large files.

## Requirements

- Python 3.6 or higher
- vt-py library (installed via setup script)
- Valid VirusTotal API key
- Internet connection

## API Key

You can obtain your VirusTotal API key by:

1. Visiting [virustotal.com](https://www.virustotal.com/)
2. Signing up or logging in to your account
3. Going to your account settings
4. Finding your API key in the profile section
5. Pasting it into `API_KEY.json`

## Error Handling

The tool includes comprehensive error handling for:
- Missing or invalid API keys
- Network errors
- Invalid file paths
- API rate limiting
- File not found errors

## License

This tool is provided as-is for educational and security purposes.

## Disclaimer

This is an unofficial tool. Always ensure you have proper authorization before scanning files, URLs, or systems. VirusTotal is a service by Google/Alphabet Inc.
