import pygame
import math
pygame.init()

BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

size = (500, 500)
screen = pygame.display.set_mode(size)

x_val = 25
y_val = 15
x_off = 3
y_off = 4

done = False
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done = True
    
    #coding code
    x_val += x_off
    y_val += y_off
    if x_val > 480:
        x_off = -3
    if y_val > 480:
        y_off = -4
    if x_val < 0:
        x_off = 3
    if y_val < 0:
        y_off = 4


    #drawing code
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, [x_val, y_val, 20, 20])
    pygame.draw.rect(screen, BLACK, [490, y_val, 20, 60])
    pygame.draw.rect(screen, BLACK, [0, y_val, 10, 60])


    pygame.display.flip()
    clock.tick(60)