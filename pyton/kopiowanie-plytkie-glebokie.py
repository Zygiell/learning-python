''' copy -  płytka, deepcopy - gl copy '''
import copy


def evil_function(toBeDestroyedList):
    print(id(toBeDestroyedList))
    toBeDestroyedList[0] = 4


myList = [1, 4, 2, 1, 52, 3]
print(id(myList))
evil_function(copy.deepcopy(myList))
