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
x_val = 250
y_val3 = 250

    #lives
lives1 = 5
lives2 = 5

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
    if x_val > 980 and x_val < 1006:
        if y_val3 > y_val2 -1 and y_val3 < y_val2 + 91: 
            #collision effects   
            x_off = -x_off
            x_off = x_off * 1.1


    if x_val < 9 and x_val > -17:
        if y_val3 > y_val -1 and y_val3 < y_val + 91:
            #collision effects
            x_off = -x_off
            x_off = x_off * 1.1
        
        #consequences of missing balls
    if x_val < 0: 
        x_val = 500
        y_val3 = 500
        x_off = 4
        y_off = 5
        lives1 -= 1
        if lives1 == 0:
            x_val = 500
            y_val3 = 750
            x_off = 0
            y_off = 0



    if x_val > 1001: 
        x_val = 500
        y_val3 = 500
        x_off = 4
        y_off = 5
        lives2 -= 1
        if lives2 == 0:
            x_val = 500
            y_val3 = 750
            x_off = 0
            y_off = 0
            

    #drawing code
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, [x_val, y_val3, 20, 20])
    pygame.draw.rect(screen, WHITE, [0, y_val, 13, 90])
    pygame.draw.rect(screen, WHITE, [990, y_val2, 13, 90])
    pygame.draw.rect(screen, WHITE, [485, 0, 30, 100])

    #displays lives
    font = pygame.font.Font(None, 127)
    score_text1 = font.render(str(lives1), True, RED)
    screen.blit(score_text1, (425, 5))
    score_text2 = font.render(str(lives2), True, RED)
    screen.blit(score_text2, (525, 5))
    if lives1 == 0:
        gameLost1 = font.render(str("Player 1 has lost."), True, RED)
        screen.blit(gameLost1, (50, 100))
    
    if lives2 == 0:
            gameLost2 = font.render(str("Player 2 has lost."), True, RED)
            screen.blit(gameLost2, (50, 100))


    #game loop
    pygame.display.flip()
    clock.tick(60)