import requests
import json 
import sys
import os 
from dotenv import load_dotenv

#Loading variables from .env file 
load_dotenv()

#If the key isn't found, the script can safely fail or return to none :) 
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    print("Error! API Key not found")
    sys.exit(1)

URL = 'https://api.abuseipdb.com/api/v2/check'

def check_ip(ip_address):
    headers = {
        'Key': API_KEY,
        'Accept': 'application/json',
    }

    #data we want to send to the API

    query_string = {
        'ipAddress': ip_address,
        'maxAgeInDays': '120', #cheking the last 120 days of history 
        'verbose': True, # request for more detailed response 
    }

    print(f"[*] Checking IP reputation for {ip_address}...")

    try:
        response = requests.get(URL, headers=headers, params=query_string)

        #200 status code means teh server says "OK"

        if response.status_code == 200:
            data = response.json()['data']

            #extracting the essential information we need
            ip = data['ipAddress']
            score = data['abuseConfidenceScore'] #range - 1-100
            isp = data['isp']
            country = data['countryName']
            total_reports = data['totalReports']

            #printing the results
            print("\n" + "=" * 40)
            print(f"Report for: {ip}")
            print("=" * 40)
            print(f"ISP: {isp}")
            print(f"Country: {country}")
            print(f"Total Reports: {total_reports}")
            print(f"Risk Score: {score}")
            print("-" * 40)

            # Simple logic to determine if we should be worried
            if score > 0:
                print("[!] ALERT: This IP is flagged as malicious!")
            else:
                print("[+] CLEAN: No malicious activity reported.")
            print("=" * 40 + "\n")
            
        elif response.status_code == 401:
            print("[!] Error: Authentication failed. Check your API Key in .env")
        elif response.status_code == 429:
            print("[!] Error: You have exceeded your daily API limit.")
        else:
            print(f"[!] Error: Server returned status code {response.status_code}")

    except Exception as e:
        print(f"[!] Critical Error: {e}")

# This block allows you to run the script from the terminal
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python ip_check.py <IP_ADDRESS>")
    else:
        target_ip = sys.argv[1]
        check_ip(target_ip)