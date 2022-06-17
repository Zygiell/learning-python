'''
Gra w życie:
Klasa klient  rodzi się z przypisaną wartością szczęścia od 0 - 100 każdy klient ma bankroll startowy równy 100 zł
10 klientów przebywa w kasynie- kasyno jest otwarte do ostatniego klienta, klient wychodzi z kasyna jak straci wszystkie swoje pieniądze
W kasynie jest jedna gra, slot machine
Gra polega na :
Człowiek ma poziom szczęścia w grze wynosi(wartość_szczescia 0-100 random) * 0.10
Wygrana 9 zł
koszt gry 1 zł
W kasynie jest tylko jedna maszyna jednocześnie może grać jeden klient, co każdą grę miejsce przy maszynie zajmuje losowy klient przebywający w kasynie.
Co gre  print info : Kto grał, czy wygrał? ile ma pieniędzy po grze.
na koniec print ile razy gra została zagrana 


'''
import random

# TO JEST TYLKO SZABLON DEBILU!!!!!!!!!


class Casino:
    def __init__(self):
        self.clients = []

    def let_client_in(self, client):
        self.clients.append(client)

    def who_plays_the_game(self):
        self.player = random.choice(self.clients)
        return self.player

    def play_game(self):
        self.player.wallet -= 1
        playerWinChance = self.player.luck * 0.10
        slotMachineResult = random.uniform(0, 100)
        if playerWinChance >= slotMachineResult:
            self.player.wallet += 9
            print(
                f'Player: {self.player.name} wins! Players wallet balance after game : {self.player.wallet}')
        else:
            print(
                f'Player: {self.player.name} lost! Player wallet balance after game : {self.player.wallet}')

    def player_kicker(self):
        for player in self.clients:
            if player.wallet <= 0:
                self.clients.remove(player)

    def __str__(self):
        return f'There are {len(self.clients)} clients in The Casino'


class Client:
    def __init__(self, name):
        self.luck = random.randint(1, 100)
        self.name = name
        self.wallet = 100

    def __str__(self):
        return f'Hello! my name is {self.name} i ve got {self.wallet} in my wallet, and my luck value is {self.luck}'


casino = Casino()

clientList = [Client('Janus'), Client('Michael'), Client('Lucy'), Client('Violette'),
              Client('Hiragi'), Client('Kirito'), Client('Miguel'),
              Client('Dexter'), Client('Rita'), Client('Samantha')]

gamecounter = 0

for client in clientList:
    casino.let_client_in(client)

while len(casino.clients) > 0:
    casino.who_plays_the_game()
    casino.play_game()
    casino.player_kicker()
    gamecounter += 1
print(f'Game over, everyone lost their money, it took {gamecounter} times')
