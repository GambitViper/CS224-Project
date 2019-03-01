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

boardImg = pygame.image.load('gameboard.png')
board_width = 306
board_height = 478

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
    won = 0
    while g2d.turn < 27 and not won:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                click_pos = pygame.mouse.get_pos()
                print click_pos
                if player == 0:
                    playero.append(click_pos)
                    player = 1
                elif player == 1:
                    playerx.append(click_pos)
                    player = 0

        gameDisplay.fill((255,255,255))
        gameDisplay.blit(boardImg,((display_width - board_width)/4,0))

        for placeo in playero:
            pygame.draw.circle(gameDisplay, blue, placeo, 15, 2)

        for placex in playerx:
            draw_x(placex, 15)

        pygame.display.update()
        clock.tick(60)
            # move = map( int, raw_input("Player {} enter move [x] [y] [z] :".format(self.turn%2+1)).split(" "))
            # print(move)
            # move = g2d.make_move(move)
            # while(not move) :
            #     move = map( int, raw_input("Player {} enter VALID move [x] [y] [z] :".format(self.turn%2+1)).split(" "))
            #     move = g2d.make_move(move)
            # g2d.print_board()
            # won = g2d.check_win()
        # if won :
        #     print("Player {} Wins!!!".format(won))
        # else :
        #     print("Draw")

game_loop()
pygame.quit()
quit()