x = int(input("nombre de ligne"))

def suite (x):
    compteur = 0
    code = "1"
    ligne_suivante = ""
    for j in range(x) :
        for i in code :
            a = i
            if a == i+1 :
                compteur += 1
            else :
                ligne_suivante += compteur,a
        f.write(ligne_suivante)












f = open('SuiteDeFibo2.txt','w')
f.write(suite(x))