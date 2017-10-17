#!/usr/bin/env python
""" This method is for moving enemies on board """

from random import randint
from person import Person
# from bomberman import BomberMan


class Enemy(Person):

    """ This init is for encapsulation """
    def __init__(self):
        Person.__init__(self)
        self.life = 1
        self._test = 0

    def make_enemy(self, xcord, ycord, enemy, bomber, g_board, ptr, enemy_arr):
        """ Method to make a new enemy """
        flag = 0
        for i in range(xcord, xcord + 2):
            for j in range(ycord, ycord + self.size):
                if(bomber[i][j] != 'B' and g_board[i][j] != 'X' and
                   enemy[i][j] != 'E' and g_board[i][j] != '/'):
                    flag = 0
                else:
                    flag = 1
                    break
        if flag == 0:
            for i in range(xcord, xcord + 2):
                for j in range(ycord, ycord + self.size):
                    enemy[i][j] = 'E'
            enemy_arr[ptr][0] = xcord
            enemy_arr[ptr][1] = ycord
            # arr[ptr][0]=xcord
            # arr[ptr][1]=ycord

        else:
            xcord = randint(1, 20) * 2
            ycord = randint(1, 20) * 4
            self.make_enemy(xcord, ycord, enemy, bomber, g_board, ptr, enemy_arr)

    def move_right(self, xcord, ycord, enemy):
        for i in range(ycord + self.size, ycord + 8):
            enemy[xcord][i] = 'E'
            enemy[xcord][i - 4] = ' '
            enemy[xcord + 1][i] = 'E'
            enemy[xcord + 1][i - 4] = ' '
        ycord += 4
        return ycord

    def move_left(self, xcord, ycord, enemy):
        for i in range(ycord - self.size, ycord):
            enemy[xcord][i] = 'E'
            enemy[xcord][i + 4] = ' '
            enemy[xcord + 1][i] = 'E'
            enemy[xcord + 1][i + 4] = ' '
        ycord -= 4
        return ycord

    def move_up(self, xcord, ycord, enemy):
        for i in range(self.size):
            enemy[xcord - 2][ycord + i] = 'E'
            enemy[xcord - 1][ycord + i] = 'E'
            enemy[xcord][ycord + i] = ' '
            enemy[xcord + 1][ycord + i] = ' '
        xcord -= 2
        return xcord

    def move_down(self, xcord, ycord, enemy):
        for i in range(self.size):
            enemy[xcord][ycord + i] = ' '
            enemy[xcord + 1][ycord + i] = ' '
            enemy[xcord + 2][ycord + i] = 'E'
            enemy[xcord + 3][ycord + i] = 'E'
        xcord += 2
        return xcord
