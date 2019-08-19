# main.py
# Dylan Palmieri
# 9/16/19
# Pong-like game (or an attempt at it)

import sys
import pygame
import os

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

    screen.fill(black)
    screen.blit(paddle, paddleRect)
    pygame.display.flip()
