import numpy as np

"""
You will be given a 2D array of the maze and an array of directions.

Your task is to follow the directions given. If you reach the end point before all your moves have gone, you should return Finish.

If you hit any walls or go outside the maze border, you should return Dead. 

If you find yourself still in the maze after using all the moves, you should return Lost.
"""

def maze_runner(maze, directions):
    direction = directions
    
    # identify the starting point of the maze
    # turn the maze into a numpy array
    maze = np.array(maze)
    sCol = np.where(maze == 2)[0][0]
    sRow = np.where(maze == 2)[1][0]

    # establish dictionary of properties of the directions
    """
    N = North: subtract 1 from the column index
    E = East: add 1 to the row index
    W = West: subtract 1 from the row index
    S = South: add 1 to the column index

    Next: iterate through direction list to determine how far we should move.
    """
    status = ""

    moveDict = {
    "N":{
        'value':-1
    },
    "E":{
        'value':1
    },
    "W":{
        'value':-1
    },
    "S":{
        'value':1
        }
    }

    """
    This needs to be updated to a while loop
    On each iteration need to check the location of where I am at within the maze.
    If I am on a tile or section with a 3 then terminate and return Finish
    """

    for i in direction:
        if i == "N":
            sCol = sCol + moveDict[i]['value']
            print(sCol, maze[sCol])
            # print()
            # print(maze[sCol-sCol+moveDict[i]['value']])
            # print(maze[sCol][sRow])
        elif i == "E":
            sRow = sRow + moveDict[i]['value']
            print(sRow, maze[sCol][sRow])
            if maze[sCol][sRow] == 3:
                # print("TEST")
                status = "Finish"
                break
        elif i == "W":
            sRow = sRow + moveDict[i]['value']
        elif i == "S":
            sCol = sCol + moveDict[i]['value']

    # print(maze[sCol][sRow])
    
    # print(maze[sCol])

    """
    Attempt to use a Try & Except clause
    If the index is out of range then we assume the user dead
    """
    try:
        if maze[sCol][sRow] == 1:
            status = "Dead"
        elif maze[sCol][sRow] == 0:
            status = "Lost"
        else:
            status = "Finish"
    except IndexError:
        status = "Dead"

    print(status)
    return status

m = [[1,1,1,1,1,1,1],
        [1,0,0,0,0,0,3],
        [1,0,1,0,1,0,1],
        [0,0,1,0,0,0,1],
        [1,0,1,0,1,0,1],
        [1,0,0,0,0,0,1],
        [1,2,1,0,1,0,1]]

d = ["N","N","N","N","N","E","E","E","E","E","W","W"]
runner_update = maze_runner(m, d)

print(runner_update)