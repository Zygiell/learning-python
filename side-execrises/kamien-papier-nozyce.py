'''papier kamien nożyce'''

import random
imie = input('Jak masz na imię?: \n')
print("Cześć", imie, "Gramy w papier, kamień, nożyce do 3 zwycięstw!")
tools = ['papier', 'kamien', 'nozyce']
result = []
c = 0
p = 0
newGame = ()
while True:
    if c == 3: #tutaj mógłbym zrobic c==3 or p == 3 i skrócić kod
        print("Wygrałem, jestem super!")
        newGame = input("Czy chcesz zacząć od nowa, T - TAK, N - NIE: \n")
        if newGame == "T" or newGame == "t": # newGame.lower 
            c = 0
            p = 0
            print("Powodzenia!")
            continue
        elif newGame == "N" or newGame == "n":
            print("No trudno, papa")
            break
        else:
            print("Niewłaściwy wybór, spróbuj jeszcze raz")
            continue
    elif p == 3:
        print(imie, "! woooow WYGRAŁEŚ")
        newGame = input("Czy dasz mi szanse się odegrać?, T - TAK, N - NIE: \n")
        if newGame == "T" or newGame == "t":
            c = 0
            p = 0
            print("Powodzenia!")
            continue
        elif newGame == "N" or newGame =="n":
            print("No trudno, papa")
            break
        else:
            print("Niewłaściwy wybór, spróbuj jeszcze raz")
            continue
    print(' 1- papier, 2- kamien, 3- nożyce, q - zakończ grę \n')
    wybor = input("Co wybierasz? : \n")
    if wybor == '1':
        print('Wybrałeś papier')
        result = random.choice(tools)
        if result == 'papier':
            print('Wybrałem papier, Remis!')
        elif result == 'kamien':
            print('Wybieram kamień, Gratulacje, wygrałeś!', imie)
            p += 1
            print("Punktacja: ", imie, ": ", p, "Komputer: ", c)
        else:
            print('Nożyce! Loser sucker!')
            c += 1
            print("Punktacja: ", imie, ": ", p, "Komputer: ", c)
    elif wybor == '2':
        print('Wybrałeś kamien')
        result = random.choice(tools)
        if result == 'papier':
            print('Wybrałem papier, Przegrałeś;(')
            c += 1
            print("Punktacja: ", imie, ": ", p, "Komputer: ", c)
        elif result == 'kamien':
            print('Wybieram kamień, Remis!')
        else:
            print('Nożyce! Gratulacje, wygrałeś!', imie)
            p += 1
            print("Punktacja: ", imie, ": ", p, "Komputer: ", c)

    elif wybor == '3':
        print('Wybrałeś nożyce')
        result = random.choice(tools)
        if result == 'papier':
            print('Wybrałem papier, Gratulacje, wygrałeś!', imie)
            p += 1
            print("Punktacja: ", imie, ": ", p, "Komputer: ", c)
        elif result == 'kamien':
            print('Wybieram kamień, Przegrałeś:(')
            c += 1
            print("Punktacja: ", imie, ": ", p, "Komputer: ", c)
        else:
            print('Nożyce! Widocznie mamy remis')
    elif wybor == 'q':
        print("Do następnego razu!")
        break
    
    else:
        print("Niewłaściwy wybór, spróbuj jeszcze raz!")

   
