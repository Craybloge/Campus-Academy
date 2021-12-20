import random, string, time

class Bruteforce():

    def __init__(self):
        self.timeStart = time.time_ns()           
        self.ascii = string.printable
        self.longueur = 3
        self.password = self.passwordGenerator()
        
        

    def passwordGenerator(self):
        return "".join(random.sample(self.ascii, self.longueur))

    def __repr__(self):
        return self.password
    

    def recursive(self, index=""):
        for i in self.ascii:
            self.passwordTest(index + i)
            if len(index + i) < len(self.password) :
                self.recursive(index + i)

    
    def passwordTest(self, test):
        print(test, self.password)
        if test == self.password:
            print("la détection de mot de passe a mis :  ", (int(time.time_ns()) - int(self.timeStart))/1000000000, " s")
            print("le mot de passe était: ", test)
            exit()


if __name__ == "__main__" :
    test = Bruteforce()
    print("le mot de passe est : ", test)
    test.recursive()


