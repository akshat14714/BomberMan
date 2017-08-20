from __future__ import print_function
import signal,sys,copy,time,os
from random import randint
from walls import *
from bricks import *
from person import *
from board import *
from bomb import *
from bomberman import *
from enemies import *
from getchunix import *
from alarmexception import *

gBoard = [[' ' for i in range(boardSizex)] for j in range(boardSizey)]
bomber = copy.deepcopy(gBoard)
enemy = copy.deepcopy(gBoard)

enemy_arr = [[0 for i in range (0,10)] for j in range (0,10)]

#for i in range(5):
#    for j in range(2):
#        enemyp[i][j] = 0

board = Board()
wall = Walls()
brick = Brick()
getch = GetchUnix()
player = BomberMan()
villan = Enemy()
bombs = Bomb()

playerx = 2
playery = 4

bombx = 0
bomby = 0

board.makeWall(gBoard)
brick.createBrick(gBoard)
player.makePlayer(playerx, playery, bomber)
for i in range(5):
    enemy_arr[i][0] = randint(1,20)*2
    enemy_arr[i][1] = randint(1,20)*4
    enemy_arr.append(villan.makeEnemy(enemy_arr[i][0], enemy_arr[i][1],enemy,bomber, gBoard,i,enemy_arr))

def alarmHandler(signum, frame):
    raise AlarmException

def input_to(timeout=1):
    signal.signal(signal.SIGALRM, alarmHandler)
    signal.alarm(timeout)
    try:
        text = getch()
        signal.alarm(0)
        return text
    except AlarmException:
        print("\n Prompt timeout. Continuing...")
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''

flag = 0
count = 0
effectfl = 0

while(1):
    print("Total Lives: " + str(player.life))
    print("Total Score: " + str(player.score))
    print("w->move up, s->move down, a->move left, d->move right")
    print("Press b to plant a bomb")
    print("To quit, press q")

    if count==0:
        if(flag==1):
            player.score = bombs.explode(bombx, bomby, gBoard, playerx, playery, bomber, enemy, player.score)
            bombs.remove(bombx, bomby, gBoard)
            if(bomber[playerx][playery] == ' '):
                player.life -= 1
                playerx = 2
                playery = 4
                player.makePlayer(playerx, playery, bomber)
            effectfl = 1
        # count = 4
        flag = 0

    if(player.life == 0):
        print("Game Over")
        sys.exit(0)

    if(flag == 1):
        count -= 1

    board.printBoard(gBoard, bomber, playerx, playery, enemy, count, bombx, bomby)

    if(effectfl == 1):
        bombs.removeEffect(bombx, bomby, gBoard)
        bombx = 0
        bomby = 0
        count = 4
        effectfl = 0

    button = input_to()

    if(button == 'b'):
        bombs.plant(playerx, playery, gBoard, count)
        bombx = playerx
        bomby = playery
        count = 4
        flag = 1

    elif(button == 'w'):
        if(player.checkUp(playerx, playery, gBoard) == 1):
            playerx = player.moveUp(playerx, playery, bomber)

    elif(button == 's'):
        if(player.checkDown(playerx, playery, gBoard) == 1):
            playerx = player.moveDown(playerx, playery, bomber)

    elif(button == 'a'):
        if(player.checkLeft(playerx, playery, gBoard) == 1):
            playery = player.moveLeft(playerx, playery, bomber)

    elif(button == 'd'):
        if(player.checkRight(playerx, playery, gBoard) == 1):
            playery = player.moveRight(playerx, playery, bomber)

    elif(button == 'q'):
        print("END")
        sys.exit(0)

    for i in range(5):
        lis = ['a', 's', 'w', 'd']
        tmp=0
        while tmp==0:
            enm = randint(0,3)
            enemyMove = lis[enm]
            if(enemyMove == 'w'):
                if(villan.checkUp(enemy_arr[i][0], enemy_arr[i][1], gBoard) == 1):
                    enemy_arr[i][0] = villan.moveUp(enemy_arr[i][0], enemy_arr[i][1], enemy)
                    if(((enemy_arr[i][0]==playerx+2 or enemy_arr[i][0]==playerx-2) and (enemy_arr[i][1]==playery)) or ((enemy_arr[i][0]==playerx) and (enemy_arr[i][1]==playery-4 or enemy_arr[i][1]==playery+4))):
                        print(playerx)
                        print(playery)
                        #player.remove(palyerx, playery, bomber)
                        for k in range(playerx, playerx+2):
                            for l in range(playery, playery+4):
                                bomber[k][l] = ' '
                        player.life -= 1
                        playerx = 2
                        playery = 4
                        player.makePlayer(playerx, playery, bomber)
                    tmp=1

            elif(enemyMove == 's'):
                if(villan.checkDown(enemy_arr[i][0], enemy_arr[i][1], gBoard) == 1):
                    tmp=1
                    enemy_arr[i][0] = villan.moveDown(enemy_arr[i][0], enemy_arr[i][1], enemy)
                    if(((enemy_arr[i][0]==playerx+2 or enemy_arr[i][0]==playerx-2) and (enemy_arr[i][1]==playery)) or ((enemy_arr[i][0]==playerx) and (enemy_arr[i][1]==playery-4 or enemy_arr[i][1]==playery+4))):
                        #player.remove(palyerx, playery, bomber)
                        for k in range(playerx, playerx+2):
                            for l in range(playery, playery+4):
                                bomber[k][l] = ' '
                        player.life -= 1
                        playerx = 2
                        playery = 4
                        player.makePlayer(playerx, playery, bomber)

            elif(enemyMove == 'a'):
                if(villan.checkLeft(enemy_arr[i][0], enemy_arr[i][1], gBoard) == 1):
                    tmp=1
                    enemy_arr[i][1] = villan.moveLeft(enemy_arr[i][0], enemy_arr[i][1], enemy)
                    if(((enemy_arr[i][0]==playerx+2 or enemy_arr[i][0]==playerx-2) and (enemy_arr[i][1]==playery)) or ((enemy_arr[i][0]==playerx) and (enemy_arr[i][1]==playery-4 or enemy_arr[i][1]==playery+4))):
                        for k in range(playerx, playerx+2):
                            for l in range(playery, playery+4):
                                bomber[k][l] = ' '
                        player.life -= 1
                        playerx = 2
                        playery = 4
                        player.makePlayer(playerx, playery, bomber)

            elif(enemyMove == 'd'):
                if(villan.checkRight(enemy_arr[i][0], enemy_arr[i][1], gBoard) == 1):
                    tmp=1
                    enemy_arr[i][1] = villan.moveRight(enemy_arr[i][0], enemy_arr[i][1], enemy)
                    if(((enemy_arr[i][0]==playerx+2 or enemy_arr[i][0]==playerx-2) and (enemy_arr[i][1]==playery)) or ((enemy_arr[i][0]==playerx) and (enemy_arr[i][1]==playery-4 or enemy_arr[i][1]==playery+4))):
                        #player.remove(palyerx, playery, bomber)
                        for k in range(playerx, playerx+2):
                            for l in range(playery, playery+4):
                                bomber[k][l] = ' '
                        player.life -= 1
                        playerx = 2
                        playery = 4
                        player.makePlayer(playerx, playery, bomber)

    os.system("clear")
