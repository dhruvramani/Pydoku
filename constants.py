#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Just contains some miscellanous constants'''

BLANK_CELL = (1, 2, 3, 4, 5, 6, 7, 8, 9)

BLANK_BOARD = [ [ list(BLANK_CELL)
        for i in range(9) ]
        for j in range(9) ]

SMALL_TEMPLATE = """\
╔═══╦═══╦═══╗
║   ║   ║   ║
║   ║   ║   ║
║   ║   ║   ║
╠═══╬═══╬═══╣
║   ║   ║   ║
║   ║   ║   ║
║   ║   ║   ║
╠═══╬═══╬═══╣
║   ║   ║   ║
║   ║   ║   ║
║   ║   ║   ║
╚═══╩═══╩═══╝"""

BIG_TEMPLATE = """
┏━━━┯━━━┯━━━┳━━━┯━━━┯━━━┳━━━┯━━━┯━━━┓
┃   │   │   ┃   │   │   ┃   │   │   ┃
┃   │   │   ┃   │   │   ┃   │   │   ┃
┃   │   │   ┃   │   │   ┃   │   │   ┃
┠───┼───┼───╂───┼───┼───╂───┼───┼───┨
┃   │   │   ┃   │   │   ┃   │   │   ┃
┃   │   │   ┃   │   │   ┃   │   │   ┃
┃   │   │   ┃   │   │   ┃   │   │   ┃
┠───┼───┼───╂───┼───┼───╂───┼───┼───┨
┃   │   │   ┃   │   │   ┃   │   │   ┃
┃   │   │   ┃   │   │   ┃   │   │   ┃
┃   │   │   ┃   │   │   ┃   │   │   ┃
┣━━━┿━━━┿━━━╋━━━┿━━━┿━━━╋━━━┿━━━┿━━━┫
┃   │   │   ┃   │   │   ┃   │   │   ┃
┃   │   │   ┃   │   │   ┃   │   │   ┃
┃   │   │   ┃   │   │   ┃   │   │   ┃
┠───┼───┼───╂───┼───┼───╂───┼───┼───┨
┃   │   │   ┃   │   │   ┃   │   │   ┃
┃   │   │   ┃   │   │   ┃   │   │   ┃
┃   │   │   ┃   │   │   ┃   │   │   ┃
┠───┼───┼───╂───┼───┼───╂───┼───┼───┨
┃   │   │   ┃   │   │   ┃   │   │   ┃
┃   │   │   ┃   │   │   ┃   │   │   ┃
┃   │   │   ┃   │   │   ┃   │   │   ┃
┣━━━┿━━━┿━━━╋━━━┿━━━┿━━━╋━━━┿━━━┿━━━┫
┃   │   │   ┃   │   │   ┃   │   │   ┃
┃   │   │   ┃   │   │   ┃   │   │   ┃
┃   │   │   ┃   │   │   ┃   │   │   ┃
┠───┼───┼───╂───┼───┼───╂───┼───┼───┨
┃   │   │   ┃   │   │   ┃   │   │   ┃
┃   │   │   ┃   │   │   ┃   │   │   ┃
┃   │   │   ┃   │   │   ┃   │   │   ┃
┠───┼───┼───╂───┼───┼───╂───┼───┼───┨
┃   │   │   ┃   │   │   ┃   │   │   ┃
┃   │   │   ┃   │   │   ┃   │   │   ┃
┃   │   │   ┃   │   │   ┃   │   │   ┃
┗━━━┷━━━┷━━━┻━━━┷━━━┷━━━┻━━━┷━━━┷━━━┛\
""".replace('   ', '{}')
