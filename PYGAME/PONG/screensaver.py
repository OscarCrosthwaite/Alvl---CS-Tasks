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
y_val2 = 15
x_off = 3
y_off = 4
y_off2 = 5

done = False
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done = True


    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        y_val -= 3
    elif keys[pygame.K_DOWN]:
        y_val += 3



    x_val += x_off
    y_val2 += y_off
    if x_val > 480:
        if y_val2 == y_val:
            x_off = -3
    if x_val < 0:
        if y_val2 == y_val:
            x_off = 3

    if y_val2 > 480:
        y_off = -4    
    if y_val2 < 0:
        y_off = 4



    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, [x_val, y_val2, 20, 20])
    pygame.draw.rect(screen, BLACK, [490, y_val, 20, 60])
    pygame.draw.rect(screen, BLACK, [0, y_val, 10, 60])


    pygame.display.flip()
    clock.tick(60)