
board = []
turn = 0

def init_board() :
    global board
    board = [[[0 for _ in range(3)] for _ in range(3)] for _ in range(3)]

def print_board() :
    global board
    global turn
    print("Turn {}\n##########".format(turn))
    if len(board) != 3 :
        print("Empty board - Please init_board")
    else :
        for level in board :
            for row in level :
                print(row)
            print("##########")
    print("")

def make_move(m) :
    global board
    global turn
    x, y, z = m[0], m[1], m[2]
    if board[x][y][z] :
        return False
    else :
        board[x][y][z] = turn%2 + 1
        turn += 1
        return True

def get_player_turn() :
    global turn
    return turn%2 + 1

def main() :
    global turn
    init_board()
    print_board()
    while turn < 27 :
        move = map( int, raw_input("Player {} enter move [x] [y] [z] :".format(get_player_turn())).split(" "))
        print(move)
        move = make_move(move)
        while(not move) :
            move = map( int, raw_input("Player {} enter VALID move [x] [y] [z] :".format(get_player_turn())).split(" "))
            print(move)
            move = make_move(move)
        print_board()

if __name__ == "__main__" :
    main()
