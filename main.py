from __future__ import print_function
import signal,sys,copy,time
from random import randint
from walls import *
#from bricks import *
#from person import *
from board import *
#from bomb import *
#from bomberman import *
from getchunix import *
from alarmexception import *

gBoard = [[' ' for i in range(boardSizex)] for j in range(boardSizey)]
bomber = copy.deepcopy(gBoard)


board = Board()
wall = Walls()
brick = Brick()
getch = GetchUnix()
#player = BomberMan()

def AlarmHandler(signum, frame):
    return AlarmException

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

board.makeWall(gBoard)

board.printBoard(gBoard)
