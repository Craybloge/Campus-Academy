import random
liste=[]
for i in range(6):
    tempo= [random.randint(0,100)]
    for j in range(13):
        tempo+=[random.randint(0,100)]
    liste+=[tempo]
    print(tempo)

# print(liste)
tempo=[]
liste2=[]
a=True
for i in range(10):
    tempo.append(a)
    if a :
        a=False
    else:
        a=True
liste2.append(tempo)
for i in range (10):
    if tempo[0]:
        tempo.remove(True)
        tempo.append(True)
    else:
        tempo.remove(False)
        tempo.append(False)
    print(tempo)
    tempo2=tempo.copy()
    liste2.append(tempo2)

print(2**100)

