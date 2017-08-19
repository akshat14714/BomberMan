from __future__ import print_function
import signal,sys,copy,time,os
from random import randint
from walls import *
from bricks import *
from person import *
from board import *
#from bomb import *
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

playerx = 2
playery = 4

# enemyx=0
# enemyy=0

board.makeWall(gBoard)
brick.createBrick(gBoard)
player.makePlayer(playerx, playery, bomber)
for i in range(5):
    enemy_arr[i][0] = randint(1,20)*2
    enemy_arr[i][1] = randint(1,20)*4
    enemy_arr.append(villan.makeEnemy(enemy_arr[i][0], enemy_arr[i][1],enemy,bomber, gBoard,i,enemy_arr))
board.printBoard(gBoard, bomber, playerx, playery, enemy)

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

while(1):
    button = input_to()
    #print(button)
    if(button == 'w'):
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
                    tmp=1

            elif(enemyMove == 's'):
                if(villan.checkDown(enemy_arr[i][0], enemy_arr[i][1], gBoard) == 1):
                    tmp=1
                    enemy_arr[i][0] = villan.moveDown(enemy_arr[i][0], enemy_arr[i][1], enemy)

            elif(enemyMove == 'a'):
                if(villan.checkLeft(enemy_arr[i][0], enemy_arr[i][1], gBoard) == 1):
                    tmp=1
                    enemy_arr[i][1] = villan.moveLeft(enemy_arr[i][0], enemy_arr[i][1], enemy)

            elif(enemyMove == 'd'):
                if(villan.checkRight(enemy_arr[i][0], enemy_arr[i][1], gBoard) == 1):
                    tmp=1
                    enemy_arr[i][1] = villan.moveRight(enemy_arr[i][0], enemy_arr[i][1], enemy)

    board.printBoard(gBoard, bomber, playerx, playery, enemy)
