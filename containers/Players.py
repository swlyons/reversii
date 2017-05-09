class HumanPlayer():
    def __init__(self, player_number=0):
        self.player_number = player_number
        self.initializing = True

    def _validate_input(self, new_position):
        valid = False
        if(not board.game[x][y] == 0):
            return False
        if self.initializing:
            x, y = new_position
            game_x, game_y = self.board.get_size()
            if (x==game_x/2 or x==game_x/2 + 1) and (y==game_y/2 or y==game_y/2):
                valid = True
            return valid
        
        if (x, y) is not in board.get_possible_sub_moves(self.player_number):
            valid = False
        
        return valid

    def _get_input(self):
        input = raw_input('where do you want to go: ')
        position = input.split(' ')
        if self._validate_input(position):
            return [int(a) for a in position]
        else:
            return self._get_input()
    
    def do_turn(self, board, initializing=False):
        self.board = board
        self.initializing = initializing
        if not board.can_move(self.player_number):
            return (board, False)
        board.print_board()
        input = self._get_input()
        board.make_move(input, self.player_number)
        return(board, True)

class ComputerPlayer():
    def __init__(self):
        pass

    def do_turn(self, board, initializing=False):
        pass