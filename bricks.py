#!/usr/bin/env python
""" This file is for creating and deleting bricks from the board """

from __future__ import print_function
from random import randint


class Brick(object):

    """ This is just an init file to show encapsulation """
    def __init__(self):
        self._test = 0
        self.size = 4

    def create_brick(self, g_board):
        """ Method to create a new brick """
        counter = 0
        while counter < 35:
            xcord = randint(2, 38)
            ycord = randint(3, 80)
            if(g_board[xcord][ycord] == ' ' and
               ((xcord % 4 == 0 and ycord % 8 == 0) or
                (xcord % 4 == 2 and ycord % 8 == 4) or
                (xcord % 4 == 2 and ycord % 8 == 0) or
                (xcord % 4 == 0 and ycord % 8 == 4))):
                for _ in range(self.size):
                    g_board[xcord][ycord + _] = "/"
                    g_board[xcord + 1][ycord + _] = "/"
                counter += 1

    def remove(self, xcord, ycord, g_board):
        """ Method to remove a brick from board """
        for i in range(xcord, xcord + 2):
            for j in range(ycord, ycord + self.size):
                g_board[i][j] = ' '
