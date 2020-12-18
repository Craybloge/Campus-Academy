Considering all the scripts of the exercises are simpler version of the script main.py, so they all work exactly the same way,
so I will only write a README for this one.
## Creation of a/several Christmas Trees
to use the scripts you can either execute them without arguments, they'll use default parameters.
you can also edit them directly, but I recommand you to only change the two constants:
- **number_of_branch:**
    The number of branch (the number of pyramid stacked we could say)
- **number_of_tree:**
    The number of Christmas Tree to print
you can also execute theses scripts with 2 int arguments to change these values.

if you want to edit further (but it may get ugly), you can also edit in the script:
- **incrementation:** In the creation function, it will increase the progressive widening of the branch. By default it start at one and it will be 1 more than the previous branch (you can only change the starting incrementation)
- **width:** In the leaves function, it will increase the base width of the first branch. By default it starts at 1 and increase by 2 for each branch (you can only modify the starting width)
- **height:** In the leaves function, it will increase the amount of leaves for each branch(the amount of stairs for each pyramid if you want). By default it is 4.

### Behaviour of each script
[level 1](https://github.com/Craybloge/CampusAcademyContest2020/blob/main/PythonScripts/exercices/level_1_the_3_branch_tree.py): Draws just the leaves.  
[level 2](https://github.com/Craybloge/CampusAcademyContest2020/blob/main/PythonScripts/exercices/level_2_the_trunk.py): Same as above + draws the trunk.  
[level 3](https://github.com/Craybloge/CampusAcademyContest2020/blob/main/PythonScripts/exercices/level_3_the_wreath.py): Same as above + draws the wreath at the bottom of the tree.  
[level 4](https://github.com/Craybloge/CampusAcademyContest2020/blob/main/PythonScripts/exercices/level_4_the_baubles.py): Same as above + draws bauble at the edge of each branch.  
[level 5](https://github.com/Craybloge/CampusAcademyContest2020/blob/main/PythonScripts/exercices/level_5_the_final_star_of_death.py): Same as above + draws a star at the top of the tree.  
[bonus 1](https://github.com/Craybloge/CampusAcademyContest2020/blob/main/PythonScripts/exercices/bonus_1_a_bigger_tree.py): Is supposed to allow to choose the size of the tree(amount of branches) but it's actually implemented in all scripts.  
[bonus 2](https://github.com/Craybloge/CampusAcademyContest2020/blob/main/PythonScripts/exercices/bonus_2_a_lot_of_trees.py): Is supposed to allow to choose the number of trees we want but it's already implemented in all scripts.  