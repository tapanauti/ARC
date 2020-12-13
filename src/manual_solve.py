#!/usr/bin/python

# Name(s): Patrick Garrett, Tapan Auti
# ID: 01571095 , 20231499
# Git Link(s):   , "https://github.com/tapanauti/ARC"


import os, sys
import json
import numpy as np
import re,copy
from scipy.ndimage import label

### YOUR CODE HERE: write at least three functions which solve
### specific tasks by transforming the input x and returning the
### result. Name them according to the task ID as in the three
### examples below. Delete the three examples. The tasks you choose
### must be in the data/training directory, not data/evaluation.

# IMP - as python uses referencing and does not actually copy the values,
#so to use the passed x for solve functions here everywhere we have made a deepcopy of x to solve the problem.

"""6f8cd79b : The task grid is a 7 x 6 grid with all blocks black,
 the solution is a grid of same size which has the blocks on border of the grid filled with cyan color.
"""
def solve_6f8cd79b(x):
    y = copy.deepcopy(x)                
    for i in range(len(y[0])):             #iterating through the y-axis
        y[0][i] = 8                        #filling the top border with desired color
        for j in range(len(y)):            #iterating through the y-axis
            y[j][-1] = 8                   #filling the right border and left border respectively
            y[j][0] = 8
        y[j][i] = 8                        #fillin gthe bottom border
    return y

"""8a004b2b: The task grid here is a around 19 x 18 grid, 
 the solution grid is depending upon the values in input grid i.e the subgrid consisting of all four corners in yellow  """
def solve_8a004b2b(x):

    z = copy.deepcopy(x)
    border = []
                                                            # function for iterating over x and y axis and if block of yellow found store it in a list.
    for i in range(len(z)):                                 
        for j in range(len(z[0])):
            if x[i][j] == 4 :
                border.append([i,j])

    y = [[] for i in range(border[0][0],border[2][0] +1)]

    for i in range(border[0][0],border[2][0] + 1):          # printing the grid from input with the yellow corners. 
        for j in range(border[0][1],border[1][1] +1):
            y[i].append(x[i][j])
    return y



"""5bd6f4ac: The 9x9 task grid is composed of  apparently random coloured squares
 The solution is a 3x3 grid of squares in the top right corner of the task matrix, 
 i.e. the final three elements of each of the first three rows of the grid."""
def solve_5bd6f4ac(x):
    z = copy.deepcopy(x)
    y = [] # holding list
    for i in z[:3]:             #iterating through slice of first 3 rows
        for j in i[-3:]:        #iterating through slice last three columns
            y.append(j)         #adding values to list
    z = np.array(y)             #re-assigning z as a numpy array composed y 
    z = z.reshape(3,3)          #re-shaping z into a 3x3 grid

    return z


"""f76d97a5: The task grids include a pattern of grey squares with the remaining squares a secondary colour. 
It is solved by changing the colour of the grey squares to the secondary colour and changing the 
squares of the secondary colour to black. """
def solve_f76d97a5(x):
    z = copy.deepcopy(x)
    
    for e in z[0]:                  #iterating through the first row of the grid to identify the secondary colour value
        if(e != 5):                 # i.e. the colour that isn't grey (5). 
            other = e

    for i in range(len(z)):
        for j in range(len(z)):      #Iterating through all squares in the grid
            if(z[i][j] != 5):        # If the square is secondary colourv value, change its colour value to black (0)
                other = z[i][j]
                z[i][j] = 0
            else:
                z[i][j] = other      # else, if the square is grey, change its colour value to that of the secondary colour
    return z

"""08ed6ac7: The task grids are composed of four “towers” of grey squares of varying heights, with the remaining 
squares in black. The task is solved by recolouring the tallest tower blue, the second-tallest red, 
third-tallest green, and the shortest yellow."""
def solve_08ed6ac7(x):
    z = copy.deepcopy(x)
    colours = [1,2,3,4]                     #The list of colours, blue, red, green, yellow
    counter = 0                             #counter value for identifying element in colour list

    for i in range(len(z)):                     #Iterating downward through the grid, left to right
        for j in range(len(z)):                  
            if(z[i][j] == 5):                   # If a square is grey, iterate down that column and assign 
                for x in range(i,len(z)):       # it a value of the next colour in the list
                    z[x][j] = colours[counter]
                counter += 1                    #increment the counter for the values in the colour list
    return z


"""7b7f7511: The task grid is composed of a pattern of coloured squares that repeats once, either horizontally 
(if row length in the grid is longer than column length) or vertically (if columns are longer than rows). 
It is solved by extracting the repeating pattern."""
def solve_7b7f7511(x):
    z = copy.deepcopy(x)
    x_axis = len(z[0])                      #Identify length of grid rows and grid columns
    y_axis = len(z)
    half_way = 0
    sol_list = []


    if (x_axis > y_axis):                    #If rows are longer than columns
        sol_list.clear()
        half_way = int(x_axis/2)             #getting value for half the row length
        for i in range(half_way):
            for j in range(y_axis):           
                sol_list.append(z[i][j])#for each row and column in that half of the grid, add their values to the solution list
        z = np.array(sol_list)          #reassign z as a numpy array of solution list
        z = z.reshape(half_way, y_axis) #re-shape z according the dimension based on half of row length
    else:
        half_way = int(y_axis/2)          # If column length is longer, repeat the above procedure, but
        sol_list.clear()                  # on the y axis instead of x axis
        for i in range(half_way):
            for j in range(x_axis):
                sol_list.append(z[i][j])
        z = np.array(sol_list)
        z = z.reshape(half_way, x_axis)

    return z

"""feca6190: The task grid is one row of 5 squares. Some squares are coloured and the rest are black. 
The solution is a grid with dimensions of the n x n (n being the number of coloured squares in the task).
Within the solution grid, the task row of 5 values is repeated on every row,starting from the bottom
row of grid, with the starting element of this pattern incremented with each row up in the grid."""
def solve_feca6190(x):
    x = copy.deepcopy(x)  
    y = x.tolist()
    number_of_colours = 0
    for c in y[0]:
        if(c != 0):
            number_of_colours += 1 #Get number of colours
                    


    #create a grid consisting of numpy array of zeros, with the dimensions equalling (5 x number_of_colours)    
    grid_dimens = 5 * number_of_colours
    grid = np.zeros((grid_dimens,grid_dimens),dtype = int)
   
   
    #starting from bottom left of grid, place x array as first 5 colour values, incrementing by 1 as it rises
    #up the rows of the grid
    #add balck color to x array to make its size same as grid
    for i in range(grid_dimens - len(y[0]) ):
        y[0].append(0)



    a = 0               #lower range for incrementing the loop on x axis
    b = len(y[0])       # upper range for loop x axis
    z= 0                # to take the value from x and insert into grid
    for i in range(len(grid)-1,-1,-1):      # traversing the grid in reverse order 9 - 0
        for j in range(a,b):                # traversing on the x axis
            grid[i][j] = y[0][z]            # inserting from x diagonally into grid
            z +=1               # with every increment in x axis increment the x index to insert color diagonally
        a +=1                   # with every increment start from 1 position next at x axis
        z = 0                   # at every y axis iteration initialse x pointer to 0

    return grid


"""d0f5fe59: The task grid is a grid with random shapes in cyan color and the output will be a grid of size where size equals number of non-connected shapes in input grid """
def solve_d0f5fe59(x):

    a, y = label(x)                         # scipy 'nd image' has a function 'label' which returns the connected blocks as label in the grid and the labelled grid itself.

    grid = np.zeros((y,y),dtype = int )     # the number of labels will be the no of non-connected shapes in the grid.
    np.fill_diagonal(grid,8)                # this will fill the diagonal in a ndarray with the desired values in our case color cyan.

    return grid

"""ded97339: The task grid is composed of a small number of dispersed cyan-coloured squares with the remaining squares black. The task is solved by assessing if any two cyan squares are on the same row or column and, if so, colouring in the intermediate squares cyan.  """
def solve_ded97339(x):
    x = copy.deepcopy(x)

    #iterating over rows in x. If there are two instances of 8 (cyan) draw a "line" between them in a different
    # "colour". 
    x_list = []
    for row in x:
        for index,item in enumerate(row):       #finding both items and their indices within each row
            if (item == 8):
                x_list.append(index)            #list of indices of occurences of 8 (cyan) in each row
        
        if(len(x_list) == 2): # If there are two "8"s in a particular row, get their indices and draw a line between them
            a = x_list[0]       #index of first 8
            b = x_list[1]       #index of second 8
            for i in range(a+1,b):
                    row[i] = 2 # 2 just represents an arbitrary colour. It can be any value apart from 0 and 8
        x_list.clear()

    #Same procedure as the iterating over X axis, except this time iterate down through columns
    y_list = []
    for column in x.T:          #x.T is tranposed version of x - columns become rows and vice versa
        for index,item in enumerate(column):
            if (item == 8):
                y_list.append(index)

        if(len(y_list) == 2):
            a = y_list[0]
            b = y_list[1]
            for i in range(a+1,b):
                    column[i] = 2
        y_list.clear()
        
    #changing all elements with the arbitrary placeholder value into 8s again
    for i in range(len(x)):
        for j in range(len(x[0])):
            if(x[i][j]==2):
                x[i][j] = 8

    return x

  


def main():
    # Find all the functions defined in this file whose names are
    # like solve_abcd1234(), and run them.

    # regex to match solve_* functions and extract task IDs
    p = r"solve_([a-f0-9]{8})" 
    tasks_solvers = []
    # globals() gives a dict containing all global names (variables
    # and functions), as name: value pairs.
    for name in globals(): 
        m = re.match(p, name)
        if m:
            # if the name fits the pattern eg solve_abcd1234
            ID = m.group(1) # just the task ID
            solve_fn = globals()[name] # the fn itself
            tasks_solvers.append((ID, solve_fn))

    for ID, solve_fn in tasks_solvers:
        # for each task, read the data and call test()
        directory = os.path.join( "data", "training")
        json_filename = os.path.join(directory, ID + ".json")
        data = read_ARC_JSON(json_filename)
        test(ID, solve_fn, data)
    
def read_ARC_JSON(filepath):
    """Given a filepath, read in the ARC task data which is in JSON
    format. Extract the train/test input/output pairs of
    grids. Convert each grid to np.array and return train_input,
    train_output, test_input, test_output."""
    
    # Open the JSON file and load it 
    data = json.load(open(filepath))

    # Extract the train/test input/output grids. Each grid will be a
    # list of lists of ints. We convert to Numpy.
    train_input = [np.array(data['train'][i]['input']) for i in range(len(data['train']))]
    train_output = [np.array(data['train'][i]['output']) for i in range(len(data['train']))]
    test_input = [np.array(data['test'][i]['input']) for i in range(len(data['test']))]
    test_output = [np.array(data['test'][i]['output']) for i in range(len(data['test']))]

    return (train_input, train_output, test_input, test_output)


def test(taskID, solve, data):
    """Given a task ID, call the given solve() function on every
    example in the task data."""
    print(taskID)
    train_input, train_output, test_input, test_output = data
    print("Training grids")
    for x, y in zip(train_input, train_output):
        #print(x)
        yhat = solve(x)
        show_result(x, y, yhat)
    print("Test grids")
    for x, y in zip(test_input, test_output):
        yhat = solve(x)
        show_result(x, y, yhat)

        
def show_result(xi, y, yhat):
    print("Input")
    print(xi)
    print("Correct output")
    print(y)
    print("Our output")
    print(yhat)
    print("Correct?")
    # if yhat has the right shape, then (y == yhat) is a bool array
    # and we test whether it is True everywhere. if yhat has the wrong
    # shape, then y == yhat is just a single bool.
    print(np.all(y == yhat))

if __name__ == "__main__": main()