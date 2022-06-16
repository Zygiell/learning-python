'''
ĆWICZENIE:

Wczytaj imiona i nazwiska z pliku o nazwie:
imionanazwiska.txt

1) rozdziel je tak aby, powstała lista krotek, gdize wewnętrzne krotki to pary imiona/nazwiska
2) zapisz imiona do pliku imiona.txt
3) zapisz nazwiska do pliku  nazwiska.txt

Zastanów się jak rozwiązać problem,
gdy nie ma podanego nazwiska w pliku imionanazwiska.txt, gdy będziesz zapisywał nazwiska do pliku nazwiska txt
'''


fullname = []

with open('pyton-kurs/8-praca-na-plikach/imionanazwiska.txt', 'r', encoding='UTF-8') as file:
    for lane in file:
        fullname.append(lane.strip())

with open('pyton-kurs/8-praca-na-plikach/imiona.txt', 'w+', encoding='UTF-8') as file:
    for name in fullname:
        file.write(name.split()[0] + '\n')

with open('pyton-kurs/8-praca-na-plikach/nazwiska.txt', 'w+', encoding='UTF-8') as file:
    for name in fullname:
        file.write(name.split()[-1] + '\n')
