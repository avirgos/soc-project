# ip-analyzer-from-splunk-query

## (OPTIONNEL) Recherche Splunk automatique

- Installer Ansible :

```bash
sudo apt-get install python3-pip python3-venv
python3 -m venv ansible-env
source ansible-env/bin/activate
pip install ansible
```

⚠️ Dans le playbook ```auto_splunk_query.yml``` vous devez compléter les valeur des variables ```username``` et ```password``` concernant votre compte Splunk. ⚠️

- Exécution du playbook Ansible 

```bash
ansible-playbook auto_splunk_query.yml
```

Lees résultats de la recherche sont stockés dans le répertoire ```queries/```.

## Utilisation

⚠️ Vous devez disposer d'une clé API [AbuseIPDB](https://www.abuseipdb.com) en crééant un compte. Puis, dans le script ```ip-analyzer-from-splunk-query.py``` vous devez compléter la valeur de la variable ```API_KEY```. ⚠️

```bash
python3 ip-analyzer-from-splunk-query.py queries/<splunk-query-json-file>
```

Une fois le fichier ```malicious-ips.csv``` obtenu, importez ce fichier dans Splunk Enterprise en tant que **lookup table** :

![add-lookup-table](assets/add-lookup-table.png)

Pour mettre à jour le fichier ```malicious-ips.csv```, supprimer la **lookup table** et importez le fichier de nouveau.

Dans cette même liste, des adresses IPs malveillantes ont été ajoutées de base au travers de cette liste : https://snort-org-site.s3.amazonaws.com/production/document_files/files/000/034/548/original/ip-filter.blf.