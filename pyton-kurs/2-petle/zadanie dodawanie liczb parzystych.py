''' nie można użyc else  '''
wynik = 0
i = 0
while i < 3:
    x = int(input("Podaj parzystą liczbę dodatnią:"))
    if (x % 2 == 1)or (x < 0):
        print("To nie jest dodatnia liczba parzysta, podaj poprawną liczbe")
        continue
    wynik += x
    i += 1
    
    
        
print("Suma parzystych liczb dodatnich podanych przez użytkownika:", wynik)
            
