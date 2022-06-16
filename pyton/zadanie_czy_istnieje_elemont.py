'''
Funkcja która będzie sprawdzała czy wartość np 30 znajduje sie w kontenerze, jeżeli się znajduje funkcja zwraca tak jeżeli nie funkcja zwraca nie
Dodatkowo sprawdź co jest szybsze, sprawdzenie w secie czy w liscie.
'''


import time


def function_performance(func, how_many_times=1, *arg):
    sum = 0

    for i in range(0, how_many_times):
        start = time.perf_counter()
        func(*arg)
        end = time.perf_counter()
        sum = sum + (end-start)
    return sum


def value_checker(container, value):
    if value in container:
        return True
    else:
        return False


setContainer = {i for i in range(1000)}
listContainer = [i for i in range(1000)]
value_checker(setContainer, 1111)
print(function_performance(value_checker, 500000, setContainer, 1111))
value_checker(listContainer, 999)
print(function_performance(value_checker, 500000, listContainer, 1111))

'''argumenty pozycyjne (NIENAZWANE) przed argumentami nazwanymi!!!! np how_many_times'''
