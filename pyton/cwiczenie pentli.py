wynik = 0
'''i = 0
while i < 4:
    x = int(input("Podaj liczbe: "))
    wynik += x
    i += 1

print("Wynik dodawania liczb:", wynik)'''



'''for i in range(1211):
    if (i % 2 == 0):
        print("Liczba", i, "jest parzysta")

   

print("Wynik dodawania liczb:", wynik)'''

wynik = 0

i = 0
while i < 3:
    x = int(input("Podaj dodatnią liczbę:"))
    if (x > 0):
        wynik += x
    else:
        print("Miała być liczba dodatnia, podaj liczbę dodatnią!!")
        continue
    print ("Aktualny wynik dodawania to:", wynik)
    i += 1
