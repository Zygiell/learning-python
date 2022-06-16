import requests
import json
import webbrowser
from pprint import pprint

params = {"api_key": "925a5ba4e4384250df3244104d7e10d1ec0b0b55",
          "country": "pl", "year": 2022, 'month': 12}

r = requests.get('https://calendarific.com/api/v2/holidays/', params)
content = r.json()
pprint(content)
