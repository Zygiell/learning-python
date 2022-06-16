''' Funkcja - blok kodu do którego można odwołać się w każdej chwili,
aby otrzymać pożadany przez nas wynik
def - definition - tworzenie funkcji
def nazwa_funkcji():
    instrukcja1
    instrukcja2
nazwa_funkcji()
'''


def wiadomosc_powitalna(imie):
    print("Cześć", imie, ", milo mi Cie Powitac w moim programie")
    

wiadomosc_powitalna("Arku")
imiona = ['Arku', 'Wiolu', 'Bartku']

for imie in imiona:
    wiadomosc_powitalna(imie)

