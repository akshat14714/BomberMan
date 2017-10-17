#!/usr/bin/env python
""" This class is for the main board for game """

from __future__ import print_function
from termcolor import colored
# from bricks import Brick
from walls import Walls

# wall = Walls()
# brick = Brick()


class Board(object):

    """ This init is just for encapsulation """
    def __init__(self):
        self.sizex = 84
        self.sizey = 42
        self._test = 0

    def make_wall(self, g_board):
        """ This method creates walls on the borad """
        for i in range(0, self.sizey, 2):
            for j in range(0, self.sizex, 4):
                if(i == 0 or j == 0 or i == 42 - 2 or
                   j == 84 - 4 or
                   (i % 4 == 0 and j % 8 == 0 and
                    j < 84 - 4 and i < 42 - 2)):
                    Walls().create_wall(i, j, g_board)

    def print_board(self, g_board, bomber, enemy, count, bombx, bomby):
        """ This method prints the main board for the game """
        for i in range(self.sizey):
            for j in range(self.sizex):
                if(i == bombx and j == bomby and g_board[i][j] != 'X' and
                   g_board[i][j] != '/'):
                    for k in range(i, i + 2):
                        for _ in range(j, j + 4):
                            if count != 0:
                                g_board[k][_] = count
                    bombx = 0
                    bomby = 0
                if bomber[i][j] == 'B':
                    print(colored(bomber[i][j], 'cyan'), end='')
                elif enemy[i][j] == 'E':
                    print(colored(enemy[i][j], 'red'), end='')
                elif g_board[i][j] == '/':
                    print(colored(g_board[i][j], 'yellow'), end='')
                elif(g_board[i][j] == 'v' or g_board[i][j] == '^' or
                     g_board[i][j] == '>' or g_board[i][j] == '<' or
                     g_board[i][j] == count):
                    print(colored(g_board[i][j], 'magenta'), end='')
                else:
                    print(g_board[i][j], end='')
            print()
