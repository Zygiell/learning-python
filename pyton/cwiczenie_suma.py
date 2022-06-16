'''Napisz program który policze sume wszystkich liczb od 1 do podanej liczby
dla np. 5
1+2+3+4+5
zwróci 15'''

a = int(input("Podaj liczbe"))
suma = 0
for liczba in range(0, a + 1):
    suma = suma + liczba
    print(suma)
