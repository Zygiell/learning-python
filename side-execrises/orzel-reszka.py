'''    Użytkownik wybiera czy obstawia resztę, czy orła (literka r – reszka, literka o – orzeł)
    Po dokonaniu wybory, Komputer odlicza 3,2,1,
    a następnie dokonuje 'rzutu’, czyli losowego wyboru orzeł / reszka.
    Komputer wyświetla wynik rzutu.
    Jeżeli wygrał użytkownik, to dodaje punkt dla użytkownika, jeżeli komputer to dodaje punkt dla komputera.
    Wyświetla wyniki
    Wracamy do punktu 1. '''

import random
import odliczacz

coin = ['orzel', 'reszka']
p = 0
c = 0
result = ()

print("Zagrajmy w orzeł reszka")

while True:
    choice = input('Co wybierasz o - orzeł r - reszka: \n')
    if choice == 'o':
        print("Wybrałeś orła, losujemy")
        print(odliczacz.odliczacz(3))
        result = random.choice(coin)
        print("Wylosowałeś :", result)
        if result == "orzel":
            p += 1
            print("Wygrałeś, punktacja Gracz :", p, "Komputer :", c)
        else:
            c += 1
            print("Przegrałeś, punktacja Gracz:", p, "Komputer :", c)

    elif choice == 'r':
        print("Wybrałeś reszkę, losujemy")
        print(odliczacz.odliczacz(3))
        result = random.choice(coin)
        print("Wylosowałeś :", result)
        if result == "reszka":
            p += 1
            print("Wygrałeś, punktacja Gracz :", p, "Komputer :", c)
        else:
            c += 1
            print("Przegrałeś, punktacja Gracz:", p, "Komputer :", c)
    else:
        print("Niewłaściwy wybór, spróbuje jescze raz")
