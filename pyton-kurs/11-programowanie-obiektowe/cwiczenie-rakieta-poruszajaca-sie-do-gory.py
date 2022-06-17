'''
Stwórz klasę która reprezentuje rakiete która potrafi poruszać się do góry:
Jakie powinna mieć atrybuty
Oraz metody

Stwórz 5 obiektów o klasie rakieta o startowej wartości 0

Porusz wszystkie rakiety do góry 10 razy losowo
Wypisz wysokości wszystkich rakiet

'''
# Samodzielnie
import random


class Rocket:
    def __init__(self, speed):
        self.sHeight = 0
        self.speed = speed

    def rocket_ten_times_goes_up_randomly_and_print_result(self):
        for rocket in range(10):
            self.sHeight += self.speed
        return print(self.sHeight)


rocket = [Rocket(random.randint(1, 5)) for _ in range(5)]

for element in rocket:
    element.rocket_ten_times_goes_up_randomly_and_print_result()


# Kurs

class Krocket:
    def __init__(self):
        self.altitude = 0

    def moveUp(self):
        self.altitude += 1


rockets = [Krocket() for _ in range(5)]
