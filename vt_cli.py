# vt_cli.py
#!/usr/bin/env python3
"""
VirusTotal CLI Tool - Interactive command-line interface for VirusTotal API
"""

import json
import os
import sys
import hashlib
import vt

# Load API key from config file
def load_api_key():
    if not os.path.exists('API_KEY.json'):
        print("❌ Error: API_KEY.json not found!")
        print("Please create API_KEY.json with your VirusTotal API key.")
        sys.exit(1)
    
    try:
        with open('API_KEY.json', 'r') as f:
            config = json.load(f)
            return config.get('api_key')
    except Exception as e:
        print(f"❌ Error reading API_KEY.json: {e}")
        sys.exit(1)

# Calculate file hashes
def calculate_file_hashes(file_path):
    """Calculate MD5, SHA1, and SHA256 hashes for a file"""
    try:
        with open(file_path, "rb") as f:
            # Get MD5
            md5_hash = hashlib.file_digest(f, "md5").hexdigest()
            
            # Reset file pointer for next hash
            f.seek(0)
            
            # Get SHA1
            sha1_hash = hashlib.file_digest(f, "sha1").hexdigest()
            
            f.seek(0)
            
            # Get SHA256
            sha256_hash = hashlib.file_digest(f, "sha256").hexdigest()
            
        return {
            'md5': md5_hash,
            'sha1': sha1_hash,
            'sha256': sha256_hash
        }
    except FileNotFoundError:
        print(f"❌ Error: File '{file_path}' not found!")
        return None
    except Exception as e:
        print(f"❌ Error calculating hashes: {e}")
        return None

# Display menu
def display_menu():
    print("\n" + "="*60)
    print("VirusTotal API CLI Tool - Most Popular Endpoints")
    print("="*60)
    print("\n1. Upload a file for scanning")
    print("   → Analyze your file with 70+ antivirus products")
    print("\n2. Get a file report by hash")
    print("   → Provide md5, sha1, or sha256 hash")
    print("\n3. Scan URL")
    print("   → Analyze URL with 70+ antivirus products")
    print("\n4. Get a URL analysis report")
    print("   → Retrieve analysis report for a URL")
    print("\n5. Get a domain report")
    print("   → Retrieve domain analysis report")
    print("\n6. Get an IP address report")
    print("   → Retrieve IP address analysis report")
    print("\n0. Exit")
    print("="*60)

# Main API operations
def upload_file(client, file_path):
    """Upload a file for scanning"""
    if not os.path.exists(file_path):
        print(f"❌ Error: File '{file_path}' not found!")
        return
    
    try:
        print(f"\n⏳ Uploading file: {file_path}...")
        with open(file_path, "rb") as f:
            analysis = client.scan_file(f)
        print(f"✅ File uploaded successfully!")
        print(f"   Analysis ID: {analysis.id}")
        print(f"   Status: {analysis.status}")
    except Exception as e:
        print(f"❌ Error uploading file: {e}")

def get_file_report(client, file_hash):
    """Get report for a file by hash"""
    try:
        print(f"\n⏳ Fetching report for hash: {file_hash}...")
        file_obj = client.get_object(f"/files/{file_hash}")
        
        print(f"\n✅ File Report Found!")
        print(f"   Name: {file_obj.meaningful_name}")
        print(f"   Size: {file_obj.size} bytes")
        print(f"   Type: {file_obj.type_description}")
        
        # Display threat analysis
        last_analysis = file_obj.last_analysis_stats
        if last_analysis:
            print(f"\n   Threat Analysis:")
            print(f"   - Malicious: {last_analysis.get('malicious', 0)}")
            print(f"   - Suspicious: {last_analysis.get('suspicious', 0)}")
            print(f"   - Undetected: {last_analysis.get('undetected', 0)}")
    except vt.NotFoundError:
        print(f"❌ File not found in VirusTotal database")
    except Exception as e:
        print(f"❌ Error fetching file report: {e}")

def scan_url(client, url):
    """Scan a URL"""
    try:
        print(f"\n⏳ Scanning URL: {url}...")
        analysis = client.scan_url(url)
        print(f"✅ URL submitted for scanning!")
        print(f"   Analysis ID: {analysis.id}")
        print(f"   Status: {analysis.status}")
    except Exception as e:
        print(f"❌ Error scanning URL: {e}")

def get_url_report(client, url):
    """Get report for a URL"""
    try:
        print(f"\n⏳ Fetching report for URL: {url}...")
        url_obj = client.get_object(f"/urls/{vt.url_id(url)}")
        
        print(f"\n✅ URL Report Found!")
        print(f"   URL: {url_obj.last_final_url}")
        
        # Display threat analysis
        last_analysis = url_obj.last_analysis_stats
        if last_analysis:
            print(f"\n   Threat Analysis:")
            print(f"   - Malicious: {last_analysis.get('malicious', 0)}")
            print(f"   - Suspicious: {last_analysis.get('suspicious', 0)}")
            print(f"   - Undetected: {last_analysis.get('undetected', 0)}")
    except vt.NotFoundError:
        print(f"❌ URL not found in VirusTotal database")
    except Exception as e:
        print(f"❌ Error fetching URL report: {e}")

def get_domain_report(client, domain):
    """Get report for a domain"""
    try:
        print(f"\n⏳ Fetching report for domain: {domain}...")
        domain_obj = client.get_object(f"/domains/{domain}")
        
        print(f"\n✅ Domain Report Found!")
        print(f"   Domain: {domain_obj.id}")
        
        # Display threat analysis
        last_analysis = domain_obj.last_analysis_stats
        if last_analysis:
            print(f"\n   Threat Analysis:")
            print(f"   - Malicious: {last_analysis.get('malicious', 0)}")
            print(f"   - Suspicious: {last_analysis.get('suspicious', 0)}")
            print(f"   - Undetected: {last_analysis.get('undetected', 0)}")
    except vt.NotFoundError:
        print(f"❌ Domain not found in VirusTotal database")
    except Exception as e:
        print(f"❌ Error fetching domain report: {e}")

def get_ip_report(client, ip):
    """Get report for an IP address"""
    try:
        print(f"\n⏳ Fetching report for IP: {ip}...")
        ip_obj = client.get_object(f"/ip_addresses/{ip}")
        
        print(f"\n✅ IP Report Found!")
        print(f"   IP: {ip_obj.id}")
        
        # Display threat analysis
        last_analysis = ip_obj.last_analysis_stats
        if last_analysis:
            print(f"\n   Threat Analysis:")
            print(f"   - Malicious: {last_analysis.get('malicious', 0)}")
            print(f"   - Suspicious: {last_analysis.get('suspicious', 0)}")
            print(f"   - Undetected: {last_analysis.get('undetected', 0)}")
    except vt.NotFoundError:
        print(f"❌ IP not found in VirusTotal database")
    except Exception as e:
        print(f"❌ Error fetching IP report: {e}")

def main():
    # Load API key
    api_key = load_api_key()
    
    # Create VirusTotal client
    try:
        client = vt.Client(api_key)
    except Exception as e:
        print(f"❌ Error initializing VirusTotal client: {e}")
        sys.exit(1)
    
    try:
        while True:
            display_menu()
            choice = input("\nEnter your choice (0-6): ").strip()
            
            if choice == '0':
                print("\n👋 Goodbye!")
                break
            
            elif choice == '1':
                file_path = input("\nEnter file path: ").strip()
                hashes = calculate_file_hashes(file_path)
                if hashes:
                    print(f"\n📊 File Hashes:")
                    print(f"   MD5:    {hashes['md5']}")
                    print(f"   SHA1:   {hashes['sha1']}")
                    print(f"   SHA256: {hashes['sha256']}")
                upload_file(client, file_path)
            
            elif choice == '2':
                file_hash = input("\nEnter file hash (MD5, SHA1, or SHA256): ").strip()
                get_file_report(client, file_hash)
            
            elif choice == '3':
                url = input("\nEnter URL to scan: ").strip()
                scan_url(client, url)
            
            elif choice == '4':
                url = input("\nEnter URL: ").strip()
                get_url_report(client, url)
            
            elif choice == '5':
                domain = input("\nEnter domain: ").strip()
                get_domain_report(client, domain)
            
            elif choice == '6':
                ip = input("\nEnter IP address: ").strip()
                get_ip_report(client, ip)
            
            else:
                print("\n❌ Invalid choice. Please enter a number between 0 and 6.")
    
    except KeyboardInterrupt:
        print("\n\n👋 Interrupted by user. Goodbye!")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
    finally:
        client.close()

if __name__ == '__main__':
    main()
