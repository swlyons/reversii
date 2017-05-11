import time

from containers.ab_tree import ABTree

class HumanPlayer():
    def __init__(self, player_number=0):
        self.player_number = player_number
        self.initializing = True
        self.last_move = (0,0)

    def _validate_input(self, new_position):
        return self.board.valid_move(new_position, self.player_number, self.initializing)

    def _get_input(self):
        input = raw_input('where do you want to go: ')
        position = input.split(' ')
        return [int(a) for a in position]
    
#        if self._validate_input(position):
#            return [int(a) for a in position]
#        else:
#            return self._get_input()
    
    def do_turn(self, board, initializing=False):
        self.board = board
        self.initializing = initializing
        if not initializing and not board.can_move(self.player_number, initializing):
            return (board, False)
        # print()
        valid = False
        while not valid:
            input = board.print_board(last_move=self.last_move, player_number=self.player_number, initializing=initializing)
            valid = self._validate_input(input)
        self.last_move = input
        board.make_move(input, self.player_number)
        return(board, True)

class ComputerPlayer():
    def __init__(self, player_number=0, max_depth=6):
        self.max_depth = max_depth
        self.player_number = player_number

    def do_turn(self, board, initializing=False):
        if not board.can_move(self.player_number, initializing):
            return (board, False)
        if initializing:
            move = board.get_possible_sub_moves(self.player_number, True)[0]
            board.make_move(move, self.player_number)
            return(board, True)
        else:
            tree = ABTree(board, max_depth=self.max_depth)
            return(tree.get_optmal_move(self.player_number), True)