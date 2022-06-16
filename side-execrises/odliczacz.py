import time


def odliczacz(value):
    print('Pozostało', value, 'sekund')
    for i in range(1, value+1):
        time.sleep(1)
        value = value - 1
        print('Pozostało', value, 'sekund')
    return
