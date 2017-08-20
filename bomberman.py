from person import *

class BomberMan(Person):
    def __init__(self):
        self.life = 3
        self.score = 0
        self._test = 0

    def makePlayer(self, x, y, bomber):
        for i in range(x,x+2):
            for j in range(y,y+4):
                bomber[i][j] = "B"
