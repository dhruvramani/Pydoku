#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
                            board = solve(board)

                # ... by column
                for y2 in range(9):
                    bit2 = board[y2][x]
                    if y2 != y:
                        if no in bit2:
                            bit2.remove(no)
                            assert len(bit2) > 0, \
                                "the number {} was repeated in column {}" \
                                    .format(no, x + 1)
                            board = solve(board)

                # ... by block
                # TODO: remove dupes by block
                pass

    return board

# a number has to appear somewhere...
def promote(board):
    # guard against aliasing
    board = deepcopy(board)

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
                        #print("Testing bit {}\n fo number {}".format(bit, no))
                        if no in bit:
                            coord = (x, y)
                            occurences.append(coord)

                # we found what we were looking for!
                assert len(occurences) > 0, "{} didn't occur in block at ({},{})".format(no, x_shift, y_shift)
                if len(occurences) == 1:
                    x, y = occurences[0]
                    board[y][x] = [no]
                    board = solve(board)

    # ... per line
    # TODO: promote lines and columns

    return board

# grand-daddy function to solve
# called by above functions on change
def solve(board):
    # guard against aliasing
    board = deepcopy(board)

    # delegate to helpers
    board = dedupe(board)
    board = blocks(board)

    # and finally...
    return board