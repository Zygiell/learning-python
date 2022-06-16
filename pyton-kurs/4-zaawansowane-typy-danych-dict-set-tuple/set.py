"""
     czy:   el. unikalne | kolejność | zmiana konkretnego el. | nowe elementy
listy []       NIE           TAK             TAK                   TAK             list
krotki ()      NIE           TAK             NIE                   NIE             tuple
słowniki{k:v}  TAK           NIE             TAK                   TAK             directionary
zbiory{}       TAK           NIE             NIE                   TAK             set

        ZBIORY: BONUS w postaci | (wszystkie unikalne elementy z zbiorów) &(koniunkcja wspólne elementy) -(odjąć) ^ (alternatywa wykl)
"""



a = {1, 4, 20, -4, 66}
b = {2, 1, 25, 40, 20}


print(a.issubset(b))
