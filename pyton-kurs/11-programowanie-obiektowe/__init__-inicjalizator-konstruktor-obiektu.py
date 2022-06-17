'''
__init__ - initialization - inicjalizacja - czyli ustawienie startowych
           wartości dla atrybutów
w innych językach __init__ to konstruktor

'''

# klasa user (forma)


class User:  # z dużej litery

    def __init__(self, age, name):
        self.age = age
        self.name = name
        self.ageInFuture = age + 1

    def print_age(self, message):
        print(message, self.name, 'wiek: ', self.age)


user1 = User(30, "Arek")
user2 = User(24, "Mirek")
user3 = User(31, "Seba")


user1.print_age("Hej")

user2.print_age('Czesc')

user3.print_age('Witaj')

print(user1.ageInFuture)
