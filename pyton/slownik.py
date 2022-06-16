



definicje = {}

while True:

    print("1: Dodać definicje")
    print("2: Szukaj definicji")
    print("3: Usuń definicję")
    print("4: Zakończ")

    wybor = input("Co chcesz zrobić?: ")

    if wybor == '1':
        klucz = input("Podaj klucz? słowo do zdefiniowania: ")
        definicja = input("Podaj definicję: ")
        definicje[klucz] = definicja
        print("Definicja dodana pomyślnie")
    elif wybor == '2':
        klucz = input("Czego szukasz? ")
        if klucz in definicje:
            print(definicje[klucz])
        else:
            print("Nie znaleziono definicjy o nazwie", klucz)
    elif wybor == '3':
        klucz = input("Nazwa definicji którą chcesz usunąć")
        if klucz in definicje:
            del definicje[klucz]
            print("Definicja usunięta pomyślnie")
        else:
            print("Nie znaleziono definicji o nazwie", klucz)
    elif wybor == '4':
        print("Kończymy prace")
        break
        
    else:
        print("Niewłaściwa opcja, spróbuj jeszcze raz.")
