'''
Stwórz konto bankowe, do którego można deponować pieniądze oraz wypłacać oraz będzie saldo

'''
import random
from result import Ok, Error


class BankAccount:  # rodzic

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def try_withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            return Ok("Money withdrawed",  amount)
        else:
            return Error("Not enough money",  self.balance)

    def __str__(self):
        return str(self.balance)


class MinBalanceAccount(BankAccount):  # dziecko
    def __init__(self, balance=0, minBalance=1000):
        super().__init__(balance)
        self.minBalance = minBalance

    def try_withdraw(self, amount):
        ifcounter = self.minBalance - amount
        if self.balance - amount < self.minBalance:
            print(
                f"Your withdraw request: {amount} is higher than your acc min balance : {self.minBalance} your balance: {self.balance}")
            if ifcounter >= 0:
                choice = input(
                    f'You can only withdraw: {ifcounter}, do you want to do it? y - yes n - no')
                if choice.lower() == 'y':
                    self.balance -= ifcounter
                    return Ok("Money withdrawed",  ifcounter)
                else:
                    return Error("Not enough money",  self.balance)
            else:
                return Error("Not enough money",  self.balance)
        else:
            return super().try_withdraw(amount)
