'''
3 zdj kotow ma odpalac z danej rasy joł


'''

import requests
import json
import webbrowser


r = requests.get(
    'https://api.thecatapi.com/v1/images/search?breed_ids=acur&limit=3')
acur = r.json()


for cat in acur:
    webbrowser.open_new_tab(cat['url'])
