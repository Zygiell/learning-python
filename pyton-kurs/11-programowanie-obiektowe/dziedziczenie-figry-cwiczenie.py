'''
Stwórz trzy klasy;

1)Rectangle - prostokąt
2) Square - kwadrat
3) Cubne - sześcian

a) stwórz konstruktory __init__
metody obliczające powierzchnię kwadratu, prostokąta sześcianu
metode obliczającą objętość sześcianu

zastanów się jak możesz wykorzystać do tego dziedziczenie aby nie powtarzać kodu

przyporządkowanie - przynależy, należy do, jes jedną ze składowych, jest częścią czegoś

Agregacja - łąćznyć w całość, zawieran ie się, gromadzenie - tworzenie obiektu składowego

Kompozycja - WARUNEK - obiekt, który przyporzadkowujemy nie może istnieć bez klasy do której własnie ten obiekt przyporządkowywujemy

Z przyporządkowania korzystamy, gdy dany obiekt jest częścią innego obiektu.

Z dziedziczenia korzystamy, gdy obiekt jest podtypem drugiego obiektu.

Konto Bankowe ma użytkowników, ale konto z minimalną wartością balansu jest podtypem konta.

Co oznacza, że w pierwszym przypadku należy zastosować przyporządkowanie, a w drugim z dziedziczenia.
cuboid
'''


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def count_surface_area(self):
        return self.a*self.b


class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)


class Cube(Square):
    def count_surface_area(self):
        return ((self.a*self.b)*6)

    def count_volume(self):
        return ((self.a*self.b)*self.a)


class Cuboid():
    def __init__(self, figure, height):
        self.base = figure
        self.height = height

    def count_volume(self):
        return self.base.count_surface_area() * self.height


square = Square(3)
cube = Cube(2)
cuboid = (Cuboid(Rectangle(2, 3), 4))
print(square.count_surface_area())

print(cube.count_surface_area())
print(cuboid.count_volume())
