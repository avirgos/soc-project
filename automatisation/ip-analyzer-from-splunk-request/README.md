# ip-analyzer-from-splunk-request

- AbuseIPDB
- Splunk Enterprise Security

Requête Splunk utilisée :

```
index="connectix" sourcetype="suricata" earliest=-24h
| stats count by dest_ip, dest_port
| where NOT cidrmatch("192.168.10.0/24", dest_ip)
| sort - count
```

```py
python3 ip-analyzer-from-splunk-request.py
```