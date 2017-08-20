class Person:
    def __init__(self):
        self._test = 0

    def checkRight(self, x, y, gBoard):
        for p in range(4):
            if(gBoard[x][y+p+4]=='X' or gBoard[x+1][y+p+4]=='X' or gBoard[x][y+p+4]=='E' or gBoard[x][y+p+4]=='/' or gBoard[x+1][y+p+4]=='E' or gBoard[x][y+4+p]=='B' or gBoard[x+1][y+p+4]=='B' or gBoard[x+1][y+p+4]=='/'):
                return 0
        return 1

    def checkLeft(self, x, y, gBoard):
        for p in range(4):
            if (gBoard[x][y-p-1]=='X' or gBoard[x+1][y-p-1]=='X' or gBoard[x][y-p-1]=='E' or gBoard[x+1][y-p-1]=='E' or gBoard[x][y-p-1]=='B' or gBoard[x+1][y-p-1]=='B' or gBoard[x][y-p-1]=='/' or gBoard[x+1][y-p-1]=='/'):
                return 0
        return 1

    def checkUp(self, x, y, gBoard):
        for p in range(2):
            for q in range(4):
                if (gBoard[x-p-1][y+q]=='X' or gBoard[x-p-1][y+q]=='/' or gBoard[x-p-1][y+q]=='E' or gBoard[x-p-1][y+q]=='B'):
                    return 0
        return 1

    def checkDown(self, x, y, gBoard):
        for p in range(2):
            for q in range(4):
                if (gBoard[x+p+1][y+q]=='X' or gBoard[x+p+1][y+q]=='/' or gBoard[x+p+1][y+q]=='E' or gBoard[x+p+1][y+q]=='B'):
                    return 0
        return 1

    def moveRight(self, x, y, bomber):
        for i in range(y+4,y+8):
            bomber[x][i] = 'B'
            bomber[x][i-4] = ' '
            bomber[x+1][i] = 'B'
            bomber[x+1][i-4] = ' '
        y += 4
        return y

    def moveLeft(self, x, y, bomber):
        for i in range(y-4,y):
            bomber[x][i] = 'B'
            bomber[x][i+4] = ' '
            bomber[x+1][i] = 'B'
            bomber[x+1][i+4] = ' '
        y -= 4
        return y

    def moveUp(self, x, y, bomber):
        for i in range(4):
            bomber[x-2][y+i] = 'B'
            bomber[x-1][y+i] = 'B'
            bomber[x][y+i] = ' '
            bomber[x+1][y+i] = ' '
        x -= 2
        return x

    def moveDown(self, x, y, bomber):
        for i in range(4):
            bomber[x][y+i] = ' '
            bomber[x+1][y+i] = ' '
            bomber[x+2][y+i] = 'B'
            bomber[x+3][y+i] = 'B'
        x += 2
        return x

    def remove(self, x, y, arr):
        for i in range(x,x+2):
            for j in range(y,y+4):
                arr[i][j] = ' '
