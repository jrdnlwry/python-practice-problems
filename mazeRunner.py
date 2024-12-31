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

    for i in direction:
        if i == "N":
            sCol = sCol + moveDict[i]['value']
            print(sCol, maze[sCol])
            print()
            # print(maze[sCol-sCol+moveDict[i]['value']])
            # print(maze[sCol][sRow])
        elif i == "E":
            sRow = sRow + moveDict[i]['value']
        elif i == "W":
            sRow = sRow + moveDict[i]['value']
        elif i == "S":
            sCol = sCol + moveDict[i]['value']

    pass