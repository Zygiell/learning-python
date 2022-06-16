string_ = 'This website is for losers LOL!'
vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
lista = string_.split()
corrected = []

for element in lista:
    for litera in element:
        if litera in vowel:
            corrected.append(element.replace(litera, ""))
print(corrected)
