import splunklib.client as client
import json
from jinja2 import Template
from datetime import datetime

# Connexion à Splunk
service = client.connect(
    host='172.10.80.212',
    port='8089',
    scheme='https',
    username='<username>',
    password='<password>'
)

# Requête de recherche Splunk
search_query = 'search index="alerts" event_title="*"'

try:
    # Envoi de la requête de recherche à Splunk
    search_results = service.jobs.oneshot(search_query, output_mode='json')

    # Récupération des résultats de la recherche au format JSON
    jsout = json.loads(search_results.read())

    # Enregistrement des résultats dans un fichier JSON
    json_formatted_str = json.dumps(jsout, indent=2)

    with open('alerts-data.json', 'w') as f:
        f.write(json_formatted_str)

    # Modèle de bulletin d'alerte en Markdown
    template = """
    {% for result in results %}
    # Alerte : {{ result['event_title'] }}
    Source : **{{ result['source'] }}**
    Horodatage : {{ result['_time'] | to_datetime }}
    Instance Splunk : {{ result['host'] }}
    {% endfor %}
    """

    # Fonction pour convertir le timestamp ISO en datetime formaté
    def to_datetime(timestamp):
        return datetime.fromisoformat(timestamp).strftime('%Y-%m-%d %H:%M:%S')

    # Enregistrement du filtre pour Jinja2
    Template.filters['to_datetime'] = to_datetime

    jinja_template = Template(template)
    
    # Rendu du modèle avec les résultats
    print(jinja_template.render(results=jsout['results']))

except Exception as e:
    print(f"Une erreur est survenue : {e}")
finally:
    service.logout()