import random;

class Warrior:

    def __init__(self):
        self.__degat = random.choice(range(3,5))
        self.__chance = 5
        self.__prix = 10
        self.__type = "warrior"
