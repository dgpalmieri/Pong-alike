# main.py
# Dylan Palmieri
# 9/16/19
# Pong-like game (or an attempt at it)

import sys
import pygame
import block, ball, scoreboard


UP      =  1
NEUTRAL =  0
DOWN    = -1


def playGame():
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        movePaddles()
        moveBall()
        updateDisplay()


def startScreen():

    while True:
        # display splash screen

        movePaddles()
        updateDisplay()
        # if spacebar is pressed
        break


def movePaddles():
    pass
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


def moveBall():
    pass


def updateDisplay():

    size = width, height = 800, 600
    black = 0, 0, 0
    pygame.display.set_caption("Pong?")

    screen = pygame.display.set_mode(size)

    screen.fill(black)
    pygame.display.flip()


def main():
    pygame.init()

    startScreen()
    playGame()


if __name__ == "__main__":
    main()
