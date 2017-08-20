class Bomb:
    def __init__(self):
        self._test = 0

    def plant(self, x, y, gBoard):
        for i in range(x,x+2):
            for y in range(y,y+4):


    def explode(self, x, y, gBoard, playerx, playery, bomber, victim):
        flag = 0
        if(x==playerx and y==playery):
            flag = 1
        for i in range(x,x+2):
            for j in range(y-5,y-1):
                if(gBoard[i][j] != 'X'):
                    gBoard[i][j] = '^'
            for j in range(y+4,y+8):
                if(gBoard[i][j] != 'X'):
                    gBoard[i][j] = '^'
        for i in range(x-3,x-1):
            for j in range(y,y+4):
                if(gBoard[i][j] != 'X'):
                    gBoard[i][j] = '^'
        for i in range(x+2,x+4):
            for j in range(y,y+4):
                if(gBoard[i][j] != 'X'):
                    gBoard[i][j] = '^'
