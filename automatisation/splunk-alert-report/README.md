# splunk-alert-report

## Prérequis

```bash
sudo apt-get install python3-pip python3-venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**⚠️ Dans le script Python ```splunk_alert_report.py```, vous devez compléter la valeur de la variable `SPLUNK_USERNAME` et `SPLUNK_PASSWORD` avec vos identifiants Splunk pour pouvoir se connecter à l'instance. Pour l'envoi de mails depuis Gmail, il faut compléter la valeur de la variable `SENDER_PASSWORD`. ⚠️**

## Utilisation

Exécutez ```splunk_alert_report.py``` :

```bash
python3 splunk_alert_report.py
```

Ce script est en charge de se connecter à l'instance Splunk et de récupérer toutes les données concernant les alertes de sévérité **"High"** ayant été déclenchées. Les données obtenues se situent dans le répertoire `splunk-alerts/`.

Puis, le script Python réalise un tri pour n'obtenir que celles datant d'aujourd'hui.

Au final, on obtient ces alertes au format Markdown dans un template Jinja et celles-ci sont envoyées par mail aux destinataires indiqués dans la variable `RECIPIENT_EMAILS`.