import copy
from random import *
class Game:
    def __init__(self, s=3):
        self.size = s
        self.board = [[[0 for _ in range(self.size)] for _ in range(self.size)] for _ in range(self.size)]
        self.turn = 0

# overides print
    def __repr__(self):
        boardbuf = ""
        boardbuf += "Turn {}\n##########\n".format(self.turn)
        if len(self.board) != self.size:
            boardbuf += "Empty board - Please init_board\n"
        else:
            for level in self.board:
                for row in level:
                    boardbuf += str(row) + "\n"
                boardbuf += "##########\n"
        boardbuf += "\n"
        return boardbuf

# makes a move on board if possible or returns false
    def make_move(self, m):
        x, y, z = m[0], m[1], m[2]
        if self.board[x][y][z]:
            return False
        else:
            self.board[x][y][z] = self.turn % 2 + 1
            self.turn += 1
            return True

# returns the board - should maybe change to deep copy of board?
    def get_board(self):
        return self.board

# returns the player number for whose turn it is
    def get_player_turn(self):
        return self.turn % 2 + 1

# checks a board for wins
    def check_win(self):
        for i, grid in enumerate(self.board):
            won = self.check_grid(grid)
            if won:
                won = list(won)
                for cord in won[1]:
                    cord.insert(0, i)
                return won
        for i in range(self.size):
            grid = []
            for j in range(self.size):
                grid.append([self.board[j][k][i] for k in range(self.size)])
            # print(grid)
            won = self.check_grid(grid)
            if won:
                won = list(won)
                for cord in won[1]:
                    cord.append(i)
                return won
        for i in range(self.size) :
            grid = []
            for j in range(self.size):
                grid.append([self.board[j][i][k] for k in range(self.size)])
            won = self.check_diagonal(grid)
            if won:
                won = list(won)
                for cord in won[1]:
                    cord.insert(1,i)
                return won
        return self.check_mulit_diagonal()
        # TODO add check 3d horizontals

# checks a 2d grid for wins
    def check_grid(self, grid):
        checks = [self.check_verticle(grid), self.check_horizontal(grid), self.check_diagonal(grid)]
        for i in checks:
            if i:
                return i
        return 0

# checks a 2d grid for diagonal wins
    def check_diagonal(self, grid):
        line = [grid[i][i] for i in range(self.size)]
        won = self.check_line(line)
        if won:
            return won, [[i, i] for i in range(self.size)]
        line = [grid[(self.size - 1) - i][i] for i in range(self.size)]
        # print line
        won = self.check_line(line)
        if won:
            return won, [[self.size - 1 - i, i] for i in range(self.size)]
        return 0

# checks if any of the super diagonals contain wins
# TODO see if can remove lines
    def check_mulit_diagonal(self):
        lines = [[self.board[i][i][i] for i in range(self.size)],
                 [self.board[i][i][(self.size - 1) - i] for i in range(self.size)],
                 [self.board[i][(self.size - 1) - i][i] for i in range(self.size)],
                 [self.board[i][(self.size - 1) - i][(self.size - 1) - i] for i in range(self.size)]]
        cords = [[[i, i, i] for i in range(self.size)],
                 [[i, i, (self.size - 1) - i] for i in range(self.size)],
                 [[i, (self.size - 1) - i, i] for i in range(self.size)],
                 [[i, (self.size - 1) - i, (self.size - 1) - i] for i in range(self.size)]]
        for i, line in enumerate(lines):
            won = self.check_line(line)
            if won:
                return [won, cords[i]]
        return 0

# looks at a 2d grid and checks if columns contain wins
    def check_verticle(self, grid):
        for i in range(self.size):
            line = [grid[j][i] for j in range(len(grid))]  # double check
            won = self.check_line(line)
            if won:
                return won, [[j, i] for j in range(self.size)]
        return 0

# Looks at a 2d grid and checks if rows contain wins
    def check_horizontal(self, grid):
        for i in range(self.size):
            won = self.check_line(grid[i])
            if won:
                return won, [[i, j] for j in range(self.size)]
        return 0

# Checks to see if moves in a line are the same
    def check_line(self, line):
        temp = line[0]
        for i in line:
            if i != temp:
                return 0
        return temp
