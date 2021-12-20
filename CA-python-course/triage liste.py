import random
liste=[]
longueurliste=20
for i in range (longueurliste):
    liste.append(random.randint(1,100))
compteur=0
liste2= []
for i in range(longueurliste):
    a=liste[0]
    for i in range(1,len(liste)):
        compteur+=1
        if liste[i]<a:
            a= liste[i]
    liste2.append(a)
    liste.remove(a)
    print(liste,liste2)
print (compteur)
print(liste2)

