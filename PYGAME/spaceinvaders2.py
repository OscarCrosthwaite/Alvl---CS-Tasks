# importing/initialising
import pygame
import math
import random
import time
pygame.init()

# colour
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLUE = (125, 125, 255)

# setting up game basics
size = (500, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("SPACE INVADERS!")
done = False
clock = pygame.time.Clock()

# classes
class player(pygame.sprite.Sprite):
    def __init__(self, s_width, s_length, s_playerX, s_playerY):
        super().__init__()
        self.image = pygame.Surface([s_width, s_length])
        self.image.fill(YELLOW)
        self.rect=self.image.get_rect()
        self.rect.x = s_playerX
        self.rect.y = s_playerY
    def update(self, s_player_speed):
        self.rect.x = self.rect.x + s_player_speed
    def coordUpdate(self):
        return self.rect.x
        


        

        

class bullets(pygame.sprite.Sprite):
    def __init__(self, s_width, s_length, s_playerX, s_playerY):
        super().__init__()
        self.image = pygame.Surface([s_width, s_length])
        self.image.fill(RED)
        self.rect=self.image.get_rect()
        self.rect.x = s_playerX
        self.rect.y = s_playerY 
    def update(self, s_bulletSpeed):
        self.rect.y = self.rect.y - s_bulletSpeed

class invaders(pygame.sprite.Sprite):
    def __init__(self, s_width, s_length, s_invaderX, s_invaderY):
        super().__init__()
        self.image = pygame.Surface([s_width, s_length])
        self.image.fill(RED)
        self.rect=self.image.get_rect()
        self.rect.x = 10 * s_invaderX
        self.rect.y = -10 * s_invaderY
        self.xMovement = 5
        self.yMovement = 10


    def x_update(self):
        self.rect.x = self.rect.x + self.xMovement
    def change_direction(self):
        self.xMovement = self.xMovement * -1
        self.rect.y = self.rect.y + self.yMovement
    


playerX = 250
playerY = 375
invader_speed = 1
bullet_speed = 5
invaderX = 550
invaderY = 0
cooldownOn = True
cooldownOn2 = True

count = 1




# sprite groups
playerGroup = pygame.sprite.Group()
playerCharacter = player(25, 25, playerX , playerY)
playerGroup.add(playerCharacter)

bulletGroup = pygame.sprite.Group()


invaderGroup = pygame.sprite.Group()
invaderNumber = 7
for j in range(0, 3):
    invaderY = j * 6
    for i in range(0, invaderNumber):
        invaderX = i * 4.8
        invader = invaders(20, 20, invaderX, invaderY)
        invaderGroup.add(invader)


# game loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # key inputs
        keys = pygame.key.get_pressed()
        player_speed = 0
        if keys[pygame.K_a]:
            player_speed = -3
        if keys[pygame.K_d]:
            player_speed = 3
        if keys[pygame.K_w]:
            # bullet firing
            if cooldownOn == True:
                playerX = playerCharacter.coordUpdate()
                bullet = bullets(10, 10, playerX, playerY)
                bulletGroup.add(bullet)
                cooldownOn = False
                bulletCooldown = pygame.time.get_ticks()
            if pygame.time.get_ticks() - bulletCooldown >= 1000:
                cooldownOn = True


    # bullet collision
    for bullet in bulletGroup:
        blockHitList = pygame.sprite.spritecollide(bullet, invaderGroup, True)
        for alien in blockHitList:
            bulletGroup.remove(bullet)
            invaderGroup.remove(alien)

            
    # sprite movement
    playerGroup.update(player_speed)
    bulletGroup.update(bullet_speed)
    for invader in invaderGroup:
        if invader.rect.x >= 505 or invader.rect.x <= -5:
            for invader in invaderGroup:
                invader.change_direction()
    for invader in invaderGroup:
        invader.x_update()
    

    # draws screen
    screen.fill(BLACK)
    playerGroup.draw(screen)
    bulletGroup.draw(screen)
    invaderGroup.draw(screen)


    # frame rate
    pygame.display.flip()
    clock.tick(25)
