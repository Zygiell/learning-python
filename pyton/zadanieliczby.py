'''
Znajdź liczby od 100 do 470 włącznie, które są:
-podzielne przez 7, ale nie są podzielne przez 5
'''

numberDiv = [numbers
    for numbers in range(2, 471)
    if (numbers % 7 == 0)
    and (numbers % 5 != 0)    
    ]
print(numberDiv)

numberDivGenerator = (number
    for number in range (2, 471)
    if (number % 7 == 0) and (number % 5 != 0)
    )
for number in numberDivGenerator:
    print(number)
