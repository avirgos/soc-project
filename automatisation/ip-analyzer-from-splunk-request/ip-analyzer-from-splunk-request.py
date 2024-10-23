import json
import requests
import csv

INPUT_JSON_FILE = "example-request-splunk-23-10-2024.json"
OUTPUT_CSV_FILE = "malicious-ips.csv"
API_KEY = '<abuse-ipdb-api-key>'

headers = {
    'Key': API_KEY,
    'Accept': 'application/json'
}

def check_ip(ip):
    url = f'https://api.abuseipdb.com/api/v2/check'
    params = {
        "ipAddress": ip,
        "maxAgeInDays": 90  # 90-day check
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    if 'data' in data:
        return data['data']['abuseConfidenceScore'], data['data']['totalReports']
    else:
        return None, None

# read INPUT_JSON_FILE
with open(INPUT_JSON_FILE) as f:
    data = [json.loads(line) for line in f]

# extract IP addresses
ip_list = [entry['result']['dest_ip'] for entry in data]

# read IPs already present in the OUTPUT_CSV_FILE file
try:
    with open(OUTPUT_CSV_FILE, "r") as f:
        reader = csv.reader(f)
        existing_ips = {row[0] for row in reader if row}
except FileNotFoundError:
    existing_ips = set()

# verify each IP address
malicious_ips = []

for ip in ip_list:
    score, reports = check_ip(ip)

    if score is not None:
        print(f"IP : {ip} | Score : {score}% | Reports : {reports}")

        if score > 0:
            print(f"⚠️  The IP address {ip} is malicious !")

            if ip not in existing_ips:
                malicious_ips.append(ip)
    else:
        print(f"IP : {ip} | No data available.")

# new potential malicious IP to add
if malicious_ips:
    with open(OUTPUT_CSV_FILE, "a", newline='') as csvfile:
        csv_writer = csv.writer(csvfile)

        # if file is empty, add the header
        if not existing_ips:
            csv_writer.writerow(["ip"])

        # add new malicious IPs to the CSV file
        for ip in malicious_ips:
            csv_writer.writerow([ip])

    print(f"\nMalicious IP addresses have been recorded in {OUTPUT_CSV_FILE}.")
else:
    print("\nNo new malicious IP addresses to record.")