'''
OOP - Object Oriented Programming

Programowanie zorientowane wokół obiektów

OBIEKT

OBIEKTY - to pojemniki do przechowywania zmiennych i funkcji tematycznie ze 
          sobą powiązanych do dalszego łątwiejszego ponownego użycia

Klasy - foremki (szablony) do tworzenia egzemplarzy obiektów

Atrybut - cecha opisująca obiekt
Metoda - funkcja, która operuje na obiekcie

Instancja klasy - instance , egzemplarz to obiegt, który wyszedł z formy (klasy)

self - z ang ja, sam , siebie w innych językach : this !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
'''

# klasa user (forma)


class User:  # z dużej Litery!!!
    age = 0
    name = ""
    # funkcja w klasie - METODA (musi być self)

    def print_age(self, message):
        print(message, self.name, 'wiek: ', self.age)


#User() - obiekty
userList = [User(), User()]

userList[0].age = 21
userList[0].name = "Franiu"
userList[0].print_age('Hello')

userList[1].age = 33
userList[1].name = "Wiola"
userList[1].print_age('Bonjur!')


user1 = User()
user1.name = "Arek"
user1.age = 16
user1.print_age("Hej")

user2 = User()
user2.name = "Mirek"
user2.age = 24
user2.print_age('Czesc')

user3 = User()
user3.name = "Seba"
user3.age = 31
user3.print_age('Witaj')
