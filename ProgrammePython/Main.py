"""
Création d'un sapin
on peut changer les constantes pour faire varier le sapin, mais pour l'esthétisme
je recommande de modifier seulement:
- NUMBER_OF_BRANCH:
    le nombre de branches (le nombre de pyramide empilée si on veut)
- NUMBER_OF_TREES :
    le nombre d'arbres de noël à afficher.

BASE_WIDTH correspond à la largeur de base du sapin,
elle commence par défaut à 1 et augmente de 2 à chaque branche.

INCREMENTATION correspond à l'élargissement progressif des branches,
par défaut chaque branche s'élargira de 1 de plus que la précédente.

TOTAL_HEIGHT correspond à la hauteur totale actuelle du dessin,
elle commence donc à 0. NE PAS MODIFIER CETTE VALEUR.

MAX_WIDTH correspond à la taille maximale qu'atteindra le sapin,
elle sert à calculer le nombre d'espace nécessaire dans le tableau.

"""
import sys
import constant
NUMBER_OF_TREES = 2
NUMBER_OF_BRANCH = 8
INCREMENTATION = 1
MAX_WIDTH = int(((8 * NUMBER_OF_BRANCH + 3)) / 2)

def creation(drawing,MAX_WIDTH, width, INCREMENTATION, total_height, NUMBER_OF_BRANCH):
    """
    ff
    """
    drawing = adding_star(drawing, MAX_WIDTH)
    total_height = 7
    #creation of the leaves
    height = 4

    for branches in range(NUMBER_OF_BRANCH):
        base_width = width
        spaces = 2 * int(MAX_WIDTH / 2)+2 - width
        for line in range(height):
            if line == 0:
                spaces += ((INCREMENTATION+branches)-1)
            drawing.append([])
            for position in range(spaces):
                drawing[line + total_height].append(" ")
            for position in range(width):
                drawing[line + total_height].append("*")
            for position in range(spaces):
                drawing[line + total_height].append(" ")
            spaces -= INCREMENTATION+branches
            print(spaces)
            width += (INCREMENTATION+branches) * 2
        total_height += height
        width = base_width+2

    
# def trunk_and_wreath(drawing,)
    #creation of the trunk and wreath
    for line in range(3):
        drawing.append([])
        if line != 2:
            #creation of the wreath
            if line == 0:
                spaces += INCREMENTATION+branches
                wreath = "|"
            elif line == 1:
                wreath = "0"
            for rows in range(spaces):
                drawing[line + total_height].append(" ")
            for rows in range(MAX_WIDTH*2-3):
                if rows%2 == 1 and not(len(drawing[line + total_height]) >= spaces+(MAX_WIDTH-5) and len(drawing[line + total_height]) < spaces+(MAX_WIDTH+2)):
                    drawing[line + total_height].append(wreath)
                if rows%2 == 0 and not(len(drawing[line + total_height]) >= spaces+(MAX_WIDTH-4) and len(drawing[line + total_height]) < spaces+(MAX_WIDTH+1)):
                    drawing[line + total_height].append(" ")
                if len(drawing[line+total_height]) >= spaces+(MAX_WIDTH-4) and len(drawing[line+total_height]) < spaces+(MAX_WIDTH+1):
                        drawing[line+total_height].append("*")
            for rows in range(spaces):
                drawing[line + total_height].append(" ")


        else:
            #creation of the trunk
            for row in range(spaces+(MAX_WIDTH-4)):
                drawing[line + total_height].append(" ")
            for row in range(5):
                drawing[line + total_height].append("*")
            for row in range(spaces+(MAX_WIDTH-4)):
                drawing[line + total_height].append(" ")
    drawing = adding_baubles(drawing)
    return drawing

def adding_star(drawing, MAX_WIDTH):
    spaces = MAX_WIDTH-5
    star_spaces = 4
    for line in range(7):
        drawing.append([])
        for rows in range(spaces):
            drawing[line].append(" ")
        if line < 2:
            for rows in range(4-star_spaces):
                drawing[line].append(" ")
            drawing[line].append("*")
            for rows in range(2):
                for rows in range(star_spaces):
                    drawing[line].append(" ")
                drawing[line].append("*")
            for rows in range(4-star_spaces):
                drawing[line].append(" ")
            star_spaces -= 2
        if line == 3:
            for rows in range(11):
                if rows%2 == 0:
                    drawing[line].append("*")
                else:
                    drawing[line].append(" ")
        if line in (4,2):
            for rows in range(5):
                drawing[line].append(" ")
            drawing[line].append("*")
            for rows in range(5):
                drawing[line].append(" ")
        if line == 5:
            for rows in range(2):
                drawing[line].append(" ")
            drawing[line].append("*")
            for rows in range(2):
                drawing[line].append(" ")
            drawing[line].append("|")
            for rows in range(2):
                drawing[line].append(" ")
            drawing[line].append("*")
            for rows in range(2):
                drawing[line].append(" ")
        if line == 6:
            drawing[line].append("*")
            for rows in range(4):
                drawing[line].append(" ")
            drawing[line].append("|")
            for rows in range(4):
                drawing[line].append(" ")
            drawing[line].append("*")
        for rows in range(spaces):
            drawing[line].append(" ")
    return drawing

def adding_baubles(drawing):
    for line in range(7, len(drawing) - 5):
        for rows in range(len(drawing[line]) - 1):
            if drawing[line][rows] == '*':
                if drawing[line + 1][rows] == " ":
                    if drawing[line][rows - 1] == " " or drawing[line][rows + 1] == " ":
                        drawing[line + 1][rows] = "0"
    return drawing

def printing(drawing, NUMBER_OF_TREES):
    for i in drawing:
        for _ in range(NUMBER_OF_TREES):
            for j in i:
                print(j, end="")
        print('')

drawing= []
total_height = 0
base_width = 1
args = sys.argv

if len(args) >= 2:
    NUMBER_OF_BRANCH = int(args[1])
if len(args) >= 3:
    NUMBER_OF_TREES = int(args[2])

tree= creation(drawing, MAX_WIDTH, base_width, INCREMENTATION, total_height, NUMBER_OF_BRANCH)
printing(tree, NUMBER_OF_TREES)
