'''


1. extract data from https://jsonplaceholder.typicode.com/todos
2. code program that defines which userID succesfully completed most tasks
3. change program elements in functions
4. change function in to universal function
5. make code self describing


'''

import requests
import json
from collections import defaultdict
a = defaultdict(str)
print(type(a['lal']))
print(a)
response = requests.get("https://jsonplaceholder.typicode.com/todos")
tasks = response.json()


def highest_value_key_in_dict(dict_name):
    keysWithHighestValue = []
    for key, value in dict_name.items():
        if value == max(dict_name.values()):
            keysWithHighestValue.append(key)
    return keysWithHighestValue


def completed_tasks_frequency(tasks):
    completedTasksFrequencyByUser = defaultdict(int)
    for entry in tasks:
        if entry['completed'] == True:
            completedTasksFrequencyByUser[entry['userId']] += 1

    return completedTasksFrequencyByUser


def user_id_with_most_completed_tasks(completedTaskFreq):
    usersWithMostCompletedTasks = []
    for key, value in completedTaskFreq.items():
        if value == max(completedTaskFreq.values()):
            usersWithMostCompletedTasks.append(key)
    return usersWithMostCompletedTasks


completedTaskFreq = completed_tasks_frequency(tasks)
usersWithTopCompletedTasks = user_id_with_most_completed_tasks(
    completedTaskFreq)
print(usersWithTopCompletedTasks)


response = requests.get("https://jsonplaceholder.typicode.com/users")
users = response.json()
print(users)

for user in users:
    if user['id'] in usersWithTopCompletedTasks:
        print('Wręczamy ciasteczko mistrzunia dyscypliny o imieniu ',
              user["name"])

# sposob 2

for useId in usersWithTopCompletedTasks:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/"+str(useId))
    user = response.json()
    print('Wręczamy ciasteczko mistrzunia dyscypliny o imieniu ',
          user["name"])

# sposob 3


def change_list_into_conj_of_param(my_list, key='id'):
    conj_param = 'id='
    lastIteration = len(my_list)
    i = 0
    for item in my_list:
        i += 1
        if i == lastIteration:
            conj_param += str(item)
        else:
            conj_param += str(item)+'&' + key + '='
    return conj_param


conj_param = change_list_into_conj_of_param([2, 3, 5])
response = requests.get(
    "https://jsonplaceholder.typicode.com/users", params=conj_param)
users = response.json()
for user in users:
    print('Wręczamy ciasteczko mistrzunia dyscypliny o imieniu ',
          user["name"])
