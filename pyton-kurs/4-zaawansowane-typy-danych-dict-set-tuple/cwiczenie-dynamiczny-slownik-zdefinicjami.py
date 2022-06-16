"""
Napisz program, który pozwoli użytkownikowi:
1) dodac nowe definicje
2) szukać istniejących definicji
3) usuwać wybrane przez niego definicje
"""

definicje = {}
while True:
    print('''Wybierz co chcesz zrobić,
    1 - Dodaj nową definicję,
    2 - Szukaj istniejących definicji,
    3 - Usuń wybraną definicję''')

    wybor = input("Co chcesz zrobić: \n")

    if wybor == '1':
        klucz = input("nazwij nową definicję: \n")
        definicja = input("Podaj definicję: \n")
        definicje[klucz] = definicja
        print("Defnicja dodana pomyślnie")
    elif wybor == '2':
        for key in definicje:
            print("definicja : \n", key, ": ", definicje[key])
            print("\n")
        szukajka = input("Podaj nazwę definicji którą szukasz")
        if szukajka in definicje:
            print(definicje[szukajka])
        else:
            print("Nie ma takiej definicji w Naszej bazie danych \n \n")
    elif wybor == '3':
        for key in definicje:
            print("definicja : \n", key, ": ", definicje[key])
            print("\n")
        usuwacz = input("Podaj nazwę definicji którą chcesz usunąć \n \n")
        if usuwacz in definicje:            
            del definicje[usuwacz]
            print("Usunięto definicję", usuwacz)
        else:
            print("Nie ma takiej definicji w Naszej bazie danych \n \n")
    else:
        print("Dokonano złego wyboru, spróbuj jeszcze raz \n \n")
