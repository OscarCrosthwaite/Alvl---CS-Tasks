
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
class Snow(pygame.sprite.Sprite):

    #constructor function (or is it?...)
    def __init__(self, s_width, s_length):
        super().__init__()

        self.image = pygame.Surface([s_width, s_length])
        self.image.fill(WHITE)
        self.speed = random.randrange(1, 4)
        self.rect=self.image.get_rect()
        self.rect.x = random.randrange(0, 600)
        self.rect.y = random.randrange(0, 400)
    #end of constructor function
    def update(self):
        if self.rect.y > 500:
            self.rect.y = -50
            self.speed = random.randrange(1,4)
        else:
            self.rect.y = self.rect.y + self.speed
# end Class Snow

# Global Variables
snow_group = pygame.sprite.Group()
number_of_flakes = 200
for i in range(0, number_of_flakes):
    flake = Snow(random.randint(5, 10), 10)
    snow_group.add(flake)
#next i



while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done =  True 
    #coding code
    snow_group.update()


    
    
    #drawing code
    screen.fill(BLUE)
    snow_group.draw(screen)









    pygame.display.flip()
    clock.tick(60)