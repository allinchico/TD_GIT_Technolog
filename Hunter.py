import random
class Hunter:

    def __init__(self):
        self.__degat = random.choice(range(1,2))
        self.__chance = 10
        self.__fuite = 20
        self.__prix = 25
        self.__unit= "hunter"