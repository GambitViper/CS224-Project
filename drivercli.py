from game import Game

def game_loop(game) :
        print(game) #.print_board()
        won = 0
        while game.turn < 27 and not won:
            move = map( int, raw_input("Player {} enter move [x] [y] [z] :".format(game.turn%2+1)).split(" "))
            # print(move)
            move = game.make_move(move)
            while(not move) :
                move = map( int, raw_input("Player {} enter VALID move [x] [y] [z] :".format(game.turn%2+1)).split(" "))
                move = game.make_move(move)
            print(game) #.print_board()
            won = game.check_win()
        if won and type(won) == list :
            print("Player {} Wins at {}!!!".format(won[0],won[1]))
        elif won :
            print(type(won))
            print("Player {} Wins!!!".format(won))
        else :
            print("Draw")

def main():
    g = Game()
    game_loop(g)

if __name__ == "__main__":
    main()