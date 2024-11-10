import splunklib.client as client
import json
from jinja2 import Environment
from datetime import datetime
import os
import smtplib
from email.mime.text import MIMEText

# Email configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
SENDER_EMAIL = "splunksoc.insacvl@gmail.com"
SENDER_PASSWORD = "<gmail-app-password>"
RECIPIENT_EMAILS = [
    "virodan4@gmail.com",                   # Antoine VIRGOS
    "linkdine08@gmail.com",                 # Ayet MERZOUQI
    "rayanebe570@gmail.com",                # Rayane BENDAHMANE
    "makaloucherif@gmail.com",              # Shérif MAKALOU
    "philemon.stjean@esih.edu"              # Philémon ST-JEAN
]

# Splunk configuration
SPLUNK_HOST = "172.10.80.212"
SPLUNK_PORT = "8089"
SPLUNK_SCHEME = "https"
SPLUNK_USERNAME = "<username>"
SPLUNK_PASSWORD = "<password>"

# connect to Splunk instance
service = client.connect(
    host=SPLUNK_HOST,
    port=SPLUNK_PORT,
    scheme=SPLUNK_SCHEME,
    username=SPLUNK_USERNAME,
    password=SPLUNK_PASSWORD
)

# Splunk search query to retrieve only "High" severity alerts
search_query = 'search index="alerts" event.event_title="*" event.impact="high"'

# convert ISO timestamp to formatted datetime
def to_datetime(timestamp):
    return datetime.fromisoformat(timestamp).strftime('%Y-%m-%d %H:%M:%S')

def send_email(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = SENDER_EMAIL
    msg['To'] = ', '.join(RECIPIENT_EMAILS)

    try:
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as smtp_server:
            smtp_server.login(SENDER_EMAIL, SENDER_PASSWORD)
            smtp_server.sendmail(SENDER_EMAIL, RECIPIENT_EMAILS, msg.as_string())
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")

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
    today_date = datetime.now().date()

    for result in jsout['results']:
        raw_data = json.loads(result['_raw'])

        # description of an alert
        result['originQuery'] = raw_data['event']['originQuery']['description']

        # convert the _time field to a datetime object
        alert_time = datetime.strptime(result['_time'], '%Y-%m-%dT%H:%M:%S.%f%z').date()

        # check if the alert is from today
        if alert_time == today_date:
            filtered_results.append(result)

    # create a model from the string template
    jinja_template = env.from_string(template)
    
    # render the template with the results
    rendered_alerts = jinja_template.render(results=filtered_results)

    # send email if there are alerts
    if filtered_results:
        email_subject = f"Alertes Splunk de sévérité élevée - {today_date}"

        send_email(email_subject, rendered_alerts)
        print("Email sent with alerts.")
    else:
        print("No high severity alerts for today. No email sent.")
except Exception as e:
    print(f"⚠️  An error occurred : {e}")
finally:
    service.logout()