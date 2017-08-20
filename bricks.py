from __future__ import print_function
from random import randint

class Brick:
    def __init__(self):
        self._test = 0

    def createBrick(self, gBoard):
        counter = 0
        while(counter < 35):
            x = randint(2,38)
            y = randint(3,80)
            if(gBoard[x][y]==' ' and ((x%4==0 and y%8==0) or (x%4==2 and y%8==4) or (x%4==2 and y%8==0) or (x%4==0 and y%8==4))):
                for p in range(4):
                    gBoard[x][y+p] = "/"
                    gBoard[x+1][y+p] = "/"
                counter += 1

    def remove(self, x, y, gBoard):
        for i in range(x,x+2):
            for j in range(y,y+4):
                gBoard[i][j] = ' '
