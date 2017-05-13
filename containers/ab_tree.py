

class ABNode:
    def __init__(self, board, root=False):
        self.board = board
        self.max_child = None
        self.root = root

    # def find_optimal_board(self, max_depth):
    #     if max_depth == self.depth and not self.visited:
    #         self.visited = True
    #         yield (self.board, self.board.get_score())
    #     else:
    #         if self.depth % 2 == 0:
    #             yield self.find_max_child(max_depth)
    #         else:
    #             yield self.find_min_child(max_depth)

    def find_max_score(self, alpha, beta, depth, player_number):
        # TODO: check for end of game
        new_depth = depth - 1
        if depth == 0:
            return self.board.get_score() * player_number
        else:
            v = float("-inf")
            _alpha = alpha
            sub_games = self.board.get_possible_sub_games(player_number, False)
            if len(sub_games) == 0:
                return ABNode(self.board).find_min_score(alpha, beta, new_depth, player_number * -1)
            for child_board in sub_games:
                v = max(v, ABNode(child_board).find_min_score(_alpha, beta, new_depth, player_number * -1))
                if _alpha <= v and self.root:
                    self.max_child = child_board
                _alpha = max(_alpha, v)
                if _alpha >= beta:
                    break
            return v


    def find_min_score(self, alpha, beta, depth, player_number):
        # TODO: check for end of game
        new_depth = depth - 1
        if depth == 0:
            return self.board.get_score() * player_number
        else:
            v = float("inf")
            _beta = beta
            sub_games = self.board.get_possible_sub_games(player_number, False)
            if len(sub_games) == 0:
                return ABNode(self.board).find_max_score(alpha, beta, new_depth, player_number * -1)
            for child_board in sub_games:
                v = min(v, ABNode(child_board).find_max_score(alpha, _beta, new_depth, player_number * -1))
                _beta = min(_beta, v)
                if alpha >= _beta:
                    break
            return v


class ABTree:
    def __init__(self, current_board, max_depth=6):
        self.root = ABNode(current_board, root=True)
        self.max_depth = max_depth

    def get_optmal_move(self, player_number):
        self.root.find_max_score(float('-inf'), float('inf'), self.max_depth, player_number)
        return self.root.max_child
        

