# ip_analyzer_from_splunk_query

## Prérequis

- Installer Ansible :

```bash
sudo apt-get install python3-pip python3-venv
python3 -m venv ansible-env
source ansible-env/bin/activate
pip install ansible
```

**⚠️ Dans le playbook Ansible ```auto_splunk_query.yml```, vous devez compléter les valeur des variables ```username``` et ```password``` concernant votre compte Splunk. ⚠️**

**⚠️ Dans le script Python ```ip_analyzer_from_splunk_query.py```, vous devez disposer d'une clé API [AbuseIPDB](https://www.abuseipdb.com) en crééant un compte. Puis, dans le script ```ip_analyzer_from_splunk_query.py``` vous devez compléter la valeur de la variable ```API_KEY```. ⚠️**

**⚠️ Dans le script Bash ```run-ip-analyzer-from-splunk-query.sh```,  complétez la variable globale ```PATH_TO_SOC_PROJECT``` pour correspondre à l'emplacement où se trouve le répertoire ```soc-project```. ⚠️**

## Utilisation

Exécutez ```run-ip-analyzer-from-splunk-query.sh``` : 

```bash
./run-ip_analyzer_from_splunk_query.sh
```

Le playbook Ansible `auto_splunk_query.yml` va s'exécuter pour lancer la requête Splunk pour obtenir les adresses IPs qui se sont connectés à des hôtes distants. Les résultats de cette requête se situent dans le répertoire `queries/`.

Puis, le script Bash va exécuter le script Python `ip_analyzer_from_splunk_query` pour déterminer lesquelles des adresses IPs obtenues sont malveillantes.

Au final, les adresses IPs malveillantes sont stockées dans le fichier `malicious-ips.csv`.

## Ajouter/modifier ```malicious-ips.csv``` dans Splunk

Une fois le fichier ```malicious-ips.csv``` obtenu, importez ce fichier dans Splunk Enterprise en tant que **lookup table** :

![add-lookup-table](assets/add-lookup-table.png)

Pour mettre à jour le fichier ```malicious-ips.csv```, supprimer la **lookup table** et importez le fichier de nouveau.

Dans cette même liste, des adresses IPs malveillantes ont été ajoutées de base au travers de cette liste : https://snort-org-site.s3.amazonaws.com/production/document_files/files/000/034/548/original/ip-filter.blf.
