#!/usr/bin/python

import os, sys
import json
import numpy as np
import re,copy

### YOUR CODE HERE: write at least three functions which solve
### specific tasks by transforming the input x and returning the
### result. Name them according to the task ID as in the three
### examples below. Delete the three examples. The tasks you choose
### must be in the data/training directory, not data/evaluation.


def solve_6f8cd79b(x):
    y = copy.deepcopy(x)
    for i in range(len(y[0])):
        y[0][i] = 8
        for j in range(len(y)):
            y[j][-1] = 8
            y[j][0] = 8
        y[j][i] = 8
    return y

def solve_8a004b2b(x):

    z = copy.deepcopy(x)
    border = []

    for i in range(len(z)):
        for j in range(len(z[0])):
            if x[i][j] == 4 :
                border.append([i,j])

    y = [[] for i in range(border[0][0],border[2][0] +1)]

    for i in range(border[0][0],border[2][0] + 1):
        for j in range(border[0][1],border[1][1] +1):
            y[i].append(x[i][j])
    return y



#example?  pushed by Patrick 
def solve_5bd6f4ac(x):
    z = copy.deepcopy(x)
    y = []
    for i in z[:3]:
        for j in i[-3:]:
            y.append(j)
    z = np.array(y)
    z = z.reshape(3,3)

    return z

#not the best solution - I might change
def solve_f76d97a5(x):
    z = copy.deepcopy(x)
    
    for e in z[0]:
        if(e != 5):
            other = e

    for i in range(len(z)):
        for j in range(len(z)):
            if(z[i][j] != 5):
                other = z[i][j]
                z[i][j] = 0
            else:
                z[i][j] = other  
    return z

def solve_08ed6ac7(x):
    z = copy.deepcopy(x)
    colours = [1,2,3,4]
    counter = 0

    for i in range(len(z)):
        for j in range(len(z)):
            if(z[i][j] == 5):
                for x in range(i,len(z)):
                    z[x][j] = colours[counter]
                counter += 1    
    return z


#Solution perhaps not totally robust. I might change it
def solve_7b7f7511(x):
    z = copy.deepcopy(x)
    x_axis = len(z[0])
    y_axis = len(z)
    half_way = 0
    sol_list = []


    if (x_axis > y_axis):
        sol_list.clear()
        half_way = int(x_axis/2)
        for i in range(half_way):
            for j in range(y_axis):
                sol_list.append(z[i][j])
        z = np.array(sol_list)
        z = z.reshape(half_way, y_axis)
    else:
        half_way = int(y_axis/2)
        sol_list.clear()
        for i in range(half_way):
            for j in range(x_axis):
                sol_list.append(z[i][j])
        z = np.array(sol_list)
        z = z.reshape(half_way, x_axis)

    return z

# saw the code incomplete so implemented it in my way, its working if we have to use this. - tapan
def solve_feca6190(x):
    x = copy.deepcopy(x)
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

    return grid

"""Incomplete - Still working on this
def solve_feca6190(x):
    x = copy.deepcopy(x)

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



    for e in range(grid_dimens-1,0,-1):
        #grid[e][0] = 5
        for i in range(len(x[0])):
            grid[e][i] = x[0][i]

        #end -=1     
        
        
        #for k in range(i,grid_dimens): 
         #   for j in range(grid_dimens,0):
          #      grid[j][k] = x[0][i]

              #  grid[10][k] = x[0][i]
               # test -= 1

    #for i in range(len(grid[0])):
     #   grid[i] = 5
    #print((x[0]))
    #x = grid
    
    return grid
"""
    



""" Incomplete Implementation
def solve_05269061(x):
    x = copy.deepcopy(x)
    a = (0,3,6)
    b = (1,4)
    c = (2,5)

    for i in range(3):
        for i in range(len(x)):
            for j in range(len(x)):
                if(x[i][j] != 0 and j in a):
                    for ac in a :
                        x[i][ac] = x[i][j]
                elif(x[i][j] != 0 and j in b):
                    for bc in b :
                        x[i][bc] = x[i][j]
                elif(x[i][j] != 0 and j in c):
                    for cc in c :
                        x[i][cc] = x[i][j]

        for i in range(len(x)):
            for j in range(len(x)):
                if(x[j][i] != 0 and j in a):
                    for ac in a :
                        x[ac][i] = x[j][i]
                elif(x[j][i] != 0 and j in b):
                    for bc in b :
                        x[bc][i] = x[j][i]
                elif(x[j][i] != 0 and j in c):
                    for cc in c :
                        x[cc][i] = x[j][i]

    
    return x
    
    """


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