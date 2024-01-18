class Player:
    def __init__(self, name):
        self.__name = name
        self.__health = 10
        self.__damage = 2
        self.__class = "NULL"

    def getHealth(self):
        return self.__health

    def setHealth(self, newhealth):
        self.__health = newhealth

    def getname(self):
        return self.__name

    def setname(self, newname):
        self.__name = newname

    def takeDamage(self, damage):
        self.__health = self.__health - damage

