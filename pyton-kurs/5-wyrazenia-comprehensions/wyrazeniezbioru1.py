

names = {"arkadiusz", "wioletta", "Karol", "Bartłomiej", "Jakub", "Ania"}


names = {name.capitalize()
        for name in names
        if name[0] != "B"
}

