import pygame
import sys
import random
import time

#constans
WIDTH = 800
HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE =  (0, 0, 255)

num_bars = 10
bar_width = 20
space = 5
hor_offset = WIDTH/4

bars = []

def bubbleSort(screen, bars):
    n = len(bars)
    for i in range(n-1):
        for j in range(0, n-1-i):
            if bars[j] > bars[j+1]:
                bars[j], bars[j+1] = bars[j+1], bars[j]
                screen.fill(WHITE)
                for k in range(num_bars):
                    x = hor_offset + (k*bar_width) + (k*space)
                    drawBar(screen, x, bars[k])
                pygame.display.update()
                time.sleep(.2)

def drawBar(screen, x, height):
    pygame.draw.rect(screen, BLACK, (x, 400-height, bar_width, height), 0)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(WHITE)

    for i in range(num_bars):
        height = random.randint(10, 100)
        bars.insert(len(bars), height)
        x = hor_offset + (i*bar_width) + (i*space)
        drawBar(screen, x, height)
    pygame.display.update()
    bubbleSort(screen, bars)
    while (True):
        
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

main()
