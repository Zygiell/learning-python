import sys

evenNumbers = [element
               for element in range (400)
               if (element % 2 == 0)
               ]
evenNumbersGenerator = (element**2
                        for element in range (100)
                        )
print(evenNumbersGenerator)

print(evenNumbersGenerator)

for item in evenNumbersGenerator:
    print(item)
