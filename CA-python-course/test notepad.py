liste = [1, 4 ,9 ,16 ,25 ,36 ,49 ,64 ,100 ,121]
def premier (liste):
    tot=[]
    for i in range (len(liste)):
        liste[i]= str(liste[i])
        tot.append(liste[i][0])
    return(tot)

def comptage_chiffre (liste):
    retour=premier(liste)
    total =  {str(j):0 for j in range(1,10)}
    print(total)
    for i in retour:
        total[i]+=1
    return(total)



print(comptage_chiffre(liste))



print([i for i in range(1,10) if i !=3])





def carre (x):
    for i in range(x-1,0,-1):
        x*=i
        print(x)
    return(x)


print(carre(int(input())))
