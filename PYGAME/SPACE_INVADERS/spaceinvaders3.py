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
size = (528, 528)
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
        self.image.fill(WHITE)
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
        self.yMovement = 20


    def x_update(self):
        self.rect.x = self.rect.x + self.xMovement
    def change_direction(self):
        self.xMovement = self.xMovement * -1
        self.rect.y = self.rect.y + self.yMovement
    


playerX = size[0]-size[0]/2
playerY = size[1]-size[1]/3
invader_speed = 1
bullet_speed = 25
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
invaderNumber = 10
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
            if keys[pygame.K_;]:
            # bullet firing
            while True:
                z = random.randint(0, 1)
                break
            if cooldownOn == True and z == 1:

                playerX = playerCharacter.coordUpdate()
                bullet = bullets(60, 60, playerX, playerY)
                bulletGroup.add(bullet)
                cooldownOn = True
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
