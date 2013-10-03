#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Functions for solving the board'''

from copy import deepcopy

# a number can appear only once
def dedupe(board):
    # guard against aliasing
    board = deepcopy(board)

    # loop over all the bits
    for y, row in enumerate(board):
        for x, bit in enumerate(row):

            # remove dupe number possibilities...
            if len(bit) == 1:
                no = bit[0]

                # ... by row
                for x2, bit2 in enumerate(board[y]):
                    if x2 != x:
                        if no in bit2:
                            bit2.remove(no)
                            assert len(bit2) > 0, \
                                "the number {} was repeated in row {}" \
                                    .format(no, y + 1)

                # ... by column
                for y2 in range(9):
                    if y2 != y:
                        bit2 = board[y2][x]
                        if no in bit2:
                            bit2.remove(no)
                            assert len(bit2) > 0, \
                                "the number {} was repeated in column {}" \
                                    .format(no, x + 1)

                # ... by block
                y2_shift = (y // 3) * 3
                x2_shift = (x // 3) * 3
                for y2 in range(y2_shift, y2_shift+3):
                    for x2 in range(x2_shift, x2_shift+3):
                        if (x2, y2) != (x, y):
                            bit2 = board[y2][x2]
                            if no in bit2:
                                bit2.remove(no)
                                assert len(bit2) > 0, \
                                    "the number {} was repeated in block {} or row {}" \
                                        .format(no, x2_shift/3, y2_shift/3)

    return board

# a number has to appear somewhere...
def promote(board):
    # guard against aliasing
    board = deepcopy(board)

    # ... per row
    for y, row in enumerate(board):

        # loop over numbers to test for
        for no in range(1, 10):

            # track co-ords where no appears
            occurences = []

            # loop over bits
            for x, bit in enumerate(row):

                    # can it be the number?
                    if no in bit:
                        coord = (x, y)
                        occurences.append(coord)

            # we found what we were looking for!
            assert len(occurences) > 0, \
                "the number {} didn't occur in row {}".format(no, y+1)
            if len(occurences) == 1:
                x, y = occurences[0]
                board[y][x] = [no]

    # ... per column
    for x in range(9):

        # loop over numbers to test for
        for no in range(1, 10):

            # track co-ords where no appears
            occurences = []

            # loop over bits
            for y in range(9):
                bit = board[y][x]

                # can it be the number?
                if no in bit:
                    coord = (x, y)
                    occurences.append(coord)

            # we found what we were looking for!
            assert len(occurences) > 0, \
                "the number {} didn't occur in column {}".format(no, x+1)
            if len(occurences) == 1:
                x, y = occurences[0]
                board[y][x] = [no]

    # ... per block
    for y_mul in range(3):
        y_shift = y_mul * 3

        for x_mul in range(3):
            x_shift = x_mul * 3

            # loop over numbers to test for
            for no in range(1, 10):

                # track co-ords where no appears
                occurences = []

                # loop over bits
                for y_pos in range(3):
                    for x_pos in range(3):

                        # calculate bit
                        y = y_pos + y_shift
                        x = x_pos + x_shift
                        bit = board[y][x]

                        # can it be the number?
                        if no in bit:
                            coord = (x, y)
                            occurences.append(coord)

                # we found what we were looking for!
                assert len(occurences) > 0, \
                    "the number {} didn't occur in block {} of row {}".format(no, x_shift/3, y_shift/3)
                if len(occurences) == 1:
                    x, y = occurences[0]
                    board[y][x] = [no]

    return board

# grand-daddy function to solve
def solve(board):
    # guard against aliasing
    board = deepcopy(board)
    original = None

    # repeat until we can't figure out anything more
    while board != original:
        # recalculate original
        original = deepcopy(board)

        # delegate solving to helpers
        board = dedupe(board)
        board = promote(board)

    # and finally...
    return board