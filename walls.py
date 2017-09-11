from __future__ import print_function
from bricks import *

brick = Brick()

boardSizey = 42
boardSizex = 84


class Walls:

    def __init__(self):
        self._struct = [[' ' for i in range(4)] for j in range(2)]

    def createWall(self, x, y, gBoard):
        for p in range(4):
            gBoard[x][y + p] = "X"
            gBoard[x + 1][y + p] = "X"
