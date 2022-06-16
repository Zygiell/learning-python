import requests
import json
import webbrowser
import credentials
from pprint import pprint


def get_json_content_from_response(response):
    try:
        content = response.json()
    except json.decoder.JSONDecodeError:
        print('niepoprawny format')
    else:
        return content


def get_favourite_cats(userId):
    params = {'sub_id': userId}
    r = requests.get('https://api.thecatapi.com/v1/favourites/',
                     params, headers=credentials.header)
    return get_json_content_from_response(r)


def get_random_cat():
    r = requests.get('https://api.thecatapi.com/v1/images/search',
                     headers=credentials.header)
    return get_json_content_from_response(r)[0]


def add_cat_to_favourites(catId, userId):
    catData = {'image_id': catId, 'sub_id': userId}
    r = requests.post('https://api.thecatapi.com/v1/favourites/',
                      json=catData, headers=credentials.header)
    return get_json_content_from_response(r)


def remove_favourite_cat(idCatToRemove):
    r = requests.delete('https://api.thecatapi.com/v1/favourites/' +
                        idCatToRemove,  headers=credentials.header)
    return get_json_content_from_response(r)


print('Zaloguj sie podaj login i haslo')
# pobieranie loginu i hasla
# sprawdzamy czy login i haslo jest poprawne
# logowanie zaszlo poprawnie
# pobieramy z bazy danych user id i name - nazwe uzytkownika

userId = 'agh2m'
name = 'Arkadiusz'

print('Witaj ' + name)
favouriteCats = get_favourite_cats(userId)
print('Twoje ulubione kotki to: ', favouriteCats)
randomCat = get_random_cat()
print('Wylosowano kotka: ', randomCat['url'])
addToFavChoice = input(
    'Czy chcesz dodać wylosowanego kotka do ulubionych? t-tak, n -nie ')
if addToFavChoice.lower() == 't':
    resultFromAddingFavCat = add_cat_to_favourites(randomCat['id'], userId)
    newlyAddedCatInfo = {resultFromAddingFavCat['id']: randomCat['url']}

else:
    print('No to lipa, kotek jest smutny :(')
favCatsByID = {
    favouriteCat['id']: favouriteCat['image']['url']
    for favouriteCat in favouriteCats
}
favCatsByID.update(newlyAddedCatInfo)
print(favCatsByID)
idCatToRemove = input('czy chcesz usunąć kotka z ulubionych? podaj jego id: ')
print(remove_favourite_cat(idCatToRemove))
