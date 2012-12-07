#!/usr/bin/env python2.6

ROWS = 6
COLS = 6

grid = [[1 for _ in range(ROWS)] for _ in range(COLS)]

def printGrid(grid):
    for col in grid:
        for row in col:
            print row,
        print

    print "Sum:",sum([sum(col) for col in grid])

def isEven(n):
    return 0 == (n%2)

print "All ones"
printGrid(grid)

for col in range(len(grid)):
    for row in range(len(grid[col])):
        if isEven(col) and isEven(row):
            grid[col][row] = 2
        elif not isEven(col) and not isEven(row):
            grid[col][row] = 2

print "Checkerboard"
printGrid(grid)
