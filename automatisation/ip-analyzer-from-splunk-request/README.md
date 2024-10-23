# ip-analyzer-from-splunk-request

Dépendances :

- AbuseIPDB
- Splunk Enterprise Security

Requête Splunk utilisée :

```
index="connectix" sourcetype="suricata" earliest=-24h
| stats count by dest_ip, dest_port
| where NOT cidrmatch("192.168.10.0/24", dest_ip)
| sort - count
```

Exécution :

```py
python3 ip-analyzer-from-splunk-request.py
```

Une fois le fichier ```malicious-ips.csv``` obtenu ou mis à jour, importez ce fichier dans Splunk Enterprise en tant que **lookup table** :

![add-lookup-table](assets/add-lookup-table.png)