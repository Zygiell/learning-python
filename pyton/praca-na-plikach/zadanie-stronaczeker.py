'''
Wyobraź sobie, że szef zlecił Ci zadanie otwarcia z jego pliku tekstowego 1500 stron i przefiltrowania ich w taki sposób, aby podać mu tylko te, które działają. Szef chce, abyś działające strony zapisał do pliku tekstowego.

Szef nie przesłał Ci jeszcze pliku ze stronami. Wiesz tylko o tym, że będziesz musiał wykonać te zadanie następnego dnia.

Załóżmy, że tylko 300 stron z tej listy działa. Czy zrobiłbyś to wszystko ręcznie? A może zastosowałbyś Pythona i to co do tej pory poznałeś? :)

Masz czas na zastanowienie się co zrobić do następnego dnia. Możesz napisać krótki program, który zrobi robotę za Ciebie lub też będziesz wykonywał cały dzień żmudną robotę ;)

Podpowiedź:

Stwórz funkcję, która otwiera i sprawdza, czy podana strona z listy istnieje (True), czy też nie (False). Skorzystaj z faktu, że strony, które się otwierają poprawnie to takie, które zwracają status_code == 200.

Pochwal się rozwiązaniem :)

Powodzenia! :-)

'''
import requests


def websiteCheck(filename):

    with open(filename, 'r', encoding='UTF-8') as file:
        for line in file:
            try:
                website = requests.get(line.strip())
                print(website)
                if website.status_code == 404:
                    continue

                else:
                    with open('pyton/praca-na-plikach/working_websites.txt', 'a+', encoding='UTF-8') as file2:
                        file2.write(line)
            except requests.exceptions.ConnectionError:
                continue


websiteCheck('pyton/praca-na-plikach/adresy.txt')
