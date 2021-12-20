f = open("myfile.txt", "w")
ligne ="1"
longueur = int(input("nombre de ligne voulu:"))
f.write(ligne +"\n")
print(ligne)
for i in range(longueur):
    f.write(ligne + "\n")
    compteur=1
    x= ""
    for j in range(len(ligne)):
        if j>0:
            if ligne[j]==ligne[j-1]:
                compteur+=1
            else :
                x+=str(compteur)+str(ligne[j-1])
                compteur=1
        if len(ligne)==j+1:
            x+=str(compteur)+str(ligne[j])
    print(x)
    ligne=x