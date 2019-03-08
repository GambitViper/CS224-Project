import pygame
import time
import random
import math
from game import Game

pygame.init()

display_width = 600
display_height = 500

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('3D-Tic-Tac-Toe.2')
clock = pygame.time.Clock()

boardImg = pygame.image.load('./images/gameboard.png')
board_width = 306
board_height = 478

boxes = {
  ((133,15),(185,60))   : (0,0,0), ((191,15),(257,60))   : (0,0,1), ((263,15),(331,60))   : (0,0,2),
  ((119,60),(183,106))  : (0,1,0), ((187,60),(263,106))  : (0,1,1), ((267,60),(347,106))  : (0,1,2),
  ((103,106),(178,150)) : (0,2,0), ((183,106),(268,150)) : (0,2,1), ((271,106),(361,150)) : (0,2,2),

  ((133,168),(187,213)) : (1,0,0), ((191,168),(257,213)) : (1,0,1), ((263,168),(331,213)) : (1,0,2),
  ((119,213),(183,260)) : (1,1,0), ((187,213),(263,260)) : (1,1,1), ((267,213),(347,260)) : (1,1,2),
  ((103,260),(179,305)) : (1,2,0), ((183,260),(267,305)) : (1,2,1), ((271,260),(361,305)) : (1,2,2),
  
  ((133,325),(187,368)) : (2,0,0), ((191,325),(257,368)) : (2,0,1), ((263,325),(331,368)) : (2,0,2),
  ((119,368),(183,415)) : (2,1,0), ((187,368),(263,415)) : (2,1,1), ((267,368),(347,415)) : (2,1,2),
  ((103,415),(179,460)) : (2,2,0), ((183,415),(267,460)) : (2,2,1), ((271,415),(361,460)) : (2,2,2)
}

def get_move_place(pos):
  x, y = pos[0], pos[1]
  for box in boxes:
    a, b = box[0][0], box[0][1]
    c, d = box[1][0], box[1][1]
    if x > a and x < c and y > b and y < d:
       return boxes.get(box)

def draw_x(pos, radius):
    line1_x1 = pos[0] - radius
    line1_y1 = pos[1] + radius
    line1_x2 = pos[0] + radius
    line1_y2 = pos[1] - radius

    line2_x1 = pos[0] - radius
    line2_y1 = pos[1] - radius
    line2_x2 = pos[0] + radius
    line2_y2 = pos[1] + radius

    pygame.draw.line(gameDisplay, red, (line1_x1,line1_y1), (line1_x2,line1_y2), 2)
    pygame.draw.line(gameDisplay, red, (line2_x1,line2_y1), (line2_x2, line2_y2), 2)

def game_loop():
    g2d = Game()

    playero = []
    playerx = []

    player = 0
    won = g2d.check_win()

    while g2d.turn < 27 and not won:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

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

        gameDisplay.fill((255,255,255))
        gameDisplay.blit(boardImg,((display_width - board_width)/4,0))

        for placeo in playero:
            pygame.draw.circle(gameDisplay, blue, placeo, 15, 2)

        for placex in playerx:
            draw_x(placex, 15)

        pygame.display.update()
        clock.tick(60)

        won = g2d.check_win()

    if won :
        print("Player {} Wins!!!".format(won))        
    else :
        print("Draw")

game_loop()