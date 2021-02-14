import pygame
import sys
import random
import time

#constans
WIDTH = 800
HEIGHT = 600

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    screen.fill((255, 255, 255))
    pygame.display.update()
    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

main()
