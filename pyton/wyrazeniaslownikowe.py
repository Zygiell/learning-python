

names = {"Arkadiusz", "Wioletta", "Karol", "Bartłomiej", "Jakub", "Ania"}

numbers = [1, 2, 3, 4, 5, 6]

celcius = {'t1': -20, 't2': -15, 't3': 0, 't4': 12, 't5': 24}

namesLength = {
    name : len(name)
    for name in names
    if name.startswith("A")
}
print(namesLength)


multiNumbers = {
    number : number**2
    for number in numbers
    }
print(multiNumbers)



ftemp = {
    key: value*1.8 + 32
    for key, value in celcius.items()
    if value > -5
    if value < 20
    }
