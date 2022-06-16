import random
import time

while True:
    tools = ['kamien', 'papier', 'nozyce']
    g = input('Co wybierasz, 1- kamien, 2- papier, 3- nozyce: ')
    g2 = random.choice(tools)
    g_index = tools.index(g)
    print(g2)
    if g_index == 2:
        g_index -= 3
    if tools.index(g) == tools.index(g2):
        print('Remis')
    elif g_index +1 == tools.index(g2):
        print("komputer wins, fatality!")
    else:
        print("player wins, fatality!")

