from Team import Team

class EnnemyTeam(Team) :
    def __init__(self, members,unit):
        super().__init__(members)
        self.__unit = unit
        self.__damage = 10
        self.__loot = 20

    def get_loot(self):
        return self.__loot

    def get_damage(self):
        return self.__damage

    def get_unit(self):
        return self.__unit