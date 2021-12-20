"""
module docstring
"""
from .car import Car
from .engine import Engine


class Dealership:
    """
    class docstring
    """
    def __init__(self, brand, personel_nb, city, nb_models):
        self.brand = brand
        self.personel_nb = personel_nb
        self.city = city
        self.nb_models = nb_models
        self.voitures_en_vente = []
        self.liste_client = []

    # fonction permettant d'ajouter les voitures en vente par la concession
    def ajout_voiture(self, elements):
        """
        method docstring
        """
        return self.voitures_en_vente.append(Car([
            elements[0],
            elements[1],
            Engine(elements[3], elements[4]),
            self.brand,
            elements[2],
            elements[5]
            ]))

    def achat_voiture(self, name, firstname, date, model):
        """
        method docstring
        """
        self.liste_client.append([date, name, firstname, model])
        self.voitures_en_vente.remove(model)
