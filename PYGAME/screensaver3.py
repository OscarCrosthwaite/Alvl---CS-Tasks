import pygame
import math
pygame.init()
pygame.font.init()

#colours
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

#screen
size = (1000, 1000)
screen = pygame.display.set_mode(size)

#variables
    #paddle starting coords
x_off = 4
y_off = 5

y_val = 0
y_val2 = 0

    #ball starting coords
x_val = 5
y_val3 = 15


#game loop
done = False
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done = True


    #inputs
    keys = pygame.key.get_pressed()
        #player 1
    if keys[pygame.K_w]:
        y_val -= 9
    if keys[pygame.K_s]:
        y_val += 9

        #player 2
    if keys[pygame.K_UP]:
        y_val2 -= 9
    if keys[pygame.K_DOWN]:
        y_val2 += 9

    #coding code
        #offset
    x_val += x_off
    y_val3 += y_off

        #collision with top and bottom wall
    if y_val3 > 970:
        y_off = -y_off
    if y_val3 < 0:
        y_off = -y_off

        #collision with rectangles
    if x_val > 969 and x_val < 1001:
        if y_val3 > y_val2 -1 and y_val3 < y_val2 + 61:    
            x_off = -x_off
    if x_val < 10 and x_val > -25:
        if y_val3 > y_val -1 and y_val3 < y_val + 61:
            x_off = -x_off
        
        #consequences of missing balls
    if x_val < 0 or x_val > 1001:
        x_val = 25
        y_val3 = 25


    #drawing code
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, [x_val, y_val3, 30, 30])
    pygame.draw.rect(screen, WHITE, [0, y_val, 10, 90])
    pygame.draw.rect(screen, WHITE, [990, y_val2, 10, 90])
    


    #game loop
    pygame.display.flip()
    clock.tick(60)