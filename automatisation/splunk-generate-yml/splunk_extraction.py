import requests
import yaml
import os

splunk_url = "https://172.10.80.212:8089"
username = "username"
password = "mdp"
output_folder = "splunk_rules_yml"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

def get_splunk_rules():
    url = f"{splunk_url}/servicesNS/admin/search/saved/searches?output_mode=json"
    response = requests.get(url, auth=(username, password), verify=False)
    if response.status_code == 200:
        return response.json().get("entry", [])
    else:
        print("Erreur lors de la récupération des règles:", response.status_code)
        return []

def save_rule_as_yaml(rule):
    rule_name = rule["name"]
    alert_event = rule.get("content", {}).get("action.email.subject", "Unnamed_Event")
    
    filename = f"{output_folder}/{rule_name}_{alert_event}.yml".replace(" ", "_").replace("/", "_")
    
    rule_yaml = {
        "name": rule_name,
        "alert_event": alert_event,
        "search": rule.get("content", {}).get("search", ""),
        "description": rule.get("content", {}).get("description", ""),
        "alert_type": rule.get("content", {}).get("alert_type", "")
    }

    with open(filename, 'w') as file:
        yaml.dump(rule_yaml, file, default_flow_style=False)
    print(f"Règle enregistrée : {filename}")

rules = get_splunk_rules()
for rule in rules:
    save_rule_as_yaml(rule)

print("Extraction terminée.")
