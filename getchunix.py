#!/usr/bin/env python
""" This file is just to handle uninterrupted keyboard inputs """

from __future__ import print_function
# import copy
# import signal
# import sys
# import time
# from random import randint


class GetchUnix(object):

    """ This is init for encapsulation """
    def __init__(self):
        import tty

    def __call__(self):
        import sys
        import tty
        import termios
        f_d = sys.stdin.fileno()
        old_settings = termios.tcgetattr(f_d)
        try:
            tty.setraw(sys.stdin.fileno())
            c_h = sys.stdin.read(1)
        finally:
            termios.tcsetattr(f_d, termios.TCSADRAIN, old_settings)
        return c_h
