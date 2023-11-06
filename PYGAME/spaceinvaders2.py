# importing/initialising
import pygame
import math
import random
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

class bullets(pygame.sprite.Sprite):
    def __init__(self, s_width, s_length, s_playerX, s_playerY):
        super().__init__()
        self.image = pygame.Surface([s_width, s_length])
        self.image.fill(RED)
        self.rect=self.image.get_rect()
        self.rect.x = s_playerX
        self.rect.x = s_playerY 
    def update(self, s_bulletSpeed):
        self.rect.y = self.rect.y - s_bulletSpeed

class invaders(pygame.sprite.Sprite):
    def __init__(self, s_width, s_length):
        super().__init__()
        self.image = pygame.Surface([s_width, s_length])
        self.image.fill(RED)
        self.rect=self.image.get_rect()
        self.rect.x = random.randrange(0, 500)
        self.rect.y = random.randrange(-50, 0)
    def update(self, ):
        if self.rect.y > 500:
            self.rect.y = random.randint(-50, 0)
            self.speed = 2
        else:
            self.rect.y = self.rect.y + self.speed
# global variables
score = 0
playerX = 250
playerY = 475



# sprite groups
playerGroup = pygame.sprite.Group()
playerCharacter = player(25, 25, playerX , playerY)
playerGroup.add(playerCharacter)

bulletGroup = pygame.sprite.Group()
bullet = bullets(10, 10, playerX, playerY)

invaderGroup = pygame.sprite.Group()
invaderNumber = 50
for i in range(0, invaderNumber):
    invader = invaders(10, 10)
    invaderGroup.add(invader)

# game loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        keys = pygame.key.get_pressed()
        player_speed = 0
        if keys[pygame.K_a]:
            player_speed = -3
        if keys[pygame.K_d]:
            player_speed = 3
        if keys[pygame.K_w]:
            bulletGroup.add(bullet)

    for bullet in bulletGroup:
        blockHitList = pygame.sprite.spritecollide(bullet, invaderGroup, True)
        for alien in blockHitList:
            bulletGroup.remove(bullet)
            invaderGroup.remove(alien)
            score += 1

    playerGroup.update(player_speed)
    bulletGroup.update()
    invaderGroup.update()

    screen.fill(BLACK)
    playerGroup.draw(screen)
    bulletGroup.draw(screen)
    invaderGroup.draw(screen)

    pygame.display.flip()
    clock.tick(60)


