import abc;

class Team(abc.ABC):
    @abc.abstractmethod
    def __init__(self, members):
        # members est un tableau
        self._members = members;

    def __len__(self):
        # retourne la longueur du tableau
        return len(self._members);

    # retourne le membre selon l'index donné en paramètre
    def __getitem__(self, index):
        return self._members(index);
