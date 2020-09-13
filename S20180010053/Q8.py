# !/bin/python3

import math
import os
import random
import re
import sys


count = [0]
gold=0
silver=0
i=0
j=0

def solvemaze(r,c,x,y,solution,maze):
    global count
    global gold
    global silver
    global i
    global j
    maze_rows=len(maze)
    maze_columns=len(maze[0])
    if ((r==x) and (c==y)):
        if silver!=gold:
            count[i]=count[i]-(j-1)
            j=0
            return False
        solution[r][c] = 1
        i=i+1
        count.insert(i,0)
        return True

    if r>=0 and c>=0 and r<maze_rows and c<maze_columns and solution[r][c] == 0 and (maze[r][c] == 0 or maze[r][c]==2):
        #if safe to visit then visit the cell
        solution[r][c] = 1
        count[i]=count[i]+1
        j=j+1
        if maze[r][c]==2:
            silver=silver+1

        if solvemaze(r+1, c,x,y,solution,maze)==True:
            return True
        #going right
        if solvemaze(r, c+1,x,y,solution,maze)==True:
            return True
        #going up

        if solvemaze(r-1, c,x,y,solution,maze)==True:
            return True
        #going left

        if solvemaze(r, c-1,x,y,solution,maze)==True:
            return True
        #backtracking
        solution[r][c] = 0
        return False

def minMoves(maze, x, y):
    global count
    global gold
    # Write your code here
    maze_rows=len(maze)
    maze_columns=len(maze[0])
    solution = [[0]*maze_columns for _ in range(maze_rows)]

    for i in range(maze_rows):
        for j in range(maze_columns):
            if maze[i][j]==2:
                gold=gold+1

#     print(solution)
#     count = 0
    if(solvemaze(0,0,x,y,solution,maze)):
        count.pop()
        return min(count)
    else:
        return -1
    print(solution)

if __name__ == '__main__':

    maze_rows = int(input().strip())
    maze_columns = int(input().strip())

    maze = []

    for _ in range(maze_rows):
        maze.append(list(map(int, input().rstrip().split())))

    x = int(input().strip())

    y = int(input().strip())

    result = minMoves(maze, x, y)
    print(result)
