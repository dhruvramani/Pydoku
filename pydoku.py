#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Main script to call that puts everything together'''

# imports
import sys
import arg_parse, read, display, solve

# parse command-line arguments
args = arg_parse.get_parser().parse_args()                   # get and run parser
no_solve, pretty_print, board, file_ = arg_parse.init(args)  # init args

# read board
# if we were supplied a file, read it
if board:
    print("Enter the known numbers (leaving spaces for those you don't know)...")
    board = read.read_file(board)
# else we have to get it from the user
else:
    print("Reading from file {}".format(file_.name))
    board = read.read_stdin()

# solve board
if not no_solve:
    print("Solving...")
    board = solve.solve(board)
# check if we're done
if solve.done(board):
    print("Solved! ", end='')
# else resort to guessing
else:
    while True:
        response = input("Board couldn't be solved by logic alone. Start guessing? [y/n]").strip().lower()[0]
        if response == 'y':
            print("Guessing...")
            board, unique = solve.guess()
            print("Guessed a correct solution!")
            break
        elif response == 'n':
            print("Will not try to guess and complete the board.")
            break

# display board
if file_:
    print("Writing to file '{}'...".format(file_.name))
    display.write(board, file_, pretty_print)
else:
    print("Here is the solution:")
    display.draw(board, pretty_print)

# exited successfully !
sys.exit(0)