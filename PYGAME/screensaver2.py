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

y_val2 = 15
y_off2 = 5

lifes = 5



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
    if x_val > 480 and x_val < 500:
        if y_val2 > y_val - 5 and y_val2 < y_val + 60:
            x_off = -3
            y_off = -4
    if x_val < 10 and x_val > -5:
        if y_val2 > y_val - 5 and y_val2 < y_val + 60:
            x_off = 3
            y_off = 4
    if y_val2 > 480:
        if y_val2 < 525:
            y_off = -4    
    if y_val2 < 0:
        if y_val2 > -20:
            y_off = 4
    if lifes > 0:
        if x_val < -5:
            lifes -= 1
            x_val = 25
            y_val = 15
            x_off = 3
            y_off = 4
            print(lifes)
        if x_val > 500:
            lifes -= 1
            x_val = 25
            y_val = 15
            x_off = 3
            y_off = 4
            print(lifes)
    if lifes == 0:
        print("Game Over!")
        print("I couldn't figure out how to print things on the display.")
        
    



    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, [x_val, y_val2, 20, 20])
    pygame.draw.rect(screen, BLACK, [490, y_val, 20, 60])
    pygame.draw.rect(screen, BLACK, [0, y_val, 10, 60])
    

    pygame.display.flip()
    clock.tick(60)