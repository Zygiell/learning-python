"""

JSON
ZAPIS
json.dumps(data) - zapisuje dane do postaci Stringowej json
json.dump(data, nameOfFile, ensure_ascii=False) - zapisuje dane do pliku w postaci json

indent=4 - wciecia
sort_keys=True - sortowanie alfabetyczne
ensure_ascii=False --- znaki specjalne np polskie znaki

ODCZYT
json.loads(jsonstring) - przetwarza jsonstring na dane typu Python

json.load(filePointer) - wczytuje json z pliku i zwraca jako wynik metody
                        dane typu Python

"""
import json
import pprint

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

encodedFilm = json.dumps(film, ensure_ascii=False, indent=4, sort_keys=True)
print(encodedFilm)

with open('pyton-kurs/8-praca-na-plikach/sample.json', 'w', encoding='UTF-8') as file:
    json.dump(film, file, ensure_ascii=False, indent=4)

with open('pyton-kurs/8-praca-na-plikach/sample.json', encoding='UTF-8') as file:
    wynik = json.load(file)
pprint.pprint(wynik)
"""
{  
   "title":"Ale ja nie będę tego robił!",
   "release_year":1969,
   "won_oscar":true,
   "actors":[  
      "Arkadiusz Włodarczyk",
      "Wiolleta Włodarczyk"
   ],
   "budget":null,
   "credits":{  
      "director":"Arkadiusz Włodarczyk",
      "writer":"Alan Burger",
      "animator":"Anime Animatrix"
   }
}
"""
