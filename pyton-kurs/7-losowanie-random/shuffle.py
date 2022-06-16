import random

cardList = ['9', '9', '9', '9',
            '10', '10', '10', '10',
            'Jack', 'Jack', 'Jack', 'Jack',
            'Queen', 'Queen', 'Queen', 'Queen',
            'King', 'King', 'King', 'King',
            'Ace', 'Ace', 'Ace', 'Ace']
random.shuffle(cardList)


def choose_random_numbers(amount, total_amount):
    x = set()
    while len(x) < amount:
        x.add(random.randint(1, total_amount))

    print(x)


choose_random_numbers(6, 48)
