#initialises pygame
import pygame
import math
import random
import time
pygame.init()

#colours
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLUE = (125, 125, 255)

#screen
size = (1000, 1000)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("PACMAN")


#classes
class pacman(pygame.sprite.Sprite):
    def __init__(self, pWidth, pLength):
        super().__init__()
        self.image = pygame.Surface([pWidth, pLength])
        self.image.fill(RED)
        self.rect=self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 500
    def pDown(self):
        self.rect.y = self.rect.y - pMovement
    def pUp(self):
        self.rect.y = self.rect.y + pMovement
    def pRight(self):
        self.rect.x = self.rect.x + pMovement
    def pLeft(self):
        self.rect.y = self.rect.y - pMovement
        
    


#variables
pMovement = 5

#sprite groups
pacmanGroup = pygame.sprite.Group()
pacmanTemp = pacman(25, 25)
pacmanGroup.add(pacmanTemp)


#game loop
done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #key inputs
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            pacmanGroup.pLeft()
        if keys[pygame.K_d]:
            pacmanGroup.pRight()
        if keys[pygame.K_s]:
            pacmanGroup.pDown()
        if keys[pygame.K_w]:
            pacmanGroup.pUp()

    
    #coding code


    #drawing code
    screen.fill(BLACK)



    #completes game loop
    pygame.display.flip()
    clock.tick(25)