'''__getitem__ pobiera pozycje z planszy
__setitem__ pozwala zmieniać.

'''

import random
from math import sqrt


class Rocket:
    def __init__(self, speed=1, rocketHeight=0, x=0):
        self.speed = speed
        self.rocketHeight = rocketHeight
        self.x = x

    def moveUp(self):
        self.rocketHeight += self.speed

    def __str__(self):
        return 'Rakieta jest aktualnie na wysokości :' + str(self.rocketHeight) + " i poruszała się o prędkości :" + str(self.speed)


class RocketBoard:
    def __init__(self, rocketsAmount=5):
        self.rockets = [Rocket(random.randint(1, 5))
                        for _ in range(rocketsAmount)]

        for _ in range(10):
            rocketIndexToMove = random.randint(0, len(self.rockets) - 1)
            self.rockets[rocketIndexToMove].moveUp()

        for rocket in self.rockets:
            print(rocket)

    def __getitem__(self, key):
        return self.rockets[key]

    def __setitem__(self, key, value):
        self.rockets[key].rocketHeight = value

    @staticmethod  # metoda statyczna bez selfa
    def get_distance(rocket1, rocket2):
        ab = abs(rocket1.rocketHeight - rocket2.rocketHeight)**2
        bc = (rocket1.x - rocket2.x)**2
        return sqrt(ab+bc)
