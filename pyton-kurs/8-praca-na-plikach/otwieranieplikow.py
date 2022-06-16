''' 
PLIK - nazwana lokacja, która przechowuje na stałe dane dysku.

RAM - pamięć podręczna komputera, gdize przechowywane są dane TYMCZASOWO

Operacjer na plikach:
1) otwieranie
2) pisanie/czytanie
3) zamykanie

podstawowe sposoby otwierania plików
r- R ead (czytanie) domyslne
w - W rite (pisanie) jezeli plik istnial to go usunie, jeśli nie to stworzy
a - A ppend (dopisywanie)

rozszerzenie to tylko 'tekst' nadawany po to aby, inne programy rozpoznawały plik w odpowiedni dla tych programów sposób

mnogie tryby:
r+ - do czytania i pisania
file.read file.write

w+ - do pisania i czytania
różni się tym, że usunie zawartość istniejącego pliku lub stworzy plik gdy go nei było

a+ - "wieczny tryb' dopisywanie i czytanie
UWAGA! wskaźnik dopisywania jest zawsze na końcu
jeśli plik nie istniał - stworzy go

tell - mówi, gdzie skonczyliśmy ostatnią operacje na pliku
seek - szuka (zmienia) - na miejsce wskazane przez nas

'''


with open('pyton-kurs/8-praca-na-plikach/Oceany.txt', 'a+', encoding='UTF-8') as file:
    file.write('\nOcean Arka')
    file.seek(0)
    print(file.tell())
