'''
Menu, jezeli uzytkownik chce 5 losowych faktów na temat psów printnij
jezlie kotow prnitnij

'''
import requests
import json

while True:
    choice = input('5 losowych faktów! Wcisnij 1 - koty 2 - psy')
    params = dict()

    if choice == '1':
        params = {
            'amount': 5,
        }
        r = requests.get('https://cat-fact.herokuapp.com/facts/random', params)
        facts = r.json()
        for cat in facts:
            print(cat['text'])
    elif choice == '2':
        params = {'amount': 5, 'animal_type': 'dog'}
        r = requests.get('https://cat-fact.herokuapp.com/facts/random', params)
        facts = r.json()
        for dog in facts:
            print(dog['text'])
    else:
        print('Niewłaściwy wybór try again')
