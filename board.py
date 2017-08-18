from __future__ import print_function
from bricks import *
from walls import *

boardSizex = 84
boardSizey = 42

wall = Walls()

class Board:
    def __init__(self):
        self._test = 0

    def makeWall(self, gBoard):
        for i in range(0, boardSizey, 2):
            for j in range(0, boardSizex, 4):
                if(i==0 or j==0 or i==boardSizey-2 or j==boardSizex-4 or ((i%4==0 and j%8==0) and (j<boardSizex-4 and i<boardSizey-2))):
                    wall.createWall(i,j,gBoard)

    def printBoard(self, gBoard, bomber, x, y, enemy, ex, ey):
        for i in range(boardSizey):
            for j in range(boardSizex):
                if(bomber[i][j]=='B'):
                    print(bomber[i][j], end='')
                elif(enemy[i][j]=='E'):
                    print(enemy[i][j], end='')
                else:
                    print (gBoard[i][j], end='')
            print()