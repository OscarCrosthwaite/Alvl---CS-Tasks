#programarcadegames.com

#importing/initialiing
import pygame
import math
import random
pygame.init()

#colour
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLUE = (125, 125, 255)

#setting up game
size = (500, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Space Invaders!")
done = False
clock = pygame.time.Clock()

    #Classes
class player(pygame.sprite.Sprite):
    #creates player sprite
    def __init__(self, s_width, s_length):
        super().__init__()
        self.image = pygame.Surface([s_width, s_length])
        self.image.fill(YELLOW)
        self.rect=self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 375
    #allows player movement
    def update(self):
        self.rect.x = self.rect.x + player_speed
        playerX = self.rect.x
        
class Bullets(pygame.sprite.Sprite):
    #creates bullet sprite
    def __init__(self, s_width, s_length, s_playerX, s_playerY):
        super().__init__()

        self.image = pygame.Surface([s_width, s_length])
        self.image.fill(RED)
        self.speed = 4
        self.rect=self.image.get_rect()
        self.rect.x = s_playerX + 7.5
        self.rect.y = 375
    #allows bullet movement
    def update(self):
        self.rect.y = self.rect.y - 2

            

class Invaders(pygame.sprite.Sprite):
    #creates space invaders
    def __init__(self, s_width, s_length):
        super().__init__()

        self.image = pygame.Surface([s_width, s_length])
        self.image.fill(RED)
        self.speed = random.randrange(1, 2)
        self.rect=self.image.get_rect()
        self.rect.x = random.randrange(0, 500)
        self.rect.y = random.randrange(-50, 0)
    #makes space invaders move
    def update(self):
        if self.rect.y > 500:
            self.rect.y = random.randint(0, 50)
            self.speed = random.randrange(1,2)
        else:
            self.rect.y = self.rect.y + self.speed


    #Global Variables
score = 0
player_speed = 3
bullet_speed = 0

printbullet = False

    #Sprite Groups
#invaders group
invaders_group = pygame.sprite.Group()
number_of_aliens = 50
for i in range(0, number_of_aliens):
    alien = Invaders(10, 10)
    invaders_group.add(alien)

#player group
player_group = pygame.sprite.Group()
player_character = player(25, 25)
player_group.add(player_character)

#(most of) bullet group
bullet_group = pygame.sprite.Group()
bullet = Bullets(10, 10, playerX, playerY)


    #Game Loop
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done =  True 
        #creates key inputs for player
        keys = pygame.key.get_pressed()
        player_speed = 0
        playerY = -100
        if keys[pygame.K_a]:
            player_speed = -3
        if keys[pygame.K_d]:
            player_speed = 3
        if keys[pygame.K_w]:
            bullet_group.add(bullet)
            
    #hit collision between bullet and alien
    for bullet in bullet_group:
        block_hit_list = pygame.sprite.spritecollide(bullet, invaders_group, True)
        for alien in block_hit_list:
            bullet_group.remove(bullet)
            invaders_group.remove(alien)
            score += 1

    #update sprites
    invaders_group.update()
    player_group.update()
    bullet_group.update()
    
    #draws sprites
    screen.fill(BLACK)
    invaders_group.draw(screen)
    player_group.draw(screen)
    bullet_group.draw(screen)

    #ends game loop
    pygame.display.flip()
    clock.tick(60)