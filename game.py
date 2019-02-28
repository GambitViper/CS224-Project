class Game :
    def __init__(self) :
        self.board = [[[0 for _ in range(3)] for _ in range(3)] for _ in range(3)]
        self.turn = 0
# __repr__ TODO look up
    def print_board(self) :
        print("Turn {}\n##########".format(self.turn))
        if len(self.board) != 3 :
            print("Empty board - Please init_board")
        else :
            for level in self.board :
                for row in level :
                    print(row)
                print("##########")
        print("")

    def make_move(self, m) :
        x, y, z = m[0], m[1], m[2]
        if self.board[x][y][z] :
            return False
        else :
            self.board[x][y][z] = self.turn%2 + 1
            self.turn += 1
            return True

    def get_player_turn(self) :
        return self.turn%2 + 1

    def game_loop(self) :
        won = 0
        while self.turn < 27 and not won:
            move = map( int, raw_input("Player {} enter move [x] [y] [z] :".format(self.turn)).split(" "))
            print(move)
            move = self.make_move(move)
            while(not move) :
                move = map( int, raw_input("Player {} enter VALID move [x] [y] [z] :".format(self.turn+1)).split(" "))
                move = self.make_move(move)
            self.print_board()
            won = self.check_win()

    def check_win(self) :
        for grid in self.board :
            won = self.check_grid(grid)
            if won :
                return won
        return 0
        # TODO add check extream diagonals

    def check_grid(self, grid) :
        f = [self.check_verticle(grid), self.check_horizontal(grid), self.check_diagonal(grid)]
        for i in f :
            if i :
                return i
        return 0

    def check_diagonal(self, grid) :
        line = [grid[i][i] for i in range(len(grid))]
        won = self.check_line(line)
        if won :
            return won
        line = [grid[2-i][i] for i in range(len(grid))] # I don't think this works
        print line
        won = self.check_line(line)
        if won :
            return won
        return 0

    def check_verticle(self, grid) :
        for i in range(len(grid[0])) :
            line = [grid[j][i] for j in range(len(grid))] #double check
            won = self.check_line(line)
            if won :
                return won
        return 0;

    def check_horizontal(self, grid) :
        for row in grid :
            won = self.check_line(row)
            if won :
                return won
        return 0

    def check_line(self, line) :
        temp = line[0]
        for i in line  :
            if i != temp :
                return 0
        return temp

g = Game()

g.game_loop()
