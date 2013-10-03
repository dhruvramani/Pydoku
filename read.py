#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''The 'I' in 'I/O' (gets the Sudoku from the user)'''

import sys, os
import tty, termios

from constants import BLANK_CELL, SMALL_TEMPLATE


# make sure it'll work
# TODO: make it work with Windows
assert os.name == 'posix', "terminal is not posix"

# read 3 chars
def _read():
    bits = []
    bit = []

    # repeat till we get 3 (valid) bits
    while len(bits) < 3:
        sys.stdout.flush()

        # turn echo off (to get chars on type)
        tty.setcbreak(sys.stdin)
        old_settings = termios.tcgetattr(sys.stdin)
        # encase in `try .. finally` construct
        # to not leave the terminal screwed up
        try:
            char = sys.stdin.read(1)
        # turn echo back on
        finally:
            fd  = sys.stdin.fileno()
            old = termios.tcgetattr(fd)
            old[3] |= termios.ECHO
            termios.tcsetattr(fd, termios.TCSADRAIN, old)

        # try to parse the character now
        try:
            if ord(char) == 127:
                char = '\b'
                if len(bits) > 0:
                    bits.pop()
                else:
                    raise ValueError('')
            elif char == ' ':
                bit = list(BLANK_CELL)
            else:
                char = int(char)
                bit  = [char]
        # if invalid, pretend that as if nothing happened
        except ValueError:
            pass
        # if valid, provide feedback and remember it
        else:
            if char != '\b':
                bits.append(bit)
            print(char, end='')

    return bits

# do the whole thing
def read():
    print("Enter the known numbers " + \
          "(leaving spaces for those you don't know)...")
    bits = []
    template = SMALL_TEMPLATE.split('   ')
    for elem in template[:-1]:
        print(elem, end='')
        bit = _read()
        bits.extend(bit)
    print(template[-1])
    board = [bits[i*9:i*9+9] for i in range(9)]
    return board


# for x in range(100):
#     print ('\rDownloading: %s (%d%%)' % ("|"*(x//2), x), end='')
#     sys.stdout.flush()
#     sleep(0.1)

# def echo(func):
#     # make sure it'll work
#     assert os.name == 'posix', "terminal is not posix"

#     # turn echo off
#     tty.setcbreak(sys.stdin)
#     old_settings = termios.tcgetattr(sys.stdin)

#     # encase in `try .. finally` construct
#     # to not leave the terminal screwed up
#     try:
#         # execute and capture return value of callback
#         value = func()
#     finally:
#         # turn echo back on
#         fd  = sys.stdin.fileno()
#         old = termios.tcgetattr(fd)
#         old[3] |= termios.ECHO
#         termios.tcsetattr(fd, termios.TCSADRAIN, old)
#         sys.stdin.flush()

#     return value