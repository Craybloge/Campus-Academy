
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
        spaces -= incrementation
        for j in range(width):
            drawing[line + totalHeight].append("*")
        width += incrementation*2
    numberOfBranch -= 1
    if numberOfBranch >0:
        creation(drawing, maxWidth, baseWidth+2,incrementation+1, totalHeight+height, numberOfBranch)
    else:
        print(incrementation, baseWidth, spaces,width)
        #creation of the trunk
        for i in range(3):
            for i in range(13):
                pass

    return drawing

def printing(drawing):
    for i in drawing:
        for j in i:
            print(j, end="")
        print('')



numberOfBranch = 37
baseWidth = 1
incrementation = 1
totalHeight = 0
maxWidth = 230
drawing= []
tree= creation(drawing, maxWidth, baseWidth, incrementation, totalHeight, numberOfBranch)
printing(tree)