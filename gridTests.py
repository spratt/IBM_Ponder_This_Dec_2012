#!/usr/bin/env python2.6

from grid import Grid

g = Grid(1,1)

print type(g)

print "----------------------------------------------------------------------"
print "| Grid(6,4)                                                          |"
print "----------------------------------------------------------------------"

ROWS = 6
COLS = 4

g = Grid(ROWS,COLS)

y,x = 0,0
print "({0},{1}) is valid? {2}".format(y,x,g.isValidPos(y,x))
y,x = ROWS-1,0
print "({0},{1}) is valid? {2}".format(y,x,g.isValidPos(y,x))
y,x = 0,COLS-1
print "({0},{1}) is valid? {2}".format(y,x,g.isValidPos(y,x))
y,x = ROWS-1,COLS-1
print "({0},{1}) is valid? {2}".format(y,x,g.isValidPos(y,x))
y,x = -1,0
print "({0},{1}) is valid? {2}".format(y,x,g.isValidPos(y,x))
y,x = 0,-1
print "({0},{1}) is valid? {2}".format(y,x,g.isValidPos(y,x))
y,x = -1,-1
print "({0},{1}) is valid? {2}".format(y,x,g.isValidPos(y,x))
y,x = ROWS,0
print "({0},{1}) is valid? {2}".format(y,x,g.isValidPos(y,x))
y,x = 0,COLS
print "({0},{1}) is valid? {2}".format(y,x,g.isValidPos(y,x))
y,x = ROWS,COLS
print "({0},{1}) is valid? {2}".format(y,x,g.isValidPos(y,x))

print "----------------------------------------------------------------------"
print "| Grid(6,6)                                                          |"
print "----------------------------------------------------------------------"

ROWS = 6
COLS = 6

g = Grid(ROWS,COLS)

y,x = 0,0
print "({0},{1}) is valid? {2}".format(y,x,g.isValidPos(y,x))
y,x = ROWS-1,0
print "({0},{1}) is valid? {2}".format(y,x,g.isValidPos(y,x))
y,x = 0,COLS-1
print "({0},{1}) is valid? {2}".format(y,x,g.isValidPos(y,x))
y,x = ROWS-1,COLS-1
print "({0},{1}) is valid? {2}".format(y,x,g.isValidPos(y,x))
y,x = -1,0
print "({0},{1}) is valid? {2}".format(y,x,g.isValidPos(y,x))
y,x = 0,-1
print "({0},{1}) is valid? {2}".format(y,x,g.isValidPos(y,x))
y,x = -1,-1
print "({0},{1}) is valid? {2}".format(y,x,g.isValidPos(y,x))
y,x = ROWS,0
print "({0},{1}) is valid? {2}".format(y,x,g.isValidPos(y,x))
y,x = 0,COLS
print "({0},{1}) is valid? {2}".format(y,x,g.isValidPos(y,x))
y,x = ROWS,COLS
print "({0},{1}) is valid? {2}".format(y,x,g.isValidPos(y,x))
