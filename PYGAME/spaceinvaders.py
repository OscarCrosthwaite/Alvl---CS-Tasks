
#programarcadegames.com

import pygame
import math
import random
pygame.init()


BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLUE = (125, 125, 255)


size = (500, 500)
screen = pygame.display.set_mode(size)


pygame.display.set_caption("Space Invaders!")


done = False
clock = pygame.time.Clock()

# Classes
class player(pygame.sprite.Sprite):
    def __init__(self, s_width, s_length):
        super().__init__()
        self.image = pygame.Surface([s_width, s_length])
        self.image.fill(YELLOW)
        self.rect=self.image.get_rect()
        self.rect.x = playerX
        self.rect.y = playerY
    def update(self):
        self.rect.x = self.rect.x + player_speed
        
class Bullets(pygame.sprite.Sprite):
    def __init__(self, s_width, s_length, s_playerX, s_playerY):
        super().__init__()

        self.image = pygame.Surface([s_width, s_length])
        self.image.fill(RED)
        self.speed = 4
        self.rect=self.image.get_rect()
        self.rect.x = s_playerX + 7.5
        self.rect.y = s_playerY
    def update(self):
        self.rect.y = self.rect.y - 2
    #def checkCollision(self, s_list):
        #s_list = pygame.sprite.spritecollide(Bullets, alien)
        #if s_list == True:
            #score += 1
            
            

class Invaders(pygame.sprite.Sprite):

    #constructor function (or is it?...)
    def __init__(self, s_width, s_length):
        super().__init__()

        self.image = pygame.Surface([s_width, s_length])
        self.image.fill(RED)
        self.speed = random.randrange(1, 2)
        self.rect=self.image.get_rect()
        self.rect.x = random.randrange(0, 500)
        self.rect.y = random.randrange(-50, 0)
    #end of constructor function
    def update(self):
        if self.rect.y > 500:
            self.rect.y = random.randint(0, 50)
            self.speed = random.randrange(1,2)
        else:
            self.rect.y = self.rect.y + self.speed
# end Class Snow

# Global Variables
score = 0
player_speed = 3
bullet_speed = 0
playerX = 300
playerY = 450
printbullet = False

invaders_group = pygame.sprite.Group()
number_of_aliens = 50
for i in range(0, number_of_aliens):
    alien = Invaders(10, 10)
    invaders_group.add(alien)
#next i

player_group = pygame.sprite.Group()
player_character = player(25, 25)
player_group.add(player_character)

bullet_group = pygame.sprite.Group()
bullet = Bullets(10, 10, playerX, playerY)
#


while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done =  True 
        keys = pygame.key.get_pressed()
        player_speed = 0
        playerY = -100
        if keys[pygame.K_a]:
            player_speed = -3
        if keys[pygame.K_d]:
            player_speed = 3
        if keys[pygame.K_w]:
            bullet_group.add(bullet)
            

    #got to hereww
    for bullet in bullet_group:
        block_hit_list = pygame.sprite.spritecollide(bullet, invaders_group, True)
        for alien in invaders_group:
            bullet_group.remove(bullet)
            invaders_group.remove(alien)
            score += 1

    invaders_group.update()
    player_group.update()
    bullet_group.update()

    
    
    
    screen.fill(BLACK)
    invaders_group.draw(screen)
    player_group.draw(screen)
    bullet_group.draw(screen)

    pygame.display.flip()
    clock.tick(60)