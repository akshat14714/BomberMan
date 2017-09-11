from __future__ import print_function
from termcolor import colored
from bricks import *
from walls import *

boardSizex = 84
boardSizey = 42

wall = Walls()
brick = Brick()


class Board:

    def __init__(self):
        self._test = 0

    def makeWall(self, gBoard):
        for i in range(0, boardSizey, 2):
            for j in range(0, boardSizex, 4):
                if(i == 0 or j == 0 or i == boardSizey - 2 or
                   j == boardSizex - 4 or
                   (i % 4 == 0 and j % 8 == 0 and
                        j < boardSizex - 4 and i < boardSizey - 2)):
                    wall.createWall(i, j, gBoard)

    def printBoard(self, gBoard, bomber, x, y, enemy, count, bombx, bomby):
        for i in range(boardSizey):
            for j in range(boardSizex):
                if(i == bombx and j == bomby and gBoard[i][j] != 'X' and
                   gBoard[i][j] != '/'):
                    for k in range(i, i + 2):
                        for l in range(j, j + 4):
                            if(count != 0):
                                gBoard[k][l] = count
                    bombx = 0
                    bomby = 0
                if(bomber[i][j] == 'B'):
                    print(colored(bomber[i][j], 'cyan'), end='')
                elif(enemy[i][j] == 'E'):
                    print(colored(enemy[i][j], 'red'), end='')
                elif(gBoard[i][j] == '/'):
                    print(colored(gBoard[i][j], 'yellow'), end='')
                elif(gBoard[i][j] == 'v' or gBoard[i][j] == '^' or
                     gBoard[i][j] == '>' or gBoard[i][j] == '<' or
                     gBoard[i][j] == count):
                    print(colored(gBoard[i][j], 'magenta'), end='')
                else:
                    print(gBoard[i][j], end='')
            print()
