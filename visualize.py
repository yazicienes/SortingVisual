import pygame
import sys
import random
import time

#constans
WIDTH = 800
HEIGHT = 600

num_bars = 10
bar_width = 20
space = 5
hor_offset = WIDTH/4


def drawBar(screen, x, height):
    pygame.draw.rect(screen, (0,0,0), (x, 400-height, bar_width, height), 0)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill((255, 255, 255))

    for i in range(num_bars):
        height = random.randint(10, 100)
        x = hor_offset + (i*bar_width) + (i*space)
        drawBar(screen, x, height)

    while (True):
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

main()
