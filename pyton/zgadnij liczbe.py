''' Zgadnij liczbe- wybierz sekretną liczbę
Napisz program który zapyta użytkownika o liczbę, jeżeli użytkownik wpisze
liczbę równą sekretnej liczbie pogratuluj, jeżeli wpisze za niską liczbę
podpowiedz iż liczba jest większa, jeżeli wpisze za wysoką liczbę poinformuj
iż jest za duża'''

secretNumber = 666
userInput = 0

while userInput != secretNumber:
    userInput = int(input('Zgadnij liczbę!: '))
    if userInput > secretNumber:
        print("Podana liczba jest za duża")
    elif userInput < secretNumber:
        print("Podana liczba jest za mała")

print("Gratulacje odgadłeś sekretną liczbę!", secretNumber)
