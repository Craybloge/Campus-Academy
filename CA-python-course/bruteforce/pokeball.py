import random
from CONSTANTE import BALLDATA


class Pokeball():
    max = 0

    def __init__(self, name):         
        self.name = name
        self.basePower = BALLDATA[name][0]
        self.type = BALLDATA[name][1]

    def __repr__(self):
    #c'est la méthode qui permet de gérer ce qui va s'afficher quand on va utiliser la fonction print sur l'objet
        return ("name: " + self.name + "  type: " + self.type + "   power: " + str(self.basePower))
    
    def tryCatch(self, pokemon):
    # c'est la méthode qui gère si la capture est un succès ou non
        chance = round(self.basePower // (pokemon.resistance/100))
        if self.type in pokemon.pokemon.types :
            #permet de gérer les pokéballs de type ayant un bonus sur un type particulier de pokémon (pour l'instant inutilisé)
            chance += 20
        if self.type == "master":
            return True
        if chance >= random.randint(0, 100):
            return True
        else:
            return False

    def special(self, chance):
    #c'est la fonction qui gère les effets des pokéballs spéciales (pour l'instant inutilisé)
        pass
