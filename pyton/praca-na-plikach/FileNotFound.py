def fileNotFound():
    fileName = input('Type name of file you want to read: \n')
    try:
        with open(str(fileName), 'r', encoding='UTF-8') as file:
            return print(file.read())
    except FileNotFoundError:
        return print('file with that name does not exist')


fileNotFound()
