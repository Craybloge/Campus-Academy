class Tabouret: 
    def __init__ (self, nombre_pieds, diametre_assise, hauteur_pieds): 
        self.nombre_pieds = nombre_pieds 
        self.diametre_assise = diametre_assise 
        self.hauteur_pieds = hauteur_pieds 
        self.calcul_longueur_pieds = self.calcul_longueur_pieds() 
    def plier(self):
        return "je me pile"
    def deplier(self): 
        return "je me deplie" 
    def calcul_longueur_pieds(self): 
        return self.nombre_pieds * self.hauteur_pieds 
t =Tabouret(2, 4 ,10)
print(t.nombre_pieds, t.diametre_assise, t.hauteur_pieds) 
t.nombre_pieds = 5 
print(t.nombre_pieds, t.diametre_assise, t.hauteur_pieds) 