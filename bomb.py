class Bomb:
    def __init__(self):
        self._test = 0

    def plant(self, x, y, gBoard, count):
        for i in range(x,x+2):
            for j in range(y,y+4):
                gBoard[i][j] = count

    def explode(self, x, y, gBoard, playerx, playery, bomber, enemy, score):
        flag = 0
        for i in range(x,x+2):
            for j in range(y-4,y):
                if(gBoard[i][j] != 'X'):
                    if(bomber[i][j]=='B'):
                        bomber[i][j] = ' '
                    if(enemy[i][j]=='E'):
                        enemy[i][j] = ' '
                        flag = 1
                    if(gBoard[i][j] == '/'):
                        flag = 2
                    gBoard[i][j] = '<'
            for j in range(y+4,y+8):
                if(gBoard[i][j] != 'X'):
                    if(bomber[i][j]=='B'):
                        bomber[i][j] = ' '
                    if(enemy[i][j]=='E'):
                        enemy[i][j] = ' '
                        flas = 1
                    if(gBoard[i][j] == '/'):
                        flag = 2
                    gBoard[i][j] = '>'
        for i in range(x-2,x):
            for j in range(y,y+4):
                if(gBoard[i][j] != 'X'):
                    if(bomber[i][j]=='B'):
                        bomber[i][j] = ' '
                    if(enemy[i][j]=='E'):
                        enemy[i][j] = ' '
                        flag = 1
                    if(gBoard[i][j] == '/'):
                        flag = 2
                    gBoard[i][j] = '^'
        for i in range(x+2,x+4):
            for j in range(y,y+4):
                if(gBoard[i][j] != 'X'):
                    if(bomber[i][j]=='B'):
                        bomber[i][j] = ' '
                    if(enemy[i][j]=='E'):
                        enemy[i][j] = ' '
                        flag = 1
                    if(gBoard[i][j] == '/'):
                        flag = 2
                    gBoard[i][j] = 'v'
        if(flag==1):
            score += 100
        elif(flag==2):
            score += 20
        return score

    def remove(self, x, y, gBoard):
        for i in range(x,x+2):
            for j in range(y,y+4):
                gBoard[i][j] = ' '

    def removeEffect(self, x, y, gBoard):
        for i in range(x,x+2):
            for j in range(y-4,y):
                if(gBoard[i][j] == '<'):
                    gBoard[i][j] = ' '
            for j in range(y+4,y+8):
                if(gBoard[i][j] == '>'):
                    gBoard[i][j] = ' '
        for i in range(x-2,x):
            for j in range(y,y+4):
                if(gBoard[i][j] == '^'):
                    gBoard[i][j] = ' '
        for i in range(x+2,x+4):
            for j in range(y,y+4):
                if(gBoard[i][j] == 'v'):
                    gBoard[i][j] = ' '
