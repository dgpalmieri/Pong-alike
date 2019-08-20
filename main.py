# main.py
# Dylan Palmieri
# 9/16/19
# Pong-like game (or an attempt at it)

import sys
import pygame
import os
import block, paddle, wall, ball, scoreboard


UP      =  1
NEUTRAL =  0
DOWN    = -1


def playGame():
    pass


def main():
    pygame.init()

    current_path = os.path.dirname(__file__)
    images_path = os.path.join(current_path, "images/")

    size = width, height = 800, 600
    black = 0, 0, 0
    pygame.display.set_caption("Pong?")

    screen = pygame.display.set_mode(size)
    paddle = pygame.image.load(os.path.join(images_path, "paddle.png"))
    paddleRect = paddle.get_rect()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
#            elif event.type == pygame.K_DOWN:
#                if event.key == pygame.K_w:
#                    player.move = UP
#                elif event.key == pygame.K_s:
#                    player_move = DOWN
#                elif event.key == pygame.K_w and event.key == pygame.K_s:
#                    player_move = NEUTRAL
#                elif event.key == pygame.K_w:
#                    player_move = UP
#                elif event.key == pygame.K_s:
#                    player_move = DOWN
#                elif event.key == pygame.K_w and event.key == pygame.K_s:
#                    player_move = NEUTRAL

        playGame()
        screen.fill(black)
        screen.blit(paddle, paddleRect)
        pygame.display.flip()


if __name__ == "__main__":
    main()
