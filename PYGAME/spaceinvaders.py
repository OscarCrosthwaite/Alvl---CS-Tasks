# x_list = pygame.sprite.spritecollide(player, y_list, False)
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


pygame.display.set_caption("Let it snow.")


done = False
clock = pygame.time.Clock()

# Classes
class Player(pygame.sprite.Sprite):
    #constructor function (or is it?...)
    def __init__(self, s_width2, s_length2):
        super().__init__()
        self.image = pygame.Surface([s_width2, s_length2])
        self.image.fill(YELLOW)
        self.speed = 0
        self.rect=self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 475
    def update(self):
        self.rect.x = self.rect.x + self.speed




class Invaders(pygame.sprite.Sprite):

    #constructor function (or is it?...)
    def __init__(self, s_width, s_length):
        super().__init__()

        self.image = pygame.Surface([s_width, s_length])
        self.image.fill(RED)
        self.speed = random.randrange(1, 4)
        self.rect=self.image.get_rect()
        self.rect.x = random.randrange(0, 600)
        self.rect.y = random.randrange(0, 400)
    #end of constructor function
    def update(self):
        if self.rect.y > 500:
            self.rect.y = random.randint(0, 50)
            self.speed = random.randrange(1,4)
        else:
            self.rect.y = self.rect.y + self.speed
# end Class Snow

# Global Variables
invaders_group = pygame.sprite.Group()
number_of_aliens = 200
for i in range(0, number_of_aliens):
    alien = Invaders(10, 10)
    invaders_group.add(alien)
#next i

player_group = pygame.sprite.Group()



while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done =  True 
        #input keys 
        keys = pygame.key.get_pressed()
        #player 1
        if keys[pygame.K_a]:
            player_speed = -5
        if keys[pygame.K_d]:
            player_speed = 5

    #coding code
    invaders_group.update()
    player_group.update()

    
    
    #drawing code
    screen.fill(BLACK)
    invaders_group.draw(screen)
    player_group.draw(screen)









    pygame.display.flip()
    clock.tick(60)
