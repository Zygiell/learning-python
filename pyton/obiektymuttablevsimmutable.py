'''
obiekt to zmienna, która ma wiecej mozliwosci,
można wywołać na nim "funkcje"
moze miec wiecej niz 1 wartość

obiekty immutable: bool, int, float, tuple, str

immutable - niezmienne
mutable - zmienny
= zmiana miejsca wskazywania na Nowy adres ID, inny obiekt,
'''


a = 4


listSample = [1, 4, 512, 24]
listSample2 = listSample

listSample2.append(465)
a = 4
b = a
b = 7
c = 5


def add(c, amount=1):
    print(id(c))
    c = c + amount
    print(id(c))


def append_element_to_list(listka, element):
    print(id(listka))
    listka.append(element)
    print(id(listka))


print(id(listSample))
append_element_to_list(listSample, 5)
