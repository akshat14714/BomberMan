#!/usr/bin/env python
""" This file is for playing the game """

from __future__ import print_function
import signal
import sys
import copy
# import time
import os
from random import randint
from walls import Walls
from bricks import Brick
# from person import Person
from board import Board
from bomb import Bomb
from bomberman import BomberMan
from enemies import Enemy
from getchunix import GetchUnix
from alarmexception import AlarmException

GBOARD = [[' ' for i in range(84)] for j in range(42)]
BOMBER = copy.deepcopy(GBOARD)
ENEMY = copy.deepcopy(GBOARD)

ENEMY_ARR = [[0 for _ in range(0, 10)] for _ in range(0, 10)]

# for i in range(5):
#    for j in range(2):
#        ENEMYp[i][j] = 0

BOARD = Board()
WALL = Walls()
BRICK = Brick()
GETCH = GetchUnix()
PLAYER = BomberMan()
VILLAN = Enemy()
BOMBS = Bomb()

PLAYERX = 2
PLAYERY = 4

BOMBX = 0
BOMBY = 0

BOARD.make_wall(GBOARD)
BRICK.create_brick(GBOARD)
PLAYER.make_player(PLAYERX, PLAYERY, BOMBER)
for i in range(5):
    ENEMY_ARR[i][0] = randint(1, 20) * 2
    ENEMY_ARR[i][1] = randint(1, 20) * 4
    ENEMY_ARR.append(
        VILLAN.make_enemy(ENEMY_ARR[i][0],
                          ENEMY_ARR[i][1],
                          ENEMY,
                          BOMBER,
                          GBOARD,
                          i,
                          ENEMY_ARR))


def alarm_handler(signum, frame):
    """ To raise interrupts """
    raise AlarmException


def input_to(timeout=1):
    """ Take uninterrupted inputs from keyboard """
    signal.signal(signal.SIGALRM, alarm_handler)
    signal.alarm(timeout)
    try:
        text = GETCH()
        signal.alarm(0)
        return text
    except AlarmException:
        print("\n Prompt timeout. Continuing...")
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''

FLAG = 0
COUNT = 0
EFFECTFL = 0
ENEMYDEATH = 0
ENEMYDIE = [0 for i in range(5)]

while 1:
    N = 5

    print("Total Lives: " + str(PLAYER.life))
    print("Total Score: " + str(PLAYER.score))
    print("w->move up, s->move down, a->move left, d->move right")
    print("Press b to plant a bomb")
    print("To quit, press q")

    if COUNT == 0:
        if FLAG == 1:
            OLD_SCORE = PLAYER.score
            PLAYER.score = BOMBS.explode(
                BOMBX,
                BOMBY,
                GBOARD,
                BOMBER,
                ENEMY,
                PLAYER.score,
                ENEMY_ARR)
            BOMBS.remove(BOMBX, BOMBY, GBOARD)
            if PLAYER.score - OLD_SCORE == 100:
                N -= 1
            if BOMBER[PLAYERX][PLAYERY] == ' ':
                PLAYER.life -= 1
                PLAYERX = 2
                PLAYERY = 4
                PLAYER.make_player(PLAYERX, PLAYERY, BOMBER)
            EFFECTFL = 1
        # COUNT = 4
        FLAG = 0

    if PLAYER.life == 0 or N == 0:
        print("Game Over")
        sys.exit(0)

    if FLAG == 1:
        COUNT -= 1

    BOARD.print_board(
        GBOARD,
        BOMBER,
        ENEMY,
        COUNT,
        BOMBX,
        BOMBY)

    if EFFECTFL == 1:
        BOMBS.remove_effect(BOMBX, BOMBY, GBOARD)
        BOMBX = 0
        BOMBY = 0
        COUNT = 4
        EFFECTFL = 0

    BUTTON = input_to()

    if BUTTON == 'b':
        BOMBS.plant(PLAYERX, PLAYERY, GBOARD, COUNT)
        BOMBX = PLAYERX
        BOMBY = PLAYERY
        COUNT = 4
        FLAG = 1

    elif BUTTON == 'w':
        if PLAYER.check_up(PLAYERX, PLAYERY, GBOARD) == 1:
            PLAYERX = PLAYER.move_up(PLAYERX, PLAYERY, BOMBER)

    elif BUTTON == 's':
        if PLAYER.check_down(PLAYERX, PLAYERY, GBOARD) == 1:
            PLAYERX = PLAYER.move_down(PLAYERX, PLAYERY, BOMBER)

    elif BUTTON == 'a':
        if PLAYER.check_left(PLAYERX, PLAYERY, GBOARD) == 1:
            PLAYERY = PLAYER.move_left(PLAYERX, PLAYERY, BOMBER)

    elif BUTTON == 'd':
        if PLAYER.check_right(PLAYERX, PLAYERY, GBOARD) == 1:
            PLAYERY = PLAYER.move_right(PLAYERX, PLAYERY, BOMBER)

    elif BUTTON == 'q':
        print("Good Bye")
        sys.exit(0)

    for i in range(5):
        lis = ['a', 's', 'w', 'd']
        tmp = 0
        if ENEMY_ARR[i][0] == -1 and ENEMY_ARR[i][1] == -1:
            if ENEMYDIE[i] == 0:
                ENEMYDIE[i] += 1
                ENEMYDEATH += 1
            if ENEMYDEATH == 5:
                print('You killed all the enemies')
                print('You win')
                sys.exit(0)
            continue
        # while tmp==0:
            # enm = randint(0,3)
        enemyMove = randint(0, 3)
        if enemyMove == 0:
            if VILLAN.check_up(ENEMY_ARR[i][0], ENEMY_ARR[i][1], GBOARD) == 1:
                ENEMY_ARR[i][0] = VILLAN.move_up(
                    ENEMY_ARR[i][0],
                    ENEMY_ARR[i][1],
                    ENEMY)
                if(((ENEMY_ARR[i][0] == PLAYERX + 2 or
                     ENEMY_ARR[i][0] == PLAYERX - 2) and
                        (ENEMY_ARR[i][1] == PLAYERY)) or
                   ((ENEMY_ARR[i][0] == PLAYERX) and
                    (ENEMY_ARR[i][1] == PLAYERY - 4 or
                     ENEMY_ARR[i][1] == PLAYERY + 4))):
                    print(PLAYERX)
                    print(PLAYERY)
                    # PLAYER.remove(palyerx, PLAYERY, BOMBER)
                    for k in range(PLAYERX, PLAYERX + 2):
                        for l in range(PLAYERY, PLAYERY + 4):
                            BOMBER[k][l] = ' '
                    PLAYER.life -= 1
                    PLAYERX = 2
                    PLAYERY = 4
                    PLAYER.make_player(PLAYERX, PLAYERY, BOMBER)
                tmp = 1

        elif enemyMove == 1:
            if(VILLAN.check_down(ENEMY_ARR[i][0],
                                 ENEMY_ARR[i][1], GBOARD) == 1):
                tmp = 1
                ENEMY_ARR[i][0] = VILLAN.move_down(
                    ENEMY_ARR[i][0],
                    ENEMY_ARR[i][1],
                    ENEMY)
                if(((ENEMY_ARR[i][0] == PLAYERX + 2 or
                     ENEMY_ARR[i][0] == PLAYERX - 2) and
                        (ENEMY_ARR[i][1] == PLAYERY)) or
                   ((ENEMY_ARR[i][0] == PLAYERX) and
                    (ENEMY_ARR[i][1] == PLAYERY - 4 or
                     ENEMY_ARR[i][1] == PLAYERY + 4))):
                    # PLAYER.remove(palyerx, PLAYERY, BOMBER)
                    for k in range(PLAYERX, PLAYERX + 2):
                        for l in range(PLAYERY, PLAYERY + 4):
                            BOMBER[k][l] = ' '
                    PLAYER.life -= 1
                    PLAYERX = 2
                    PLAYERY = 4
                    PLAYER.make_player(PLAYERX, PLAYERY, BOMBER)

        elif enemyMove == 2:
            if(VILLAN.check_left(ENEMY_ARR[i][0],
                                 ENEMY_ARR[i][1], GBOARD) == 1):
                tmp = 1
                ENEMY_ARR[i][1] = VILLAN.move_left(
                    ENEMY_ARR[i][0],
                    ENEMY_ARR[i][1],
                    ENEMY)
                if(((ENEMY_ARR[i][0] == PLAYERX + 2 or
                     ENEMY_ARR[i][0] == PLAYERX - 2) and
                        (ENEMY_ARR[i][1] == PLAYERY)) or
                   ((ENEMY_ARR[i][0] == PLAYERX) and
                    (ENEMY_ARR[i][1] == PLAYERY - 4 or
                     ENEMY_ARR[i][1] == PLAYERY + 4))):
                    for k in range(PLAYERX, PLAYERX + 2):
                        for l in range(PLAYERY, PLAYERY + 4):
                            BOMBER[k][l] = ' '
                    PLAYER.life -= 1
                    PLAYERX = 2
                    PLAYERY = 4
                    PLAYER.make_player(PLAYERX, PLAYERY, BOMBER)

        elif enemyMove == 3:
            if(VILLAN.check_right(ENEMY_ARR[i][0],
                                  ENEMY_ARR[i][1], GBOARD) == 1):
                tmp = 1
                ENEMY_ARR[i][1] = VILLAN.move_right(
                    ENEMY_ARR[i][0],
                    ENEMY_ARR[i][1],
                    ENEMY)
                if(((ENEMY_ARR[i][0] == PLAYERX + 2 or
                     ENEMY_ARR[i][0] == PLAYERX - 2) and
                        (ENEMY_ARR[i][1] == PLAYERY)) or
                   ((ENEMY_ARR[i][0] == PLAYERX) and
                    (ENEMY_ARR[i][1] == PLAYERY - 4 or
                     ENEMY_ARR[i][1] == PLAYERY + 4))):
                    # PLAYER.remove(palyerx, PLAYERY, BOMBER)
                    for k in range(PLAYERX, PLAYERX + 2):
                        for l in range(PLAYERY, PLAYERY + 4):
                            BOMBER[k][l] = ' '
                    PLAYER.life -= 1
                    PLAYERX = 2
                    PLAYERY = 4
                    PLAYER.make_player(PLAYERX, PLAYERY, BOMBER)

    os.system("clear")
