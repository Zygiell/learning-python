'''


1. extract data from https://jsonplaceholder.typicode.com/todos
2. code program that defines which userID succesfully completed most tasks
3. change program elements in functions
4. change function in to universal function
5. make code self describing


'''

import requests
import json

r = requests.get('https://jsonplaceholder.typicode.com/todos')
tasks = r.json()

userIDvalue = dict()
usersWithBestScore = []

for entry in tasks:
    if entry['completed'] == True:
        try:
            userIDvalue[entry['userId']] += 1
        except KeyError:
            userIDvalue[entry['userId']] = 1
print(userIDvalue)

for key, value in userIDvalue.items():
    if value == max(userIDvalue.values()):
        usersWithBestScore.append(key)
print(usersWithBestScore)
