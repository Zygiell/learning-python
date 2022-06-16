"""

json.loads(jsonstring) - przetwarza jsonstring na dane typu Python

json.load(filePointer) - wczytuje json z pliku i zwraca jako wynik metody
                        dane typu Python

load z ang. wczytać
"""

import json

film = {
    "title": "Ale ja nie będę tego robił!",
    "release_year": 1969,
    "won_oscar": True,
    "actors": ("Arkadiusz Włodarczyk", "Wiolleta Włodarczyk"),
    "budget": None,
    "credits": {
        "director": "Arkadiusz Włodarczyk",
        "writer": "Alan Burger",
        "animator": "Anime Animatrix"
    }
}

encodedRetrievedMovie = '{"title": "Ale ja nie będę tego robił!", "release_year": 1969, "won_oscar": true, "actors": ["Arkadiusz Włodarczyk", "Wiolleta Włodarczyk"], "budget": null, "credits": {"director": "Arkadiusz Włodarczyk", "writer": "Alan Burger", "animator": "Anime Animatrix"}}'

decodedM = json.loads(encodedRetrievedMovie)


with open('sample.json', encoding='UTF-8') as file:
    wynik = json.load(file)
print(wynik)
