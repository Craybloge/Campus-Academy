"""
Creation of a/several Christmas Trees

The two constants:
- number_of_branch:
    The number of branch (the number of pyramid stacked we could say)
- number_of_tree :
    The number of Christmas Tree to print

"""
import sys

NUMBER_OF_TREES = 4
NUMBER_OF_BRANCH = 4


def creation(number_of_branch):
    """
    Here we're going to create variables needed to draw the tree,
    and call the functions in order to have the complete tree.

    Incrementation: this is the progressive widening of the branches,
    by default it will be 1 more than the previous branch.

    max_width: This is the maximum width the tree will reach,
    used to calculate how many spaces we will need to fit it
    in the 2-dimensionnal list.
    """
    incrementation = 1
    max_width = int((8 * NUMBER_OF_BRANCH + 3) / 2)

    drawing, current_height = adding_star(max_width)
    drawing, current_height, spaces = leaves(drawing,
                                             max_width,
                                             current_height,
                                             incrementation,
                                             number_of_branch)
    drawing = trunk_and_wreath(drawing,
                               max_width,
                               current_height,
                               (spaces +
                                incrementation +
                                (number_of_branch - 1)))
    drawing = adding_baubles(drawing)
    return drawing


def adding_star(max_width):
    '''
    Here we draw the star, that's the first thing we want to draw
    as it's on the top of the tree.
    That's why we create the list "drawing" here.
    We then calculate the amount of spaces to add before the star
    and then starts to draw.
    The algorythm is still not optimized and very long,
    it's WIP.
    '''
    drawing = []
    spaces = max_width-5
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
                if rows % 2 == 0:
                    drawing[line].append("*")
                else:
                    drawing[line].append(" ")
        if line in (4, 2):
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
    return drawing, 7


def leaves(drawing, max_width, current_height,
           incrementation, number_of_branch):
    '''
    Here we're going to manage the creation of the leaves
    (the main part of the tree).

    "width": Corresponds to the base width of the first leave of a branch,
    by default it starts at 1 and increase by 2 each branch.

    "height": Corresponds to the number of leaves for each branch
    (we can change that if we want but it's not asked in the exercise).
    '''
    width = 1
    height = 4

    for branches in range(number_of_branch):
        base_width = width
        spaces = 2 * int(max_width / 2)+2 - width
        for line in range(height):
            if line == 0:
                spaces += ((incrementation+branches)-1)
            drawing.append([])
            for rows in range(spaces):
                drawing[line + current_height].append(" ")
            for rows in range(width):
                drawing[line + current_height].append("*")
            for rows in range(spaces):
                drawing[line + current_height].append(" ")
            spaces -= incrementation+branches
            width += (incrementation+branches) * 2
        current_height += height
        width = base_width+2
    return drawing, current_height, spaces


def trunk_and_wreath(drawing, max_width, current_height, spaces):
    '''
    Here we manage both the creation of the trunk and the wreath
    as we draw line per line and they are on the same lines for
    the most part.

    We first draw the to lines with wreath and trunk,
    and then we draw the last line of the trunk.
    '''
    for line in range(3):
        drawing.append([])
        if line != 2:
            ''' Creation of the wreath and
                the two first line of the trunk
            '''
            if line == 0:
                wreath = "|"
            elif line == 1:
                wreath = "0"
            for rows in range(spaces):
                drawing[line + current_height].append(" ")
            for rows in range(max_width*2-3):
                if (rows % 2 == 1 and
                    not(
                        len(drawing[line + current_height]) >=
                        spaces+(max_width-5) and
                        len(drawing[line + current_height]) <
                        spaces+(max_width+2))):
                    # if both condition are True we are on the trunk
                    drawing[line + current_height].append(wreath)
                if (rows % 2 == 0 and
                    not(
                        len(drawing[line + current_height]) >=
                        spaces+(max_width-4) and
                        len(drawing[line + current_height]) <
                        spaces+(max_width+1))):
                    # if both condition are True we are on the trunk
                    drawing[line + current_height].append(" ")
                if (len(drawing[line+current_height]) >=
                        spaces+(max_width-4) and
                        len(drawing[line+current_height]) <
                        spaces+(max_width+1)):
                    # if both condition are True we are on the trunk
                    drawing[line+current_height].append("*")
            for rows in range(spaces):
                drawing[line + current_height].append(" ")
        else:
            '''Creation of the last line of the trunk'''
            for row in range(spaces+(max_width-4)):
                drawing[line + current_height].append(" ")
            for row in range(5):
                drawing[line + current_height].append("*")
            for row in range(spaces+(max_width-4)):
                drawing[line + current_height].append(" ")
    return drawing


def adding_baubles(drawing):
    '''
    Here we add the baubles on the tree.
    it's a special function because it's the only one
    that modify existing elements instead of adding new.
    We simply detect each end of a branch and add a bauble.
    '''
    for line in range(7, len(drawing) - 5):
        for rows in range(len(drawing[line]) - 1):
            if drawing[line][rows] == '*':
                if drawing[line + 1][rows] == " ":
                    if (drawing[line][rows - 1] == " " or
                            drawing[line][rows + 1] == " "):
                        drawing[line + 1][rows] = "0"
    return drawing


def printing(drawing, number_of_trees):
    '''
    Here is the function that print the 2-dimensionnal list
    on the console, the number of times needed.
    '''
    for i in drawing:
        for _ in range(number_of_trees):
            for j in i:
                print(j, end="")
        print('')


'''
If the program is launched with arguments
in the console to change the amount of branch or trees,
they'll be managed here.
'''
args = sys.argv
if len(args) >= 2:
    NUMBER_OF_BRANCH = int(args[1])
if len(args) >= 3:
    NUMBER_OF_TREES = int(args[2])

# it's where we launch the drawing of the tree
tree = creation(NUMBER_OF_BRANCH)
printing(tree, NUMBER_OF_TREES)
