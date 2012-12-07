#!/usr/bin/env python2.6

class Grid(object):
    def __init__(self,rows,cols):
        self.rows = rows
        self.cols = cols
        self._grid = [[1 for _ in range(cols)] for _ in range(rows)]

    def __str__(self):
        s = ""
        for row in self._grid:
            for col in row:
                s += "{0} ".format(col)
            s += "\n"
        return s

    def sum(self):
        return sum([sum(col) for col in self._grid])

    def isValidPos(self,row,col):
        return (0 <= row < self.rows) and (0 <= col < self.cols)

    def getNeighbours(self,row,col):
        nborVals = set()
        nborVals.add(self.getVal(row-1,col)) # up
        nborVals.add(self.getVal(row+1,col)) # down
        nborVals.add(self.getVal(row,col-1)) # left
        nborVals.add(self.getVal(row,col+1)) # right
        return nborVals

    def isPosValid(self,row,col):
        if not self.isValidPos(row,col):
            return False
        return self.getVal(row,col) == self.maxVal(row,col)

    def getVal(self,row,col):
        if self.isValidPos(row,col):
            return self._grid[row][col]
        return 0

    def setVal(self,row,col,val):
        if self.isValidPos(row,col):
            self._grid[row][col] = val
        self.makeValid()

    def maxVal(self,row,col):
        nborVals = self.getNeighbours(row,col)
        for i in range(len(nborVals)+1):
            if (i+1) not in nborVals:
                return (i+1)

    def isValid(self):
        valid = True
        for row in range(self.rows):
            for col in range(self.cols):
                valid = valid and self.isPosValid(row,col)
        return valid

    def makeValid(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if not self.isPosValid(row,col):
                    self.setVal(row,col,self.maxVal(row,col))

def isEven(n):
    return 0 == (n%2)

if __name__ == '__main__':
    g = Grid(6,6)

    print "All ones"
    print g
    print "Sum:",g.sum()

    print "Checkerboard"
    g.makeValid()
    print g
    print "Sum:",g.sum()

    print "makeValid(Checkerboard)"
    g.makeValid()
    print g
    print "Sum:",g.sum()
