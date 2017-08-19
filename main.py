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
enemyp = [[0 for j in range(2)] for i in range(5)]

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

enemyx = 0
enemyy = 0

board.makeWall(gBoard)
brick.createBrick(gBoard)
player.makePlayer(playerx, playery, bomber)
enemyx = randint(1,20)*2
enemyy = randint(1,20)*4
villan.makeEnemy(enemyx, enemyy, enemy, bomber, gBoard)
board.printBoard(gBoard, bomber, playerx, playery, enemy, enemyx, enemyy)

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

    lis = ['a', 's', 'w', 'd']
    enm = randint(0,3)
    enemyMove = lis[enm]

    if(enemyMove == 'w'):
        if(villan.checkUp(enemyx, enemyy, gBoard) == 1):
            enemyx = villan.moveUp(enemyx, enemyy, enemy)

    elif(enemyMove == 's'):
        if(villan.checkDown(enemyx, enemyy, gBoard) == 1):
            enemyx = villan.moveDown(enemyx, enemyy, enemy)

    elif(enemyMove == 'a'):
        if(villan.checkLeft(enemyx, enemyy, gBoard) == 1):
            enemyy = villan.moveLeft(enemyx, enemyy, enemy)

    elif(enemyMove == 'd'):
        if(villan.checkRight(enemyx, enemyy, gBoard) == 1):
            enemyy = villan.moveRight(enemyx, enemyy, enemy)

    board.printBoard(gBoard, bomber, playerx, playery, enemy, enemyx, enemyy)
