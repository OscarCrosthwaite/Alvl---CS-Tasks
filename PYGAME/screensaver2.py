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
size = (500, 500)
screen = pygame.display.set_mode(size)

#variables
x_val = 25
y_val = 15
x_off = 3
y_off = 4

y_val2 = 15
y_off2 = 5

lifes = 5
score = 0

#game loop
done = False
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done = True

   #key detection for moving rectangles up and down
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        y_val -= 4
    elif keys[pygame.K_DOWN]:
        y_val += 4


    x_val += x_off
    y_val2 += y_off
    #code that makes ball bounce of the rectangles
    #also code that increases score
    if x_val > 478 and x_val < 495:
        if y_val2 > y_val - 5 and y_val2 < y_val + 60:
            x_off = -3
            score += 1
    if x_val < 10 and x_val > -5:
        if y_val2 > y_val - 5 and y_val2 < y_val + 60:
            x_off = 3
            score += 1
    
    #code that makes ball bounce of the top and bottom wall
    if y_val2 > 480:
        if y_val2 < 525:
            y_off = -4  
 
    if y_val2 < 0:
        if y_val2 > -20:
            y_off = 4

    #code that checks if you missed the ball and resets the score and the ball
    if x_val < -5:
        score = 0
        x_val = 25
        y_val = 15
        x_off = 3
        y_off = 4
    if x_val > 500:
        score = 0
        x_val = 25
        y_val = 15
        x_off = 3
        y_off = 4
    
    

    
    #creates the rectangles and the ball
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, [x_val, y_val2, 20, 20])
    pygame.draw.rect(screen, WHITE, [490, y_val, 20, 60])
    pygame.draw.rect(screen, WHITE, [0, y_val, 10, 60])
    
    #creates the score board
    font = pygame.font.Font(None, 36)
    score_text = font.render(str(score), True, RED)
    screen.blit(score_text, (250, 50))

    #game loop
    pygame.display.flip()
    clock.tick(60)