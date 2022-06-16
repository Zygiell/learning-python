'''
yield - z ang. dostarczyć, dać, wydać z siebie

'''


def generate_even_numbers():

    for element in range(400):

        if (element % 2) == 0:
            yield element


evenNumberGenerator = (element
                       for element in range(400)
                       if element % 2 == 0)

a = generate_even_numbers()
c = []
for e in range(100):
    c.append(next(a))
print(c)


def generate_10_numbers():
    x = 0
    while True:
        yield x
        x += 1


print(list(generate_10_numbers()))
