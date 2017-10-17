#!/usr/bin/env python
""" This method is for moving objects on board """

from person import Person


class BomberMan(Person):

    """ This init file for encapsulation """
    def __init__(self):
        Person.__init__(self)
        self.life = 3
        self.score = 0
        self._test = 0

    def make_player(self, xcord, ycord, bomber):
        """ This method to form the bomberman player """
        for i in range(xcord, xcord + 2):
            for j in range(ycord, ycord + self.size):
                bomber[i][j] = "B"
