'''
TO DO LIST:
API : https://docs.thecatapi.com/
1. function that converts json into content
2. auth with api using header from another file.
2. function that generates random cats
3. app that show user random cats, user can decide if want to add cat to his favourite cat list
4. user also can delete cats from his fav list.

'''
import requests
import json
import credentials


def get_content_from_json(response):
    try:
        content = response.json()
    except json.decoder.JSONDecodeError:
        print('Wrong Format')
    else:
        return content


def get_random_cat_info():
    r = requests.get('https://api.thecatapi.com/v1/images/search')
    return get_content_from_json(r)[0]


def get_user_favourite_cats_list(userid):
    params = {'sub_id': userid}
    r = requests.get('https://api.thecatapi.com/v1/favourites/',
                     params, headers=credentials.header)
    return get_content_from_json(r)


def add_generated_cat_to_user_favourite_cats_list(userid, catid):
    catData = {'image_id': catid, 'sub_id': userid}
    r = requests.post('https://api.thecatapi.com/v1/favourites/',
                      json=catData, headers=credentials.header)
    return get_content_from_json(r)


def delete_cat_from_user_favourite_cats_list(CatToRemoveId):
    r = requests.delete('https://api.thecatapi.com/v1/favourites/' +
                        CatToRemoveId, headers=credentials.header)
    return get_content_from_json(r)


def run():
    # Welcome message - extract name from user:
    name = input('Hello, whats your name ?: ')
    print('Nice to meet you', name)
    # Use user name as an id, everytime user launch app, if he put his name correctly, he will connect with his favourite list(case insensitive):
    userID = name[0] + name[-1] + 'ZyGiELapp'
    userFavCats = get_user_favourite_cats_list(userID)
    randomGeneratedCat = get_random_cat_info()
    newlyAddedCatInfo = dict()
    favCatsByID = {
        favouriteCat['id']: favouriteCat['image']['url']
        for favouriteCat in userFavCats
    }
    print('List of your favourite cats: ')
    for key, value in favCatsByID.items():
        print(key, ' : ', value)

    while True:
        print('You drew this cat photo: ', randomGeneratedCat['url'])
        menu = input('''What would you like to do:
                    1. Generate random cat
                    2. Add generated cat to my personal favourite list
                    3. Delete cat from my personal favourite list
                    4. Show my favourite cats list
                    5. Quit
                    Press button 1,2,3,4,5  to chose: ''')

        # Menu conditions below :

        if menu == '1':
            randomGeneratedCat = get_random_cat_info()
            continue

        elif menu == '2':
            resultFromAddingCatToFav = add_generated_cat_to_user_favourite_cats_list(
                userID, randomGeneratedCat['id'])
            newlyAddedCatInfo = {
                resultFromAddingCatToFav['id']: randomGeneratedCat['url']}
            print('Operation status :',
                  resultFromAddingCatToFav['message'], ', added cat id: ', resultFromAddingCatToFav['id'])
            # updating dictionary of fav cat lists so i dont need to connect with api to keep it updated every time
            favCatsByID.update(newlyAddedCatInfo)
            newlyAddedCatInfo.clear()
            randomGeneratedCat = get_random_cat_info()
            continue

        elif menu == '3':
            print('List of your favourite cats: ')
            for key, value in favCatsByID.items():
                print(key, ' : ', value)
            catToDeleteId = input(
                'Type cat ID you want to delete from your favourite list : ')
            resultFromDeletingCatFromFav = delete_cat_from_user_favourite_cats_list(
                catToDeleteId)
            print('Operation status :', resultFromDeletingCatFromFav)
            try:
                favCatsByID.pop(int(catToDeleteId))
            except ValueError:
                print('FAILED!!! ID has to be an number!!!!')
            continue

        elif menu == '4':
            print('List of your favourite cats: ')
            for key, value in favCatsByID.items():
                print(key, ' : ', value)
            continue

        elif menu == '5':
            print('Quiting app')
            break

        else:
            print('Wrong choice, try again')


run()
