import figury

from enum import IntEnum

Menu_Figury = (IntEnum('Menu_Figury', 'Kwadrat Prostokąt Koło Trójkąt Trapez'))

while True:

    choice = int(input(""" Wybierz figurę, której pole chcesz obliczyć:
        1. Kwardrat
        2. Prostokąt
        3. Koło
        4. Trójkąt
        5. Trapez \n"""))

    if choice == Menu_Figury.Kwadrat:
        a = float(input("Podaj bok kwadratu: "))
        print(figury.pow_kwadrat(a))

    elif choice == Menu_Figury.Prostokąt:
        a = float(input("Podaj pierwszy bok prostokąta: "))
        b = float(input("Podaj drugi bok prostokąta: "))
        print(figury.pow_prostok(a, b))

    elif choice == Menu_Figury.Koło:
        r = float(input("Podaj promień koła: "))
        print(figury.pow_kola(r))

    elif choice == Menu_Figury.Trójkąt:
        a = float(input("Podaj długośc boku trójkąta: "))
        h = float(input("Podaj wysokość trójkąta: "))
        print(figury.pow_triangle(a, h))

    elif choice == Menu_Figury.Trapez:
        a = float(input("Podaj pierwszy bok trapezu: "))
        b = float(input("Podaj drugi bok trapezu: "))
        h = float(input("Podaj wysokość trapezu: "))
        print(figury.pow_trapez(a, b, h))
    else:
        print('Niewłaściwy wybór, spróbuj jeszcze raz!')
