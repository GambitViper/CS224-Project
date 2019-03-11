from game import Game
from bot import Bot

def game_loop(game, cpu = False) :
    bot = Bot(game)
    print(game) #.print_board()
    won = 0
    while game.turn < 27 and not won:
        if game.get_player_turn() == 1 or not cpu:
            move = map( int, raw_input("Player {} enter move [x] [y] [z] :".format(game.turn%2+1)).split(" "))
            move = game.make_move(move)
            while(not move) :
                move = map( int, raw_input("Player {} enter VALID move [x] [y] [z] :".format(game.turn%2+1)).split(" "))
                move = game.make_move(move)
        elif game.get_player_turn() == 2 and cpu:
            print "...bot taking turn"
            move = bot.dumb_bot_take_turn()
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
    game_loop(g, True)

if __name__ == "__main__":
    main()