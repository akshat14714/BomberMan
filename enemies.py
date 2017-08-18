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
                if(bomber[i][j]!='B' and gBoard[i][j]!='X' and enemy[i][j]!='E'):
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
            self.makeEnemy(x,y,enemy, bomber, gBoard)
