import random


class Rocket:
    def __init__(self, speed=1):
        self.speed = speed
        self.rocketHeight = 0

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
