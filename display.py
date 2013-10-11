#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''The 'O' in 'I/O' (pretty prints the solved board)'''

from constants import SMALL_TEMPLATE, BIG_TEMPLATE


# pretty print helpers #######################################################

# add strings for every number per cell
def _expand(old_board, done):
    new_board = []

    # loop over rows and bits
    for old_row in old_board:
        new_row = []
        for old_bit in old_row:

            # if we're done, either the number or nothing
            if done:
                if len(old_bit) == 1:
                    new_bit = str(old_bit[0])
                else:
                    new_bit = ' '

            # else, add possibilities for unsolved numbers also
            else:
                new_bit = [' ' for i in range(9)]                 # assume all numbers impossible
                for no in old_bit:                                # go over possible numbers
                    new_bit[no - 1] = str(no)                     # replace space with number at index
                new_bit = [new_bit[3*i:3*i+3] for i in range(3)]  # split into 3 equal segments

            new_row.append(new_bit)

        new_board.append(new_row)

    return new_board

# map cells to template
def _organize(old_board, done):
    new_board = []

    for row in old_board:
        for x in range(3):

            # if we're done, map to small template
            if done:
                line = ''.join(row[3*x : 3*x+3])
                new_board.append(line)

            # else, map to big template
            else:
                for bit in row:
                    line = ''.join(bit[x])
                    new_board.append(line)

    return new_board

# format template with cells
def _map(board, done):
    template = SMALL_TEMPLATE if done else BIG_TEMPLATE
    template = template.replace('   ', '{}')
    return template.format(*board)


# print helpers ##############################################################
def _pretty_print(board, done):
    expanded  = _expand(board, done)
    formatted = _organize(expanded, done)
    mapped = _map(formatted, done)

    return mapped

def _normal_print(board):
    return '\n'.join(
        ''.join(
            str(bit[0]) if len(bit) == 1 else ' ' for bit in row
        ) for row in board
    )

def _print(board, pretty_print, done):
    if pretty_print:
        return _pretty_print(board, done)
    else:
        return _normal_print(board)


# main functions #############################################################

def draw(board, pretty_print, done):
    print(_print(board, pretty_print, done))

def write(board, file_, pretty_print, done):
    with file_:
        file_.write(_print(board, pretty_print, done))
        file_.write('\n')

# def prettyPrint(board, reverse=False):
#     def complement(old):
#         assert hasattr(old, '__iter__'), "`bit` arg should be an iter"
#         new = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#         for no in old:
#             new.remove(no)
#         return new
#
#     for row in board:
#         for bit in row:
#                 if type(bit) == int:
#                     s = '{:^10}'.format('*' + str(bit) + '*')
#                 else:
#                     if reverse:
#                         bit = complement(bit)
#                     n = ''.join( map(str, bit) )
#                     s = '{:<10}'.format(n)
#                 print(s, end='')
#         print()