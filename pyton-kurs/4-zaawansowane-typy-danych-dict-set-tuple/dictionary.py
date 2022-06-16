# slownik {} dictionary KLUCZ-WARTOŚĆ (testujemy commity)

ludzie2 = {
    '1': {'name': 'Krzysztof', 'age': 25, 'sex': 'male'},
    '2': {'name': 'Dawid', 'age': 22, 'sex': 'male'},
    '3': {'name': 'Katarzyna', 'age': 21, 'sex': 'female'},
}
for key in ludzie2:
    print("id: ", key)
    for secKey in ludzie2[key]:
        print(secKey, ludzie2[key][secKey])

print(ludzie2['3']['age'])


ludzie = [
    {'id': '1', 'name': 'Krzysztof', 'lastname': 'Kowalski',
        'age': 25, 'sex': 'mężczyzna'},
    {'id': '2', 'name': 'Kamil', 'lastname': 'Pałkowski',
        'age': 33, 'sex': 'mężczyzna'},
    {'id': '3', 'name': 'Katarzyna', 'lastname': 'Bosakowska',
        'age': 21, 'sex': 'kobieta'},
    {'id': '4', 'name': 'Jakub', 'lastname': 'Warchoł', 'age': 44, 'sex': 'mężczyzna'},
    {'id': '5', 'name': 'Anna', 'lastname': 'Żygadło', 'age': 52, 'sex': 'kobieta'},
    {'id': '6', 'name': 'Kinga', 'lastname': 'Bożek', 'age': 25, 'sex': 'kobieta'},
    {'id': '7', 'name': 'Sylwester', 'lastname': 'Żygadło',
        'age': 28, 'sex': 'mężczyzna'},
    {'id': '8', 'name': 'Bartosz', 'lastname': 'Makowski',
        'age': 31, 'sex': 'mężczyzna'},
]


ludzie3 = ["arkadiusz",
           "wiola",
           "kuba"
           ]

oceny = {
    'Arkadiusz': (2, 1, 3, 5),
    'Wiola': (5, 6, 3, 2, 4)
}

oceny2 = [
    {'name': "Arkadiusz", 'oceny': (2, 1, 3, 5), 'zachowanie': 'podłe'},
    {'name': "Wioletta", 'oceny': (3, 2, 1, 6), 'zachowanie': 'dobre'}
]

oceny3 = {
    "Arkadiusz": {'oceny': (2, 1, 3, 5), 'zachowanie': 'podłe'},
    "Wioletta": {'oceny': (5, 3, 1, 4), 'zachowanie': 'dobre'}
}


'''
for record in ludzie:
    for key in record:
        print(key, ":", record[key])'''


'''


listaGosci = {
        ('Arkadiusz', 28, 'mężczyzna', '691624752'),
        ('Wioletta', 22, 'kobieta', '686484030'),
        ('Kuba', 33, 'mężczyzna', '512444333')
    }
listaGosci2 = {
        ('Arkadiusz', 28, 'mężczyzna'),
        ('W', 22, 'kobieta'),
        ('K', 33, 'mężczyzna')
        }

listaGosci3 = listaGosci & listaGosci2


for imie, wiek, plec, tel in listaGosci:
    print("Imie: ", imie)
    print("Wiek: ", wiek)
    print("Plec: ", plec)
    print("Nr telefonu: ", tel)
    print("\n")
'''
