"""
module docstring
"""
from classes.dealership import Dealership
from classes.customer import Customer
from classes.supplier import Supplier
from constants import LIST_CARS, CAR_DEALERSHIP


class Main:
    """
    class docstring
    """

    def __init__(self):
        self.supplier = None
        self.customer = {}
        self.model = {}
        self.suppliers = {}
        self.dealership = None
        self.set_objects_from_datas()
        self.main_loop()

    def set_objects_from_datas(self):
        """
        function docstring
        """
        self.dealership = Dealership(*CAR_DEALERSHIP)
        for ele in LIST_CARS:
            self.dealership.ajout_voiture(ele)
        for car in self.dealership.voitures_en_vente:
            self.model[car.model] = car

    def choix_supplier(self):
        """
        furnishing docstring
        """
        self.supplier = input("choisissez le supplier: ")
        if self.supplier in self.suppliers:
            print("nous connaissons déja ce supplier")
        else:
            print(
                "c'est la première fois que l'on commerce avec"
                " ce supplier, on va l'enregistrer"
            )
            self.suppliers[self.supplier] = Supplier(
                self.supplier,
                input("choisissez la localisation de l'usine: "),
                input("donnez la nationalité du supplier: ")
            )

    def choix_modele(self):
        """
        mod choice docstring
        """
        mod = input("saisissez le modèle de la voiture:")
        if mod in self.model:
            print(
                "on a déja acheté ce type de modèle,"
                " il a été acheté automatiquement")
            self.dealership.ajout_voiture([
                self.model[mod].price,
                self.model[mod].wheel,
                self.model[mod].color,
                self.model[mod].engine.horsepower,
                self.model[mod].engine.fuel,
                self.model[mod].model
            ])
            self.suppliers[self.supplier].historique_achat_supplier(
                self.model[mod])
        else:
            print("ce modèle n'existe pas encore, on va le créer:")
            self.model[mod] = self.dealership.ajout_voiture([
                int(input("choisissez le prix:")),
                input("saisisssez le type de roue: "),
                input("saissez la couleur de la voiture:"),
                int(input("choisissez la puissance du moteur: ")),
                input("choisissez le carburant du moteur:"),
                mod
            ])
            self.suppliers[self.supplier].historique_achat_supplier(
                self.model[mod])

    def buy(self):
        """
        buy method docstring
        """
        print("on va maintenant vous proposer d'ajouter la nouvelle voiture:")
        self.choix_supplier()
        self.choix_modele()

    def sell(self):
        """
        selling method docstring
        """
        name = input("name du client:")
        if name in self.customer:
            print("le client est déja dans notre base de donnée:")
        else:
            self.customer[name] = Customer(name, input("prénom du client:"))
        self.customer[name].achat(
            input("date d'achat (jj/mm/aaaa):"),
            self.dealership.voitures_en_vente[
                int(input("index de la voiture:"))
                ]
        )
        self.dealership.achat_voiture(
            self.customer[name].name,
            self.customer[name].firstname,
            self.customer[name].last_buy[1],
            self.customer[name].last_buy[0]
            )
        print(self.customer[name].last_buy)
        print(self.customer[name].__dict__)

    def main_loop(self):
        """
        mainloop docstring
        """
        while True:
            print("\n \n voici la liste des voitures en vente: ")
            for car in self.dealership.voitures_en_vente:
                print(car.__dict__)
            # choix de l'utilisateur
            user_input = input("tapez achat, vente, listea, listev ou quit : ")
            # ajout d'une voiture dans la liste des voitures Ã  vendre
            if user_input == "achat":
                self.buy()
            # ajout d'une vente dans l'historique d'achat
            elif user_input == "vente":
                self.sell()
            # affichage de l'historique d'achat
            elif user_input == "listea":
                print("voici la liste des voitures achetées :")
                print(self.dealership.liste_client)

            # affichage de la liste des voitures en vente
            elif user_input == "listev":
                pass
            # mettre fin au programme
            elif user_input == "quit":
                break

            # check si il a écrit un truc correc
            else:
                print("vous n'avez pas tapé qqch de correct")


if __name__ == "__main__":
    Main()