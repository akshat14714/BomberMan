from person import *
from bomberman import *
from random import randint

class Enemy(Person):
    def __init__(self):
        self._test = 0

    def makeEnemy(self, x, y, enemy, bomber, gBoard):
            f = 0
            for i in range(x,x+2):
                for j in range(y,y+4):
                    if(bomber[i][j]!='B' and gBoard[i][j]!='X' and enemy[i][j]!='E' and gBoard[i][j]!='/'):
                        f = 0
                    else:
                        f = 1
                        break
            if(f == 0):
                for i in range(x,x+2):
                    for j in range(y,y+4):
                        enemy[i][j] = 'E'

            else:
                x = randint(1,20)*2
                y = randint(1,20)*4
                self.makeEnemy(x, y, enemy, bomber, gBoard)

    def moveRight(self, x, y, enemy):
        for i in range(y+4,y+8):
            enemy[x][i] = 'E'
            enemy[x][i-4] = ' '
            enemy[x+1][i] = 'E'
            enemy[x+1][i-4] = ' '
        y += 4
        return y

    def moveLeft(self, x, y, enemy):
        for i in range(y-4,y):
            enemy[x][i] = 'E'
            enemy[x][i+4] = ' '
            enemy[x+1][i] = 'E'
            enemy[x+1][i+4] = ' '
        y -= 4
        return y

    def moveUp(self, x, y, enemy):
        for i in range(4):
            enemy[x-2][y+i] = 'E'
            enemy[x-1][y+i] = 'E'
            enemy[x][y+i] = ' '
            enemy[x+1][y+i] = ' '
        x -= 2
        return x

    def moveDown(self, x, y, enemy):
        for i in range(4):
            enemy[x][y+i] = ' '
            enemy[x+1][y+i] = ' '
            enemy[x+2][y+i] = 'E'
            enemy[x+3][y+i] = 'E'
        x += 2
        return x
