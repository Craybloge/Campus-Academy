
def creation(drawing, maxWidth,width, incrementation, totalHeight, numberOfBranch):

    #creation of the leaves
    baseWidth = width
    height = 4
    spaces = 2*int(maxWidth/2)-width
    for line in range(height):
        if line == 0:
            spaces += (incrementation-1)
        drawing.append([])
        for position in range(spaces):
            drawing[line + totalHeight].append(" ")
        for j in range(width):
            drawing[line + totalHeight].append("*")
        for position in range(spaces):
            drawing[line + totalHeight].append(" ")
        spaces -= incrementation
        width += incrementation*2
    numberOfBranch -= 1
    totalHeight +=height
    if numberOfBranch >0:
        creation(drawing, maxWidth, baseWidth+2,incrementation+1, totalHeight, numberOfBranch)
    else:
        #creation of the trunk and wreath
        for line in range(3):
            drawing.append([])

            if line !=2:
                #creation of the wreath
                if line == 0:
                    wreath = "|"
                    width -= incrementation*2
                    spaces += incrementation
                elif line == 1:
                    wreath = "0"
                
                for position in range(spaces):
                    drawing[line+totalHeight].append(" ")
                for position in range(width):
                    if position%2 == 1 and not(len(drawing[line+totalHeight]) >= spaces+(int(width/2)-2) and len(drawing[line+totalHeight]) < spaces+(int(width/2)+4)):
                        drawing[line+totalHeight].append(wreath)
                    if position%2 == 0 and not(len(drawing[line+totalHeight]) >= spaces+(int(width/2)-2) and len(drawing[line+totalHeight]) < spaces+(int(width/2)+3)):
                        drawing[line+totalHeight].append(" ")
                    if len(drawing[line+totalHeight]) >= spaces+(int(width/2)-2) and len(drawing[line+totalHeight]) < spaces+(int(width/2)+3):
                        drawing[line+totalHeight].append("*")

            else:   
                #creation of the trunk
                for j in range(spaces+(int(width/2)-2)):
                    drawing[line+totalHeight].append(" ")
                for j in range(5):
                    drawing[line+totalHeight].append("*")
    drawing = addingBaubles(drawing)
    return drawing



def addingBaubles(drawing):
    for line in range(len(drawing)-5):
        for rows in range(len(drawing[line])-1):
            if drawing[line][rows] == '*' and drawing[line+1][rows] == " ":
                if drawing[line][rows-1] == " " or drawing[line][rows+1] == " ":
                    drawing[line+1][rows] = "0"
    return drawing



def printing(drawing):
    for i in drawing:
        for j in i:
            print(j, end="")
        print('')



numberOfBranch = 5
baseWidth = 1
incrementation = 1
totalHeight = 0
maxWidth = int(((8*numberOfBranch-1)+6)/2)
drawing= []
tree= creation(drawing, maxWidth, baseWidth, incrementation, totalHeight, numberOfBranch)
printing(tree)