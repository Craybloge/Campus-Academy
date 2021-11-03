# le parametre d'entrer c'est "liste"

liste = (["dsfsdsdfsd", "FKEPJFPZdddddddddddddddddddddFfjfiez", "sdvvzefz"],
         ["zefzfzfefz", "dzfsdvze"])


def mise_en_forme(liste):
    liste_nb_max = [0]*len(liste[0])
    temp = [0]*len(liste[0])
    for i in range(len(liste)):
        for j in range(len(liste[i])):
            temp[j] = len(liste[i][j])
            if temp[j] > liste_nb_max[j] :
                liste_nb_max[j] = temp[j]

    for i in range(len(liste)):
        print(" ")
        for j in range(len(liste[i])):
            print(" ", liste[i][j], " " *
                  (liste_nb_max[j] - len(liste[i][j])), "|", end="")


mise_en_forme(liste)