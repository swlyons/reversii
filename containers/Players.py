import time

from containers.ab_tree import ABTree

class HumanPlayer():
    def __init__(self, player_number=0):
        self.player_number = player_number
        self.initializing = True
        self.last_move = (0,0)

    def _validate_input(self, new_position):
        valid = False
        x,y = new_position
        if(not self.board.game[x][y] == 0):
            return False
        if self.initializing:
            x, y = new_position
            game_x, game_y = self.board.get_size()
            if (x==game_x/2 or x==game_x/2 - 1) and (y==game_y/2 or y==game_y/2 - 1):
                valid = True
            return valid
        
        elif self.board._valid_move((x,y), self.player_number):
            valid = True
    
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
        # print()
        valid = False
        while not valid:
            input = board.print_board(last_move=self.last_move, player_number=self.player_number)
            valid = self._validate_input(input)
        self.last_move = input
        board.make_move(input, self.player_number)
        return(board, True)

class ComputerPlayer():
    def __init__(self, player_number=0, max_depth=6):
        self.max_depth = max_depth
        self.player_number = player_number

    def do_turn(self, board, initializing=False):
        if not board.can_move(self.player_number):
            return (board, False)
        tree = ABTree(board, max_depth=self.max_depth)
        return(tree.get_optmal_move(self.player_number), True)