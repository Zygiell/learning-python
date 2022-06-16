import time


def number_multiplied_by_itself_generator():
    i = 0
    while True:
        print('start', i)
        i += 1
        i = yield i*i
        print('end', i)


c = number_multiplied_by_itself_generator()
c.send(None)
dupa = []

for e in range(20):
    dupa.append(c.send(e))
    print(dupa)
print(dupa)
time.sleep(2)
for e in range(1, 20):
    dupa.append(c.send(e))
    print(dupa)
