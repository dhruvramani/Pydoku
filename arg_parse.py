#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Parses (if necessary) command-line arguments'''

import argparse

# create parser object
def get_parser():

    # construct `parser`
    parser = argparse.ArgumentParser(
        prog='pydoku.py',
        formatter_class=argparse.RawTextHelpFormatter,
        description="""A simple Python Package that solves a Sudoku via the command line;""",
        epilog="For more help and details, check out the `README.md` file")

    # positional args
    #action_group = parser.add_mutually_exclusive_group()
    #action_group.add_argument('-s', '--solve', help="solve the board")
    #action_group.add_argument('-r', '--read',  help="just read the board and save it")
    #action_group.add_argument('-d', '--display', help="just display the board given")
    #parser.add_argument('action', choices=ACTIONS,
    #    help="if `read`, then just read the board an save it;\n"
    #         "if `display`, then just display the given board;\n"
    #         "if `solve`, read the board, solve it and then display it!")

    # optional flags
    parser.add_argument('-n', '--nosolve', action='store_true',
        help="don't solve the board, only read and display it")

    # optional args
    parser.add_argument('-b', '--board', type=argparse.FileType('r'),
        help="read board from file `BOARD` (or, if absent, obtain board interactively from stdin)")
    parser.add_argument('-f', '--file', type=argparse.FileType('w'),
        help="save the solved (or, if using the `-d` option, the just inputted) board to `FILE`")

    # mutually exclusive groups
    print_style = parser.add_mutually_exclusive_group()
    parser.set_defaults(pretty_print=True)
    print_style.add_argument('-p', '--prettyprint', action='store_const', dest='pretty_print', const=True,
        help="display the board formatted using box characters")
    print_style.add_argument('-P', '--normalprint', action='store_const', dest='pretty_print', const=False,
         help="display the board as just a newline-separated row of numbers")

    # return constructed `parser`
    return parser

# init vars from parsed arguments
def init(args):
    no_solve     = args.nosolve
    pretty_print = args.pretty_print
    board        = args.board or None
    file         = args.file or None

    return no_solve, pretty_print, board, file

