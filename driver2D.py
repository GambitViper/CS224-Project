import pygame
import time
import random
import math
from game import Game
from bot import Bot

# Setup function for instantiating a pygame instance
pygame.init()

# Sets the global 
display_width = 600
display_height = 500

# Setup for pre-defined colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Window setup code
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('3D-Tic-Tac-Toe.2')
clock = pygame.time.Clock()

# Image load and image dimensions
boardImg = pygame.image.load('./images/gameboard.png')
board_width = 306
board_height = 478

# Current dictionary hard-coded lookup for comparing mouse pointer values to positions in the array of the game
boxes = {
    ((133, 15), (185, 60)): (0, 0, 0), ((191, 15), (257, 60)): (0, 0, 1), ((263, 15), (331, 60)): (0, 0, 2),
    ((119, 60), (183, 106)): (0, 1, 0), ((187, 60), (263, 106)): (0, 1, 1), ((267, 60), (347, 106)): (0, 1, 2),
    ((103, 106), (178, 150)): (0, 2, 0), ((183, 106), (268, 150)): (0, 2, 1), ((271, 106), (361, 150)): (0, 2, 2),

    ((133, 168), (187, 213)): (1, 0, 0), ((191, 168), (257, 213)): (1, 0, 1), ((263, 168), (331, 213)): (1, 0, 2),
    ((119, 213), (183, 260)): (1, 1, 0), ((187, 213), (263, 260)): (1, 1, 1), ((267, 213), (347, 260)): (1, 1, 2),
    ((103, 260), (179, 305)): (1, 2, 0), ((183, 260), (267, 305)): (1, 2, 1), ((271, 260), (361, 305)): (1, 2, 2),

    ((133, 325), (187, 368)): (2, 0, 0), ((191, 325), (257, 368)): (2, 0, 1), ((263, 325), (331, 368)): (2, 0, 2),
    ((119, 368), (183, 415)): (2, 1, 0), ((187, 368), (263, 415)): (2, 1, 1), ((267, 368), (347, 415)): (2, 1, 2),
    ((103, 415), (179, 460)): (2, 2, 0), ((183, 415), (267, 460)): (2, 2, 1), ((271, 415), (361, 460)): (2, 2, 2)
}

# Hackey fix to a slight problem with the turn counting display
# TODO remove later
def flipTurn(turn):
    if turn == 1:
        return 2
    else:
        return 1

# Draws the box and displays current symbol for turn
def turn_converter(turn, parent_pos, cpu):
    pos1 = parent_pos[0] + 60
    pos2 = parent_pos[1] - 12
    pos = (pos1, pos2)
    pygame.draw.rect(gameDisplay, black, [pos1, pos2, 50, 50], 2)
    pos = (pos[0] + 25, pos[1] + 25)
    if cpu:
        turn = flipTurn(turn)
    if turn == 1:
        draw_x(pos, 15)
    if turn == 2:
        pygame.draw.circle(gameDisplay, blue, pos, 15, 2)

# Displays the turn for each player in the upper right corner
def turn_counter(turn, pos, cpu):
    font = pygame.font.SysFont(None, 35)
    text = font.render("Turn  ", True, black)
    turn_display = turn_converter(turn, pos, cpu)
    gameDisplay.blit(text, pos)

# Compares against the bounding boxes array to return the value lookup as a position in the game array
def get_move_place(pos):
    x, y = pos[0], pos[1]
    for box in boxes:
        a, b = box[0][0], box[0][1]
        c, d = box[1][0], box[1][1]
        if x > a and x < c and y > b and y < d:
            return boxes.get(box)

# Function returns the midpoint between two points
def midpoint(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

# Compares bot board move to box positions and returns a centered x,y position coordinate
def get_bot_move_pos(move):
    invertboxes = {v: k for k, v in boxes.items()}
    for ibox in invertboxes:
        if list(ibox) == move:
            val = invertboxes.get(ibox)
            print("Bot pos found: {} <- {}".format(val, move))
            return midpoint(val[0], val[1])

# Function used to programmatically draw an 'X' on the board
def draw_x(pos, radius):
    line1_x1 = pos[0] - radius
    line1_y1 = pos[1] + radius
    line1_x2 = pos[0] + radius
    line1_y2 = pos[1] - radius

    line2_x1 = pos[0] - radius
    line2_y1 = pos[1] - radius
    line2_x2 = pos[0] + radius
    line2_y2 = pos[1] + radius

    pygame.draw.line(gameDisplay, red, (line1_x1, line1_y1), (line1_x2, line1_y2), 2)
    pygame.draw.line(gameDisplay, red, (line2_x1, line2_y1), (line2_x2, line2_y2), 2)

# Function to draw all the 'O's on the game board
def drawOs(positions):
    for pos in positions:
        pygame.draw.circle(gameDisplay, blue, pos, 15, 2)

# Function to draw all the 'X's on the game board
def drawXs(positions):
    for pos in positions:
        draw_x(pos, 15)

# Game loop performs all the game logic and redrawing of the board during every clock tick
def game_loop(game, cpu = False):
    # Setup board variables for position array of 'O's and position array of 'X's to display symbols on the board
    g2d = game
    if cpu:
        bot = Bot(g2d)

    print("CPU val: {}".format(cpu))

    playero = []
    playerx = []

    # Starts the game logic by instantiating won to False
    won = g2d.check_win()

    # Main loop stops either if someone wins or if the maximum turns is exceeded
    while g2d.turn < 27 and not won:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if cpu and g2d.get_player_turn() == 2:
                print("Bot turn")
                move = bot.dumb_bot_take_turn()
                move_pos = get_bot_move_pos(move)
                move = game.make_move(move)
                playerx.append(move_pos)
            elif cpu and g2d.get_player_turn() == 1:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click_pos = pygame.mouse.get_pos()
                    move = get_move_place(click_pos)
                    print("pos: {0} -> move: {1}".format(click_pos, move))
                    if move is not None:
                        if g2d.make_move(move):
                            playero.append(click_pos)
            else:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click_pos = pygame.mouse.get_pos()
                    move = get_move_place(click_pos)
                    print("pos: {0} -> move: {1}".format(click_pos, move))
                    if move is not None:
                        if g2d.make_move(move):
                            if g2d.get_player_turn() == 1:
                                playero.append(click_pos)
                            elif g2d.get_player_turn() == 2:
                                playerx.append(click_pos)

        # Wipes the game board and fills white
        gameDisplay.fill((255, 255, 255))

        # Displays currently the board represented as a background image
        gameDisplay.blit(boardImg, ((display_width - board_width) / 4, 0))

        # Calls the draw functions for each the 'O's and the 'X's
        drawOs(playero)
        drawXs(playerx)

        # Calls the function to display the turn counter and the current turn
        turn_counter(g2d.get_player_turn(), (display_width - 125, 25), cpu)
        
        # Updates the window display based on the pre-loaded rendering above and updates the clock tick
        pygame.display.update()
        clock.tick(60)

        # Updates the boolean tracking if a player / agent has won the game yet
        won = g2d.check_win()

    if won:
        print("Player {} Wins!!!".format(won))
    else:
        print("Draw")

def main():
    game = Game()
    game_loop(game, True)

if __name__ == "__main__":
    main()
