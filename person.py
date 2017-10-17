#!/usr/bin/env python
""" This method is for moving objects on board """

class Person(object):

    """ This init for encapsulation """
    def __init__(self):
        self._test = 0
        self.size = 4

    def check_right(self, xcord, ycord, g_board):
        """ Method to check for right movement """
        for _ in range(self.size):
            if(g_board[xcord][ycord + _ + 4] == 'X' or
               g_board[xcord + 1][ycord + _ + 4] == 'X' or
               g_board[xcord][ycord + _ + 4] == 'E' or g_board[xcord][ycord + _ + 4] == '/' or
               g_board[xcord + 1][ycord + _ + 4] == 'E' or
               g_board[xcord][ycord + 4 + _] == 'B' or
               g_board[xcord + 1][ycord + _ + 4] == 'B' or
               g_board[xcord + 1][ycord + _ + 4] == '/'):
                return 0
        return 1

    def check_left(self, xcord, ycord, g_board):
        """ Method to check for left movement """
        for _ in range(self.size):
            if(g_board[xcord][ycord - _ - 1] == 'X' or
               g_board[xcord + 1][ycord - _ - 1] == 'X' or
               g_board[xcord][ycord - _ - 1] == 'E' or
               g_board[xcord + 1][ycord - _ - 1] == 'E' or
               g_board[xcord][ycord - _ - 1] == 'B' or
               g_board[xcord + 1][ycord - _ - 1] == 'B' or
               g_board[xcord][ycord - _ - 1] == '/' or
               g_board[xcord + 1][ycord - _ - 1] == '/'):
                return 0
        return 1

    def check_up(self, xcord, ycord, g_board):
        """ Method to check for upward movement """
        for p_e in range(2):
            for q_e in range(self.size):
                if(g_board[xcord - p_e - 1][ycord + q_e] == 'X' or
                   g_board[xcord - p_e - 1][ycord + q_e] == '/' or
                   g_board[xcord - p_e - 1][ycord + q_e] == 'E' or
                   g_board[xcord - p_e - 1][ycord + q_e] == 'B'):
                    return 0
        return 1

    def check_down(self, xcord, ycord, g_board):
        """ Method to check for downward movement """
        for p_e in range(2):
            for q_e in range(self.size):
                if(g_board[xcord + p_e + 2][ycord + q_e] == 'X' or
                   g_board[xcord + p_e + 2][ycord + q_e] == '/' or
                   g_board[xcord + p_e + 2][ycord + q_e] == 'E' or
                   g_board[xcord + p_e + 2][ycord + q_e] == 'B'):
                    return 0
        return 1

    def move_right(self, xcord, ycord, bomber):
        """ Method to move right """
        for i in range(ycord + self.size, ycord + 8):
            bomber[xcord][i] = 'B'
            bomber[xcord][i - 4] = ' '
            bomber[xcord + 1][i] = 'B'
            bomber[xcord + 1][i - 4] = ' '
        ycord += 4
        return ycord

    def move_left(self, xcord, ycord, bomber):
        """ Method to move left """
        for i in range(ycord - self.size, ycord):
            bomber[xcord][i] = 'B'
            bomber[xcord][i + 4] = ' '
            bomber[xcord + 1][i] = 'B'
            bomber[xcord + 1][i + 4] = ' '
        ycord -= 4
        return ycord

    def move_up(self, xcord, ycord, bomber):
        """ Method to move up """
        for i in range(self.size):
            bomber[xcord - 2][ycord + i] = 'B'
            bomber[xcord - 1][ycord + i] = 'B'
            bomber[xcord][ycord + i] = ' '
            bomber[xcord + 1][ycord + i] = ' '
        xcord -= 2
        return xcord

    def move_down(self, xcord, ycord, bomber):
        """ Method to move down """
        for i in range(self.size):
            bomber[xcord][ycord + i] = ' '
            bomber[xcord + 1][ycord + i] = ' '
            bomber[xcord + 2][ycord + i] = 'B'
            bomber[xcord + 3][ycord + i] = 'B'
        xcord += 2
        return xcord

    def remove(self, xcord, ycord, arr):
        """ Method for removal of any person """
        for i in range(xcord, xcord + 2):
            for j in range(ycord, ycord + self.size):
                arr[i][j] = ' '
