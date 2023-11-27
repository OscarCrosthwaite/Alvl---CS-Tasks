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
    def update(self, s_hpMove, s_vpMove):
        self.rect.x = self.rect.x + s_hpMove
        self.rect.y = self.rect.y + s_vpMove
    def collision(self, s_hpMove, s_vpMove):
        self.rect.x = self.rect.x - s_hpMove
        self.rect.x = self.rect.x - s_vpMove

class wall(pygame.sprite.Sprite):
    def __init__(self, wWidth, wLength, wXCoord, wYCoord):
        super().__init__()
        self.image = pygame.Surface([wWidth, wLength])
        self.image.fill(BLUE)
        self.rect=self.image.get_rect()
        self.rect.x = wXCoord
        self.rect.y = wYCoord


        
    


#variables

#pacman move speed
hpMove = 0
vpMove = 0

#map coords
mapX = 0
mapY = 0


#sprite groups
#pacman group
pacmanGroup = pygame.sprite.Group()
pacmanTemp = pacman(25, 25)
pacmanGroup.add(pacmanTemp)

#wall group
wallGroup = pygame.sprite.Group()



#plans walls
map = [ [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], #1
	    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], #2
	    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], #3
	    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], #4
	    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], #5
	    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], #6
	    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], #7
	    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], #8
	    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], #9
    	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #10
	    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #11
	    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], #12
    	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], #13
	    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], #14
    	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], #15
	    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], #16
    	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], #17
	    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], #18
	    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], #19
	    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] ]

#draws walls
for i in map:

    for j in i:
        if j == 1:
            wallTemp = wall(50, 50, mapX, mapY)
            wallGroup.add(wallTemp)
        mapX = mapX + 50
    mapX = 0
    mapY = mapY + 50



#game loop
done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #key inputs
        keys = pygame.key.get_pressed()
        hpMove = 0
        vpMove = 0
        if keys[pygame.K_a]:
            hpMove = -5
        if keys[pygame.K_d]:
            hpMove = 5
        if keys[pygame.K_s]:
            vpMove = 5
        if keys[pygame.K_w]:
            vpMove = -5

            

    
    #coding code

    #sprite collision
    #pacman collision with wall
    for wallTemp in wallGroup:
        wallObstructList = pygame.sprite.spritecollide(wallTemp, pacmanGroup, False)
        for pacmanTemp in wallObstructList:
            if pacmanTemp.rect.colliderect(wallTemp.rect):
                hpMove = 
                vpMove = 
                pacmanGroup.update(hpMove, vpMove)
            
                
            
    
            

    #update functions
    pacmanGroup.update(hpMove, vpMove)
    

    #drawing code
    screen.fill(BLACK)
    pacmanGroup.draw(screen)
    wallGroup.draw(screen)



    #completes game loop
    pygame.display.flip()
    clock.tick(60)