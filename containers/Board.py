
import numpy as np

class Board():
    def __init__(self, width=8, height=8, game=None):
        if game is None:
            self.game = np.zeros((width, height))
        else:
            self.game = game

    def get_size(self):
        return (len(self.game), len(self.game[0]))

    def can_move(self, player_number):
        return True

    def get_score(self):
        pass

    def get_possible_sub_games(self):
        pass

    def _valid_move(self, move, player_number):
        if self.game[move[0]][move[1]] is not 0:
            return False
        


    def get_possible_sub_moves(self, player_number):
        possible_moves = []
        for row in range(self.get_size()[0]):
            for col in range(self.get_size()[1]):
                if self._valid_move((row, col), player_number):
                    possible_moves.append((row, col))
        return possible_moves

    def make_move(self, position, player_number):
        print (self.game)
        self.game[position[0]][position[1]] = int(player_number)
        print('finish')

    def print_board(self):
        def get_char(value):
            if value == 1:
                return 'w'
            elif value == -1:
                return 'b'
            else: 
                return '-'
        column_numbers = range(0, len(self.game[0]))
        print(self.game)
        print('  {}'.format(' '.join([str(a) for a in column_numbers])))
        i = 0
        for row in self.game:
            row_chars = [get_char(value) for value in row]
            print('{} {}'.format(i, ' '.join(row_chars)))
            i = i + 1
        pass