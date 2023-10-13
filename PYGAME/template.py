
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


pygame.display.set_caption("Let it snow.")


done = False
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True 

    pygame.display.flip()
    #defines frames per second
    clock.tick(60)