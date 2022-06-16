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

with open('imionanazwiska.txt', 'r', encoding='UTF-8') as file:
    for lane in file:
        fullname.append(tuple(lane.strip().split(' ')))

with open('imiona.txt', 'w', encoding='UTF-8') as file:
    for item in fullname:
        file.write(item[0] + '\n')
with open('nazwiska.txt', 'w', encoding='UTF-8') as file:
    for item in fullname:
        try:
            file.write(item[1] + '\n')
        except IndexError:
            file.write('\n')
