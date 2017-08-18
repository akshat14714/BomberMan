class Person:
    def __init__(self):
        self._test = 0

    def checkRight(self, x, y, gBoard):
        for p in range(4):
            if(gBoard[x][y+p+4]=='X' or gBoard[x+1][y+p+4]=='X' or gBoard[x][y+p+4]=='E' or gBoard[x+1][y+p+4]=='E' or gBoard[x][y+4+p]=='B' or gBoard[x+1][y+p+4]=='B'):
                return 0
        return 1

    def checkLeft(self, x, y, gBoard):
        for p in range(4):
            if(gBoard[x][y-p-1]=='X' or gBoard[x+1][y-p-1]=='X' or gBoard[x][y-p-1]=='E' or gBoard[x+1][y-p-1]=='E' or gBoard[x][y-p-1]=='B' or gBoard[x+1][y-p-1]=='B'):
                return 0
        return 1

    def checkUp(self, x, y, gBoard):
        for p in range(2):
            for q in range(4):
                if(gBoard[x-p-1][y+q]=='X' or gBoard[x-p-1][y+q]=='E' or gBoard[x-p-1][y+q]=='B'):
                    return 0
        return 1

    def checkDown(self, x, y, gBoard):
        for p in range(2):
            for q in range(4):
                if(gBoard[x+p+1][y+q]=='X' or gBoard[x+p+1][y+q]=='E' or gBoard[x+p+1][y+q]=='B'):
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

    def moveRightE(self, x, y, enemy):
        for i in range(y+4,y+8):
            enemy[x][i] = 'E'
            enemy[x][i-4] = ' '
            enemy[x+1][i] = 'E'
            enemy[x+1][i-4] = ' '
        y += 4
        return y

    def moveLeftE(self, x, y, enemy):
        for i in range(y-4,y):
            enemy[x][i] = 'E'
            enemy[x][i+4] = ' '
            enemy[x+1][i] = 'E'
            enemy[x+1][i+4] = ' '
        y -= 4
        return y

    def moveUpE(self, x, y, enemy):
        for i in range(4):
            enemy[x-2][y+i] = 'E'
            enemy[x-1][y+i] = 'E'
            enemy[x][y+i] = ' '
            enemy[x+1][y+i] = ' '
        x -= 2
        return x

    def moveDownE(self, x, y, enemy):
        for i in range(4):
            enemy[x][y+i] = ' '
            enemy[x+1][y+i] = ' '
            enemy[x+2][y+i] = 'E'
            enemy[x+3][y+i] = 'E'
        x += 2
        return x
