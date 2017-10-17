#!/usr/bin/env python
""" This method is for walls on board """

from __future__ import print_function
from bricks import Brick

BRICK = Brick()


class Walls(object):

    """ This init for encapsulation """
    def __init__(self):
        self.size = 4
        self._struct = [[' ' for _ in range(4)] for _ in range(2)]

    def create_wall(self, xcord, ycord, g_board):
        """ This method to create walls """
        for i in range(self.size):
            g_board[xcord][ycord + i] = "X"
            g_board[xcord + 1][ycord + i] = "X"
