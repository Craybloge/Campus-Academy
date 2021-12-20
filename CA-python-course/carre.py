class Carre:
    counter=0
    def __init__ (self, cote):
        self.cote = cote
        self.aire = self.aire()
        self.perimeter = self.perimeter()
        self.__class__.counter += 1
        print(self.__class__)
    
    def __repr__ (self):
        return ("Le carré à un côté d'une longueur de {}, une aire de {}  et un périmètre de {}".format(self.cote,self.aire, self.perimeter))

    def __add__(self, carre):
        return Carre(self.cote +carre.cote) 

    def __sub__(self, carre):
        return Carre(self.cote -carre.cote) 

    def __int__ (self):
        return(self.cote)
    
    def __lt__(self,carre):
        return(self.cote<carre.cote)

    def aire(self):
        return self.cote**2
    
    def perimeter(self):
        return self.cote*4

    def factor(self,x):
        return Carre(x*self.cote)


if __name__ == "__main__":
    print("carré")
