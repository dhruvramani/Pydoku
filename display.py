#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''The 'O' in 'I/O' (pretty prints the solved board)'''

from constants import BIG_TEMPLATE


# get board into shape #######################################################

def _organize(board):
    format = []
    for row in board:
        for x in range(3):
            for bit in row:
                line = ''.join( map(str, bit[x]) )
                format.append(line)
    return format

def _expand(old_board):
    new_board = []

    for old_row in old_board:
        new_row = []

        for old_bit in old_row:

            new_bit = [' ' for i in range(9)]
            for no in old_bit:
                new_bit[no - 1] = no
            new_bit = [new_bit[3*i:3*i+3] for i in range(3)]

            new_row.append(new_bit)

        new_board.append(new_row)

    return new_board


# choose correct representation ##############################################

def _pretty_print(board):
    expanded  = _expand(board)
    formatted = _organize(expanded)

    string = BIG_TEMPLATE.format(*formatted)

    return string

def _normal_print(board):
    return '\n'.join(''.join(row) for row in board)

def _print(board, pretty_print):
    if pretty_print:
        return _pretty_print(board)
    else:
        return _normal_print(board)


# integrate everything #######################################################

def draw(board, pretty_print):
    print(_print(board))

def write(board, file_, pretty_print):
    with file_:
        file_.write(_print(board))
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
