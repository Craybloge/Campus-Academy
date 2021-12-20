import random
liste=[]
longueurliste=20
for i in range (longueurliste):
    liste.append(random.randint(1,100))
print(liste)
i=0
compteur=0
permute= True

while permute:
    permute=False
    for i in range(len(liste)-1):
            if liste[i]>liste[i+1]:
                permute= True
                a=liste[i]
                liste[i]=liste[i+1]
                liste[i+1]=a
                print(liste)
        
    else:
        while i>0:
            compteur+=1
            if liste[i]<liste[i-1]:
                permute=True
                a=liste[i]
                liste[i]=liste[i-1]
                liste[i-1]=a
                print(liste)
            i-=1
        
    

print(liste)