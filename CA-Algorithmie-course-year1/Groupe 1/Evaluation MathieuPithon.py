Tableau2dimensionCoordonnées = []
Tableau2dimensionSomme =[]
print("somme des coordonnées de la case: ")
for x in range(10):
    Tableau2dimensionSomme.append([])
    tableautemporaire =[]
    for y in range(10):
        Tableau2dimensionSomme[x].append(0)
        tableautemporaire.append((x+y))
    Tableau2dimensionCoordonnées.append(tableautemporaire)
    print(tableautemporaire)

print("\n somme des coordonnées adjacente:")
for horizontalIndex in range(10):
    for verticalIndex in range(10):
        if horizontalIndex < 9:
            Tableau2dimensionSomme[horizontalIndex][verticalIndex] += Tableau2dimensionCoordonnées[horizontalIndex+1][verticalIndex]
        if horizontalIndex > 0:
            Tableau2dimensionSomme[horizontalIndex][verticalIndex] += Tableau2dimensionCoordonnées[horizontalIndex-1][verticalIndex]
        if verticalIndex < 9:
            Tableau2dimensionSomme[horizontalIndex][verticalIndex] += Tableau2dimensionCoordonnées[horizontalIndex][verticalIndex+1]
        if verticalIndex > 0:
            Tableau2dimensionSomme[horizontalIndex][verticalIndex] += Tableau2dimensionCoordonnées[horizontalIndex][verticalIndex-1]
    print(Tableau2dimensionSomme[horizontalIndex])