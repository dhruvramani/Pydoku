#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from read import read
from draw import draw
from solve import solve

import sys
from pprint import pprint


board = read()

# avoid overflowing C Stack
# TODO: make the other functions return a bool as to change or not, then call from here to avoid recursion
sys.setrecursionlimit(50000)

print("Solving...")
board = solve(board)

# TODO: track and print time taken
# TODO: check if we actually solved it or not
print("Solved! Here is the solution:")
draw(board)