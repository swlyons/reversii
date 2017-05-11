import curses

import numpy as np

class Board():
    def __init__(self, width=8, height=8, game=None):
        if game is None:
            self.game = np.zeros((width, height), dtype=np.int)
        else:
            self.game = game

    def get_size(self):
        return (len(self.game), len(self.game[0]))

    def can_move(self, player_number, initializing):
        return len(self.get_possible_sub_moves(player_number, initializing)) > 0

    def get_score(self):
        return np.sum(self.game)
    
    def get_possible_sub_games(self, player_number, initializing):
        
        possible_moves = self.get_possible_sub_moves(player_number, initializing)
        possible_games = []
        
        for eachMove in possible_moves:
            newboard = Board(len(self.game), len(self.game[0]), self.game)
            newboard.make_move(eachMove, player_number)
            possible_games.append(newboard)
        return possible_games
        


    def valid_move(self, move, player_number, initializing):        
        if move[0] < 0 or move[1] < 0 or move[0] >= len(self.game) or move[1] >= len(self.game[0]) or not self.game[move[0]][move[1]] == 0:
            return False

        if initializing:
            if not (move[0] == len(self.game)/2 or move[0] == len(self.game)/2 - 1):
                return False
            if not (move[1] == len(self.game[0])/2 or move[1] == len(self.game[0])/2 - 1):
                return False
            return True
        
        rowt = move[0]-1
        colt = move[1]
        while rowt >= 0 and not self.game[rowt][colt] == 0:
            if self.game[rowt][colt] == player_number:
                return True
            rowt=rowt-1
        
        rowt = move[0]+1
        colt = move[1]
        while rowt < len(self.game) and not self.game[rowt][colt] == 0:
            if self.game[rowt][colt] == player_number:
                return True
            rowt=rowt+1

        rowt = move[0]
        colt = move[1]-1
        while colt >= 0 and not self.game[rowt][colt] == 0:
            if self.game[rowt][colt] == player_number:
                return True
            colt=colt-1
        
        rowt = move[0]
        colt = move[1]+1
        while colt < len(self.game[0]) and not self.game[rowt][colt] == 0:
            if self.game[rowt][colt] == player_number:
                return True
            colt=colt+1
        
        
        rowt = move[0]-1
        colt = move[1]-1
        while rowt >= 0 and colt >= 0 and not self.game[rowt][colt] == 0:
            if self.game[rowt][colt] == player_number:
                return True
            rowt=rowt-1
            colt=colt-1
        
        rowt = move[0]+1
        colt = move[1]-1
        while colt >= 0 and rowt < len(self.game) and not self.game[rowt][colt] == 0:
            if self.game[rowt][colt] == player_number:
                return True
            rowt=rowt+1
            colt=colt-1

        rowt = move[0]-1
        colt = move[1]+1
        while rowt >= 0 and colt < len(self.game[0]) and not self.game[rowt][colt] == 0:
            if self.game[rowt][colt] == player_number:
                return True
            rowt=rowt-1
            colt=colt+1
        
        rowt = move[0]+1
        colt = move[1]+1
        while rowt < len(self.game) and colt < len(self.game[0]) and not self.game[rowt][colt] == 0:
            if self.game[rowt][colt] == player_number:
                return True
            rowt=rowt+1
            colt=colt+1
        
        return False
            

    def get_possible_sub_moves(self, player_number, initializing):
        possible_moves = []
        for row in range(self.get_size()[0]):
            for col in range(self.get_size()[1]):
                if self.valid_move((row, col), player_number, initializing):
                    possible_moves.append((row, col))
        # print possible_moves
        return possible_moves

    def make_move(self, move, player_number):
        self.game[move[0]][move[1]] = int(player_number)
        
        rowt = move[0]-1
        colt = move[1]
        while rowt >= 0 and not self.game[rowt][colt] == 0:
            if self.game[rowt][colt] == player_number:
                rowt=rowt+1
                while rowt < move[0]:
                    self.game[rowt][colt] = player_number
                    rowt=rowt+1
                break
            rowt=rowt-1
        
        rowt = move[0]+1
        colt = move[1]
        while rowt < len(self.game) and not self.game[rowt][colt] == 0:
            if self.game[rowt][colt] == player_number:
                rowt=rowt-1
                while rowt> move[0]:
                    self.game[rowt][colt] = player_number
                    rowt=rowt-1
                break
            rowt=rowt+1

        rowt = move[0]
        colt = move[1]-1
        while colt >= 0 and not self.game[rowt][colt] == 0:
            if self.game[rowt][colt] == player_number:
                colt = colt+1
                while colt<move[1]:
                    self.game[rowt][colt] = player_number
                    colt = colt+1
                break
            colt=colt-1
        
        rowt = move[0]
        colt = move[1]+1
        while colt < len(self.game[0]) and not self.game[rowt][colt] == 0:
            if self.game[rowt][colt] == player_number:
                colt = colt - 1
                while colt > move[1]:
                    self.game[rowt][colt] = player_number
                    colt = colt - 1
                break
            colt=colt+1
        
        
        rowt = move[0]-1
        colt = move[1]-1
        while rowt >= 0 and colt >= 0 and not self.game[rowt][colt] == 0:
            if self.game[rowt][colt] == player_number:
                rowt=rowt+1
                colt=colt+1
                while rowt < move[0]:
                    self.game[rowt][colt] = player_number
                    rowt=rowt+1
                    colt=colt+1
                break
            rowt=rowt-1
            colt=colt-1
        
        rowt = move[0]+1
        colt = move[1]-1
        while colt >= 0 and rowt < len(self.game) and not self.game[rowt][colt] == 0:
            if self.game[rowt][colt] == player_number:
                rowt = rowt-1
                colt = colt+1
                while move[0]<rowt:
                    self.game[rowt][colt] = player_number
                    rowt = rowt-1
                    colt = colt+1
                break
            rowt=rowt+1
            colt=colt-1

        rowt = move[0]-1
        colt = move[1]+1
        while rowt >= 0 and colt < len(self.game[0]) and not self.game[rowt][colt] == 0:
            if self.game[rowt][colt] == player_number:
                rowt=rowt+1
                colt=colt-1
                while rowt < move[0]:
                    self.game[rowt][colt] = player_number
                    rowt=rowt+1
                    colt=colt-1
                break
            rowt=rowt-1
            colt=colt+1
        
        rowt = move[0]+1
        colt = move[1]+1
        while rowt < len(self.game) and colt < len(self.game[0]) and not self.game[rowt][colt] == 0:
            if self.game[rowt][colt] == player_number:
                rowt = rowt - 1
                colt = colt - 1
                while rowt > move[0]:
                    self.game[rowt][colt] = player_number
                    rowt = rowt - 1
                    colt = colt - 1
                break
            rowt=rowt+1
            colt=colt+1

    def print_board(self, player_number=None, last_move=(1,1), initializing=False):
        def get_user_input(prompt='Invalid, try again'):
            y,x = last_move
            # curses.noecho()
            curses.noecho()
            stdscr.keypad(1)
            possible_moves = self.get_possible_sub_moves(player_number, initializing)
            while True:
                curses.flash()
                curses.setsyx((y + 1),(x + 1) * 2)
                curses.doupdate()
                c = stdscr.getch()
                if c == curses.KEY_LEFT:
                    x = max(x -1,0)
                elif c == curses.KEY_RIGHT:
                    x = min(x + 1, len(self.game) - 1)
                elif c == curses.KEY_UP:
                    y = max(y-1,0)
                elif c == curses.KEY_DOWN:
                    y = min(y+1, len(self.game[0])-1)
                elif c == curses.KEY_ENTER or c == 10 or c == 13:
                    return(y,x)


        def get_char(value):
            if value == 1:
                return 'w'
            elif value == -1:
                return 'b'
            else: 
                return '-'
        column_numbers = range(0, len(self.game[0]))
        stdscr = curses.initscr()
        
        stdscr.clear()
        stdscr.addstr(0, 0, '  {}'.format(' '.join([str(a) for a in column_numbers])))
        i = 0
        for index, row in enumerate(self.game):
            row_chars = [get_char(value) for value in row]
            stdscr.addstr(index + 1, 0, '{} {}'.format(i, ' '.join(row_chars)))
            i = i + 1
        if player_number is not None:
            stdscr.addstr(i + 1, 0, 'player {}\'s turn'.format(get_char(player_number)))
        stdscr.refresh()
        # stdscr.curs_set(1)
        input = get_user_input()
        if player_number is not None:
            stdscr.addstr(i + 1, 0, 'player {}\'s turn'.format(get_char(player_number * -1)))
        stdscr.refresh()
        return input 
        # print('  {}'.format(' '.join([str(a) for a in column_numbers])))
        # i = 0
        # for index, row in enumerate(self.game):
        #     row_chars = [get_char(value) for value in row]
        #     print('{} {}'.format(i, ' '.join(row_chars)))
        #     i = i + 1
        pass