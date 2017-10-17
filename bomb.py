#!/usr/bin/env python
""" This file for the main bomb class """

class Bomb(object):

    """ This init is just for encapsulation """
    def __init__(self):
        self.size = 4
        self._test = 0

    def plant(self, xcord, ycord, g_board, count):
        """ This method is for planting the bomb """
        for i in range(xcord, xcord + 2):
            for j in range(ycord, ycord + self.size):
                g_board[i][j] = count

    def explode(
            self,
            xcord,
            ycord,
            g_board,
            bomber,
            enemy,
            score,
            enemyarr):
        """ This method is for explosion of the bomb """
        flag = 0
        for i in range(xcord, xcord + 2):
            for j in range(ycord - self.size, ycord):
                if g_board[i][j] != 'X':
                    if bomber[i][j] == 'B':
                        bomber[i][j] = ' '
                    if enemy[i][j] == 'E':
                        enemy[i][j] = ' '
                        for k in range(5):
                            if(enemyarr[k][0] == i and
                               enemyarr[k][1] == j):
                                enemyarr[k][0] = -1
                                enemyarr[k][1] = -1
                                flag = 1
                                break
                        flag = 1
                    if g_board[i][j] == '/':
                        flag = 2
                    g_board[i][j] = '<'
            for j in range(ycord + self.size, ycord + 8):
                if g_board[i][j] != 'X':
                    if bomber[i][j] == 'B':
                        bomber[i][j] = ' '
                    if enemy[i][j] == 'E':
                        enemy[i][j] = ' '
                        for k in range(5):
                            if(enemyarr[k][0] == i and
                               enemyarr[k][1] == j):
                                enemyarr[k][0] = -1
                                enemyarr[k][1] = -1
                                # enemy_arr.remove(k)
                                flag = 1
                                break
                        # flas = 1
                    if g_board[i][j] == '/':
                        flag = 2
                    g_board[i][j] = '>'
        for i in range(xcord - 2, xcord):
            for j in range(ycord, ycord + self.size):
                if g_board[i][j] != 'X':
                    if bomber[i][j] == 'B':
                        bomber[i][j] = ' '
                    if enemy[i][j] == 'E':
                        enemy[i][j] = ' '
                        for k in range(5):
                            if(enemyarr[k][0] == i and
                               enemyarr[k][1] == j):
                                enemyarr[k][0] = -1
                                enemyarr[k][1] = -1
                                flag = 1
                                break
                        flag = 1
                    if g_board[i][j] == '/':
                        flag = 2
                    g_board[i][j] = '^'
        for i in range(xcord + 2, xcord + 4):
            for j in range(ycord, ycord + self.size):
                if g_board[i][j] != 'X':
                    if bomber[i][j] == 'B':
                        bomber[i][j] = ' '
                    if enemy[i][j] == 'E':
                        enemy[i][j] = ' '
                        for k in range(5):
                            if(enemyarr[k][0] == i and
                               enemyarr[k][1] == j):
                                enemyarr[k][0] = -1
                                enemyarr[k][1] = -1
                                flag = 1
                                break
                    if g_board[i][j] == '/':
                        flag = 2
                    g_board[i][j] = 'v'
        if flag == 1:
            score += 100
        # n -= 1
        elif flag == 2:
            score += 20
        return score

    def remove(self, xcord, ycord, g_board):
        """ This method is for removing the bomb after explosion """
        for i in range(xcord, xcord + 2):
            for j in range(ycord, ycord + self.size):
                g_board[i][j] = ' '

    def remove_effect(self, xcord, ycord, g_board):
        """ This method is for removing the effects of explosion """
        for i in range(xcord, xcord + 2):
            for j in range(ycord - self.size, ycord):
                if g_board[i][j] == '<':
                    g_board[i][j] = ' '
            for j in range(ycord + self.size, ycord + 8):
                if g_board[i][j] == '>':
                    g_board[i][j] = ' '
        for i in range(xcord - 2, xcord):
            for j in range(ycord, ycord + self.size):
                if g_board[i][j] == '^':
                    g_board[i][j] = ' '
        for i in range(xcord + 2, xcord + 4):
            for j in range(ycord, ycord + self.size):
                if g_board[i][j] == 'v':
                    g_board[i][j] = ' '
