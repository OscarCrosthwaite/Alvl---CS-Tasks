#initialize pygame
import pygame
import math
pygame.init()

#pygame doesnt have its own colours
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

#creates a screen
size = (700, 500)
screen = pygame.display.set_mode(size)

#displays a caption
pygame.display.set_caption("test pygame program")

#loop until user clicks the close button
done = False
#used to manage how fast the screen updates
clock = pygame.time.Clock()

# Global Variables
x_val = 0
y_val = 50
x2_val = -750
y2_val = 50

# -Main Program Loop-
while not done:
    for event in pygame.event.get(): #user does something
        if event.type == pygame.QUIT: #if user hypothetically clicked close
            done = True #flag that we are done and to exit the loop
    
    # -game logic is put here-
    y_val = 50
    x_val += 5
    if x_val > 700:
        x_val = -750
    x2_val += 5
    if x2_val > 700:
        x2_val = -750
    

    # -drawing code is put here-
    screen.fill(WHITE)
    if x_val < 0:
        screen.fill(BLACK)
    if x2_val < 0:
        screen.fill(WHITE)
    
    #put all drawing code beneath the screen.fill command
    

    pygame.draw.rect(screen, GREEN, [0, 250, 700, 250])
    pygame.draw.rect(screen, RED, [200, 200, 200, 200,])
    pygame.draw.rect(screen, RED, [225, 125, 50, 75])
    pygame.draw.polygon(screen, RED, [(200, 200), (400, 200), (300, 150)])
    pygame.draw.rect(screen, WHITE, [300, 325, 50, 75])
    pygame.draw.rect(screen, WHITE, [250, 250, 40, 40])
    pygame.draw.rect(screen, WHITE, [335, 250, 40, 40])
    pygame.draw.circle(screen, YELLOW, [x_val, y_val], 25)
    pygame.draw.circle(screen, WHITE, [x2_val, y2_val], 25)
    pygame.draw.circle(screen, BLACK, [x2_val + 5, y2_val -3], 25)

    


    pygame.display.flip()
    #defines frames per second
    clock.tick(60)
