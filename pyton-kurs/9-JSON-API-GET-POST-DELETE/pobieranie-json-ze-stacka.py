import requests
import json
import pprint
import webbrowser
from datetime import datetime, timedelta
'''
time stamp - znak czasu
1 stycznia 1970

'''
'''
API - Application Programming Interface
Inter = pomiędzy
face = twarz
minimalie 15 pkt
posegregowane malejaco
z ostatniego tygodnia
kategoria python
'''
fromdateparm = datetime.today() - timedelta(days=30)

params = {
    'site': 'stackoverflow',
    'sort': 'votes',
    'order': 'desc',
    'fromdate': int(fromdateparm.timestamp()),
    'tagged': 'python',
    'min': '15'

}
r = requests.get('https://api.stackexchange.com/2.3/questions/', params)

try:
    questions = r.json()
except json.decoder.JSONDecodeError:
    print('Zly format')
else:
    for question in questions['items']:
        webbrowser.open_new_tab(question['link'])
