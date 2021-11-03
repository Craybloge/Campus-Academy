import random, pypokedex, copy
from os import system, name
from pprint import pprint
import inquirer
from pokemon import Pokemon as Poke
from pokeball import Pokeball as Ball


class Game():

    def __init__(self, pokelist):  
        self.pokepool = pokelist      
        self.starter = copy.copy(Poke.spawn(self.pokepool))
        self.pokedex = [self.starter]
        self.money = 2000
        self.inventory = {"pokeball" : 10, "superball" : 1, "hyperball" : 2, "masterball": 1}
        
    def journey(self):
    #la méthode qui affiche le menu principal et qui redirige le joueur
        game.clear()
        question = [
        inquirer.List(
            "menu",
            message="souhaitez vous aller combattre un pokémon sauvage ou aller acheter des pokeballs à la boutique?",
            choices=["Aventure", "Boutique", "Voir inventaire", "Quitter le jeu"],
            ),
        ]
        choix = inquirer.prompt(question)
        if choix["menu"] == "Aventure":
            self.encounter()
        elif choix["menu"] == "Boutique":
            self.shop()
        elif choix["menu"] == "Voir inventaire":
            self.inventaire()
            x = input("retour")
            self.journey()
        elif choix["menu"] == "Quitter le jeu":
            quit()

    def encounter(self):
    #la méthode qui fait apparaitre un pokémon en face de nous
        self.pokemonSauvage = copy.copy(Poke.spawn(self.pokepool))
        self.combatOptions()

    def combatOptions(self):
    #la méthode qui affiche les options quand on se retrouve face à un pokémon
        print("-----------------------------------------------------------------")
        questions = [
            inquirer.List(
                "choix",
                message="vous vous retrouvez face à un " +  self.pokemonSauvage.pokemon.name + " sauvage de rareté " + str(self.pokemonSauvage.spawnrate) + ", que faites vous?",
                choices=["observer le pokémon", "combattre", "capturer", "voir inventaire", "fuir"],
            ),
        ]

        answer = inquirer.prompt(questions)
        if answer["choix"] == "observer le pokémon":
            print("vous observez le pokémon, vous décrivez ce que vous pouvoir voir en face de vous: \n", self.pokemonSauvage)
            print("\n\n\n")
            self.combatOptions()
        elif answer["choix"] == "combattre":
            self.combat()
        elif answer["choix"] == "capturer":
            self.capture()
        elif answer["choix"] == "voir inventaire":
            self.inventaire()
            self.combatOptions()
        elif answer["choix"] == "fuir":
            self.fuite()

    def inventaire(self):
    # c'est la méthode qui affiche l'inventaire
        print("liste de vos pokémons:")
        print("---------------------------------")
        for i in self.pokedex:
            print(i)

        print("---------------------------------")  
        print("liste de votre inventaire:")
        print("---------------------------------") 
        for i in self.inventory:
            print(i, ": ", self.inventory[i])
        print("---------------------------------")
        print("vous possédez ", self.money, " pokedollars")

    def combat(self):
    #méthode qui gère l'affrontement entre les pokémons du joueur de le pokémon sauvage
        print("-----------------------------------------------------------------")
        question = [
            inquirer.List(
                "pokemon",
                message="quel pokémon souhaitez vous envoyer au combat: ",
                choices=self.pokedex,
            ),
        ]

        combatPokemon = inquirer.prompt(question)
        combatPokemon = combatPokemon["pokemon"]
        print(combatPokemon.pokemon.name, "! à l'attaque!")
        ratio = (self.pokemonSauvage.resistance * self.pokemonSauvage.damage - combatPokemon.resistance * combatPokemon.damage)//100
        if random.randint(0, (100 + ratio)) > 50:
            print("combat perdu, votre pokémon est ko!, le temps qu'il se réveille, ", self.pokemonSauvage.pokemon.name, " s'est enfui!")
        else:
            print("combat gagné, vous avez démoli le pokémon sauvage et vous avez gagné ", self.pokemonSauvage.resistance * self.pokemonSauvage.damage//4 + (5000//self.pokemonSauvage.spawnrate), "pokedollars")
            self.money += ((self.pokemonSauvage.resistance * self.pokemonSauvage.damage)//4) + (5000//self.pokemonSauvage.spawnrate)

    def fuite(self):
    #tout simplement la méthode qui affiche la fuite
        print("vous prenez la fuite!")

    def capture(self):
    #méthode qui gère la capture d'un pokémon et le choix de la pokéball
        print("-----------------------------------------------------------------")
        pokeballList = {}
        for i in self.inventory:
            if self.inventory[i] != 0:
                pokeballList[i] = self.inventory[i]
        pokeballList["annuler"] = "annuler"
        question = [
        inquirer.List(
            "pokeball",
            message="quelle pokeball souhaitez vous utiliser?: ",
            choices=pokeballList,
            ),
        ]
        pokeball = inquirer.prompt(question)
        if pokeball["pokeball"] == "annuler":
            self.combatOptions()
        else:
            pokeball = Ball(pokeball["pokeball"])
            self.inventory[pokeball.name] -= 1
            print("vous lancez une ", pokeball.name, " sur ", self.pokemonSauvage.pokemon.name, "!")
            if pokeball.tryCatch(self.pokemonSauvage):
                print("félicitation! le pokémon est capturé et il est ajouté à votre pokédex!")
                self.pokedex.append(self.pokemonSauvage)
            else:
                print("la tentative échoue! le pokémon se libère, voulez vous réessayer ou tenter autre chose?")
                question = [
                inquirer.List(
                    "choix",
                    message="la tentative échoue! le pokémon se libère, voulez vous réessayer ou tenter autre chose?",
                    choices=["réessayer", "retour aux choix"],
                    ),
                ]
                answer = inquirer.prompt(question)
                if answer["choix"] == "réessayer":
                    self.capture()
                else:
                    self.combatOptions()
    
    def shop(self):
    #la méthode qui crée la boutique
        print("-----------------------------------------------------------------")
        question = [
            inquirer.List(
                "shop",
                message="Bienvenue dans mon humble boutique, voici ce que vous pouvez acheter (votre argent: " + str(self.money) + "$)",
                choices=["pokéball : 200$", "superball: 600$", "hyperball: 1200$", "masterball: 50 000$", "retour au choix"],
                ),
        ]
        achat = inquirer.prompt(question)["shop"]
        if achat == "pokéball : 200$":
            self.achat("pokeball", 200)
        elif achat == "superball: 600$":
            self.achat("superball", 600)
        elif achat == "hyperball: 1200$":
            self.achat("hyperball", 1200)
        elif achat == "masterball: 50 000$":
            self.achat("masterball", 50000)
        else:
            self.journey()

    def achat(self, pokeball, prix):
    #méthode qui gère l'achat des objets, l'inventaire et l'argent
        print("-----------------------------------------------------------------")
        if prix > self.money:
            print("vous n'avez pas assez d'argent!")
            self.shop()
        else:
            quantity = int(input("quelle quantité de " + pokeball + " souhaitez vous acheter?"))
            print(quantity, pokeball, ", ça vous fera ", quantity * prix, "$")
            if quantity * prix > self.money:
                print("vous n'avez pas assez d'argent!")
                self.achat(pokeball, prix)
            else:
                self.money -= quantity*prix
                self.inventory[pokeball] += quantity
                question = [
                    inquirer.List(
                        "shop",
                        message="Votre Achat a été validé, que souhaitez vous faire?",
                        choices=["continuer les achats", "retour au menu"],
                        ),
                ]
                choix = inquirer.prompt(question)["shop"]
                if choix == "continuer les achats":
                    self.shop()
                else:
                    self.journey()

    def clear(self):
    #permet me clear la console
        if name == 'nt':
            _ = system('cls')


# lancement du script, génère le pool de pokémon puis lance le jeu
if __name__ == "__main__" :
    sum = 0
    pokeliste = {}
    for i in range (1, 898):
        pokeliste[i] = Poke(i)
        print(pokeliste[i].pokemon.name)
        sum += pokeliste[i].spawnrate

    game = Game(pokeliste)
    print("votre starter est: ", game.starter.pokemon.name, " et sa rareté est: ", game.starter.spawnrate)

    while True:
        game.journey()
        

