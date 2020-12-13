import numpy as np
x = [[1, 0, 7, 0, 0]]
#Get number of colours
colours = []
for c in x[0]:
    if(c != 0):
        colours.append(c)         
number_of_colours = len(colours)

#create a grid consisting of numpy array of zeros, with the dimensions equalling (5 x number_of_colours)    
grid_dimens = 5 * number_of_colours
grid = np.zeros((grid_dimens,grid_dimens),dtype = int)
#starting from bottom left of grid, place x array as first 5 colour values, incrementing by 1 as it rises
#up the rows of the grid

#below this tried to implement the code - tapan
# add balck color to x array to make its size same as grid
for i in range(grid_dimens - len(x[0]) ):
    x[0].append(0)

#  using a lot comments so you can understand what i haveimpemented - tapan

a = 0 # lower range for incrementing the loop on x axis
b = len(x[0]) # upper range for loop x axis
z= 0 # to take the value from x and insert into grid
for i in range(len(grid)-1,-1,-1): # traversing the grid in reverse order 9 - 0
    for j in range(a,b): # traversing on the x axis
        grid[i][j] = x[0][z] # inserting from x diagonally into grid
        z +=1 # with every incremnet in x axis increment the x index to insert color diagonally
    a +=1 # with every increment start from 1 position next at x axis
    z = 0 # at every y axis iteration initialse x pointer to 0

print(grid)