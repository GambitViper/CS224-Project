import copy
from random import *
from game import Game


# Bot instance takes the instance of the Game instance to infer its turn
class Bot:
    def __init__(self, game):
        self.board = game.get_board()
        self.game = game

    # function for dumb bot to take it's turn, returns a list of the three indexes that are the location it will put
    # its piece. Code assumes bot is always O (2 in the game board)
    def dumb_bot_take_turn(self):
        # get list of all empty spaces
        free_spaces = [[l, r, c] for l in range(len(self.board)) for r in range(len(self.board[l])) for c in range(
            len(self.board[l][r])) if self.board[l][r][c] == 0]
        # for each space in free_spaces check if a move results in a win for bot, if it does make that move.
        for m in free_spaces:
            fake_board = copy.deepcopy(self.game)
            fake_board.board[m[0]][m[1]][m[2]] = 2
            if fake_board.check_win():
                return m
        # for each space in free_spaces check if a move results in a win for player, if it does block that move
        for m in free_spaces:
            fake_board = copy.deepcopy(self.game)
            fake_board.board[m[0]][m[1]][m[2]] = 1
            if fake_board.check_win():
                return m
        # there is no wining move for the bot or player, so take a random move from free_spaces
        return free_spaces[randint(0, len(free_spaces)-1)]
