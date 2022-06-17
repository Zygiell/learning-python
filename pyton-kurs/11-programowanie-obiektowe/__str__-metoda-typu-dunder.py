'''
metoda typu d under - DOUBLE underscore
__str__ - STRing

'''
import random


class Rocket:
    def __init__(self, speed=1):
        self.speed = speed
        self.rocketHeight = 0

    def moveUp(self):
        self.rocketHeight += self.speed
        print(self.rocketHeight)

    def __str__(self):
        return 'Rakieta jest aktualnie na wysokości :' + str(self.rocketHeight) + " i poruszała się o prędkości :" + str(self.speed)


rockets = [Rocket(random.randint(1, 5)) for _ in range(5)]

for _ in range(10):
    rocketIndexToMove = random.randint(0, len(rockets) - 1)
    rockets[rocketIndexToMove].moveUp()

for rocket in rockets:
    print(rocket)
