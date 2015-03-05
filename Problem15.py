## Project Euler Problems

#Problem 15: Lattice Grid


##Overcomplicated the problem, actual solution below

from functools import lru_cache

@lru_cache(None)
def findmoves(x, y):
    if x == 0 or y == 0:
        return 1
    return findmoves(x - 1, y) + findmoves(x, y - 1)


i = 20
print(findmoves(i, i))


#My initial attempt

RIGHT = (0, 1)
DOWN = (1, 0)

class LatticeGrid(object):
    def __init__(self, size):
        self.grid = [[0] * (size + 1) for _ in range(size + 1)]
        self.row = 0
        self.col = 0
        self.startpt = (0, 0)
        self.endpt = (size, size)
        self.movedict = {}
        self.movelist = [RIGHT, DOWN]
        
    def __str__(self):
        s = ''
        for row in self.grid:
            if s:
                s += '\n'
            s += str(row)
        return s + "\nCurrent position: " + str(self.position())
    
    def move(self, direction):
        self.row += direction[0]
        self.col += direction[1]
        return self.row, self.col

    def position(self):
        return (self.row, self.col)
    
    def findmoves(self, destination):
        movecount = 0
        start = self.position()
        while start != destination:
            if start[0] < destination[0]:
                self.move(DOWN)
            if start[1] < destination [1]:
                self.move(RIGHT)

board = LatticeGrid(2)




