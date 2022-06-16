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


def findApproxValue(value, percentRange):
    lowestValue = value - (percentRange / 100) * value
    highestValue = value + (percentRange / 100) * value
    return random.randint(lowestValue, highestValue)


def welcome_message():
    global name
    name = input('Hi, whats your name?: ')
    time.sleep(1)
    print('Hello', name)
    time.sleep(1)
    print('Lets play a game, you are closed in very tight room, you can only move forward.')
    time.sleep(1)
    print('To get out you need to take 5 steps, every step you take there is a chance to find a chest with gold,')
    time.sleep(1)
    print('lets see how much gold can you collect')


def is_chest_found(chestChanceToFind):
    isFindChance = random.uniform(0, 100)
    if isFindChance <= chestChanceToFind:
        return True
    else:
        return False


def time_counter():
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')


def which_chest_found():
    global playerPouch
    chest = ['green', 'orange', 'violet', 'gold']
    foundChest = random.choices(chest, [75, 20, 4, 1])
    print('Congratulations you found a chest with gold, its',
          str(foundChest), 'chest.')
    if foundChest == ['green']:
        playerPouch += findApproxValue(1000, 10)
    elif foundChest == ['orange']:
        playerPouch += findApproxValue(4000, 10)
    elif foundChest == ['violet']:
        playerPouch += findApproxValue(9000, 10)
    else:
        playerPouch += findApproxValue(16000, 10)


playerPouch = 0
steps = 0
welcome_message()


while True:
    playerChoice = input(
        'Are you ready to take first step? Y - yes Q - quit a game: ')
    playerChoice = playerChoice.lower()

    if playerChoice == 'y':
        while (steps < 5):
            steps += 1
            print('You made', steps, 'step, you are looking around')
            time_counter()
            if is_chest_found(60) == True:
                which_chest_found()
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
