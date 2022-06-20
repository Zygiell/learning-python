class User:
    lastUserid = 0

    def __init__(self, name=""):
        self.name = name
        User.lastUserid += 1
        self.id = User.lastUserid
