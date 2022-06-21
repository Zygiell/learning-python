from unittest import removeResult
from cwiczeniebankaccount import MinBalanceAccount
'''
CWICZENIE 1
konto = BankAccount()

amountToWithdraw = 777

konto.deposit(500)


result = konto.try_withdraw(amountToWithdraw)

if result.isSuccess:
    print(result.message)
    print('cos od siebie')
else:
    print(result.message)
    print('cos od siebie')
'''
'''
dziedziczenie super()
KLASA RODZIC - KLASA DZIECKO
super klasa -   sub klasa

    POTWÓR - super klasa:
SZKIELET, ZOMBIE - sub klasy (mają cechy wspólne np HP - cechy
wspólne są w super klasie POTWÓR)
'''
accountMin = MinBalanceAccount(1500, 1000)

result = accountMin.try_withdraw(1)

if result.is_ok():
    print(result.message)
