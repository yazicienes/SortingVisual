import pygame
import sys
import random
import time

#constans
WIDTH = 800
HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE =  (66, 135, 245)

num_bars = 15
bar_width = 20
space = 5
hor_offset = WIDTH/4

bars = []
sorting = True

def reset(screen):
    bars.clear()
    for i in range(num_bars):
        height = random.randint(10, 100)
        bars.insert(len(bars), height)
        x = hor_offset + (i*bar_width) + (i*space)
        drawBar(screen, x, height, BLACK)

def draw_bars(screen, j):
    #clear screen
    screen.fill(WHITE)
    #loop for drawing each bar
    for k in range(num_bars):
        x = hor_offset + (k*bar_width) + (k*space)
        if k==(j) or (k==(j+1)):
            drawBar(screen, x, bars[k], BLUE)
        else:
            drawBar(screen, x, bars[k], BLACK)

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            sorting = False

def bubbleSort(screen, bars):
    """
    sort and draw
    """
    n = len(bars)
    #bubble sorting algorithm, picking the maximum each time 
    for i in range(n-1):
        for j in range(0, n-1-i):
            if bars[j] > bars[j+1]:
                bars[j], bars[j+1] = bars[j+1], bars[j]
                draw_bars(screen, j)

                pygame.display.update()
                time.sleep(.2)

                handle_events()
                
    #sorting done , generate a new random list
    time.sleep(.6)
    reset(screen)

def drawBar(screen, x, height, color):
    pygame.draw.rect(screen, color, (x, 400-height, bar_width, height), 0)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(WHITE)

    reset(screen)

    pygame.display.update()

    while sorting:
        bubbleSort(screen, bars)


if __name__ == "__main__":
    main()
