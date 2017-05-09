# from __future__ import print_function

import sys, os, time, curses

import numpy as np

from containers.Board import Board
from containers.Players import HumanPlayer, ComputerPlayer
# stdscr = curses.initscr()
# for x in range(0,3):
#     # print(x, end='')  # No need for sep here, but okay :)
#     # sys.stdout.write('000\r010\r000\r')
#     # sys.stdout.flush()
#     stdscr.addstr(0, 0, "hello {}".format(x))
#     stdscr.addstr(1, 0, "hello {}".format(x))
#     stdscr.refresh()
#     time.sleep(1)
gameOver = False

players = []
players.append(HumanPlayer(player_number=-1))
players.append(HumanPlayer(player_number=1))
turn_number = 0
board = Board()


while not gameOver:
    gameOver = True
    #player 1's turn
    board, changed = players[0].do_turn(board, initializing=turn_number<4)
    turn_number+=1
    if changed:
        gameOver = False


    #player 2's turn
    board, changed = players[1].do_turn(board, initializing=turn_number<4)
    turn_number+=1
    if changed:
        gameOver = False
    
if board.get_score() < 0:
    print 'Player 1 (black) wins!'

elif board.get_score() > 0:
    print 'Player 2 (white) wins!'

else:
    print 'TIE GAME!'
    
# players = [HumanPlayer(), ComputerPlayer()]

# turn = 0
# while True:
#     players[turn % 2].get_turn()
#     turn = turn + 1
#     if end_of_game():
#         break
# do stuff