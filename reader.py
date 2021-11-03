# le parametre d'entrer c'est "liste"

def mise_en_forme():
    nb_of_letter_max = 0
    for i in range(len(liste)):
        for j in range(len(liste[i])):
            temp = len(liste[i][j])
            if temp > nb_of_letter_max:
                nb_of_letter_max = temp


    for i in range(len(liste)):
        for j in range(len(liste[i])):
            print(liste[i][j], " " * (nb_of_letter_max - len(liste[i][j])), "|")
