'''
docstring - DOCument string - pomaga dokumentować klasy  / metody

'''
import random


class Rocket:

    def __init__(self, speed):
        """konstrukcja

        Args:
            speed (int): szybkość rakiety
        """
        self.speed = speed
        self.rocketHeight = 0

    def moveUp(self):
        """rakieta porusza się do góry
        """

        self.rocketHeight += self.speed
        print(self.rocketHeight)


rockets = [Rocket(random.randint(1, 5)) for _ in range(5)]
counter = 0

while counter < 10:
    counter += 1
    for rocket in rockets:
        rocket.moveUp()
