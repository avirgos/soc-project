import splunklib.client as client
import json
from jinja2 import Environment
from datetime import datetime
import os

# connect to Splunk instance
service = client.connect(
    host='172.10.80.212',
    port='8089',
    scheme='https',
    username='<username>',
    password='<password>'
)

# Splunk search query to retrieve only "High" severity alerts
search_query = 'search index="alerts" event.event_title="*" event.impact="high"'

# convert ISO timestamp to formatted datetime
def to_datetime(timestamp):
    return datetime.fromisoformat(timestamp).strftime('%Y-%m-%d %H:%M:%S')

try:
    # send the search query to Splunk
    search_results = service.jobs.oneshot(search_query, output_mode='json')

    # retrieve search results in JSON format
    jsout = json.loads(search_results.read())

    # directory to store Splunk alerts
    directory = "./splunk-alerts"
    if not os.path.exists(directory):
        os.makedirs(directory)

    # save results to a JSON file
    json_formatted_str = json.dumps(jsout, indent=2)

    json_filename = os.path.join(directory, f'alerts-data-high-severity.json')
    with open(json_filename, 'w') as f:
        f.write(json_formatted_str)

    # Markdown alert bulletin template
    template = """
{% for result in results %}
# Alerte : {{ result['event.event_title'] }}
Sévérité : **{{ result['event.impact'] }}**
Description : {{ result['originQuery'] }}
Horodatage : {{ result['_time'] | to_datetime }}
{% endfor %}
    """

    # Jinja2 environment and filter
    env = Environment()
    env.filters['to_datetime'] = to_datetime

    # process results
    filtered_results = []
    today_date = datetime.now().strftime('%Y-%m-%d')

    for result in jsout['results']:
        raw_data = json.loads(result['_raw'])

        # description of an alert
        result['originQuery'] = raw_data['event']['originQuery']['description']

        # convert "_time" to datetime object for filtering
        event_time = datetime.fromisoformat(result['_time'].replace('Z', '+00:00'))
        
        # retrieve Splunk alerts from today
        if event_time.date() == today_date:
            filtered_results.append(result)

    # create a model from the string template
    jinja_template = env.from_string(template)
    
    # render the template with the results
    print(jinja_template.render(results=filtered_results))
except Exception as e:
    print(f"⚠️ An error occurred : {e}")
finally:
    service.logout()