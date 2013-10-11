#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Main script to call that puts everything together'''

# imports
import sys, time
import arg_parse, read, display, solve

# initialize
print("Starting up Pydoku...")
start = time.clock()
duration = 0
done = False

# parse command-line arguments
args = arg_parse.get_parser().parse_args()                   # get and run parser
no_solve, pretty_print, board, file_ = arg_parse.init(args)  # init args

# read board
# if we were supplied a file, read it
if board:
    print("Reading from file '{}'...".format(board.name))
    board = read.read_file(board)
# else we have to get it from the user
else:
    print("Enter the known numbers (leaving spaces for those you don't know)...")
    now = time.clock()
    board = read.read_stdin()
    duration -= time.clock() - now

# solve board
if not no_solve:
    print("Solving... ", end='')
    board = solve.solve(board)

    # check if we're done
    if solve.done(board):
        done = True
        print("Solved!")
    # else resort to guessing
    else:
        now = time.clock()
        while True:
            response = input("\nBoard couldn't be solved by logic alone. Start guessing? [y/n] ") \
                .strip().lower()[0]
            if response == 'y':
                print("Guessing...", end='')
                start = time.clock()
                board = solve.guess(board)
                duration += time.clock() - start
                print("Guessed a correct solution!")
                break
            elif response == 'n':
                print("Will not try to guess and complete the board.")
                break
        duration -= time.clock() - now

# display board
if file_:
    print("Writing to file '{}'...".format(file_.name))
    display.write(board, file_, pretty_print, done)
else:
    print("Here is the solution:")
    display.draw(board, pretty_print, done)

# exit successfully!
duration += time.clock() - start
duration = round(duration, 1)
print('Execution complete in approximately {} seconds!'.format(duration))
sys.exit(0)