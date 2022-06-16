'''
Napisz krótką grę w której masz 5 ruchów w jedną stronę poprzez KOMNATĘ.
Za każdym razem masz szanse spotkać po drodze skrzynkę  lub NIC.
Skrzynki mają różne kolory.
Kolor skrzynki oznacza jak rzadka jest ta skrzynka.

zielona - 75%
pomarańczowa - 20 %
fioletowa -4 %
złota (legendarna) - 1 %

Ustaw, że jest 40% szansy, że nie spotkasz niczego. 60%, ze będzie skrzynka
Ustaw złoto jako to co może 'wypaść' ze skrzynki:
zielony - 1000
pomarańczowy - 4000
fioletowy - 9000
złota - 16000

1, czysty kod
2 nazywanie zmeinnych tak by były samoopisujące sie
3 po angielsku
'''
import random
import time


def welcome_message():
    global name
    name = input('Hi, whats your name?: ')
    time.sleep(1)

    welcome_text = f"""Hello {name}
Lets play a game, you are closed in very tight room, you can only move forward.
To get out you need to take 5 steps, every step you take there is a chance to find a chest with gold,
lets see how much gold can you collect
"""
    for l in welcome_text.split('\n'):
        print(l)
        time.sleep(1)


def is_chest_found(chestChanceToFind):
    if random.uniform(0, 100) <= chestChanceToFind:
        return True
    else:
        return False


def time_counter():
    for c in ['3', '2', '1']:
        print(c)
        time.sleep(1)


def which_chest_found():
    chests_odds = {'green': 75, 'orange': 20, 'violet': 4, 'gold': 1}
    chests_reward = {'green': 1000, 'orange': 4000,
                     'violet': 9000, 'gold': 16000}
    foundChest = random.choices(
        list(chests_odds.keys()), list(chests_odds.values()))
    print('Congratulations you found a chest with gold, its',
          str(foundChest), 'chest.')
    return chests_reward[foundChest[0]]


def run():
    welcome_message()
    steps = ['first', 'second', 'third', 'fourth', 'fifth']
    while True:
        playerPouch = 0
        step_counter = 0
        playerChoice = input(
            'Are you ready to take first step? Y - yes Q - quit a game: ').lower()

        if playerChoice == 'y':
            while (step_counter < 5):
                print('You made', steps[step_counter],
                      'step, you are looking around')
                step_counter += 1
                time_counter()

                if is_chest_found(60) == True:
                    playerPouch += which_chest_found()
                    time.sleep(1)
                    print('Your gold balance: ', playerPouch)
                else:
                    print('You found nothing', name,
                          'Better luck next step buddy!')

            print('You made it out from the room, you managed to earn',
                  playerPouch, 'gold.')
        elif playerChoice == 'q':
            break
        else:
            print('Wrong choice, try again Y - yes, Q - quit a game: ')
            continue


run()
