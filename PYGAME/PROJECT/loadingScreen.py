import pygame, sys, time, random, math
pygame.init()
pygame.font.init()

# colours
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLUE = (125, 125, 255)

# screen
size = (1000, 1000)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("TEMP NAME")
# settings screen
def openSettings(X, Y):
    closeSettings = False
    # sets font and text size
    font = pygame.font.SysFont('arial', 32)
    # sets text to write
    text = font.render(str("temp"), True, WHITE)
    # creates drawable object containing text
    textRect = text.get_rect()
    # centers object
    textRect.center = (X // 2, Y // 2)
    # displays text until ESCAPE is pressed
    while closeSettings == False:
        screen.blit(text, textRect)
        if event.key == pygame.K_BACKSPACE:
            closeSettings == True

        



# classes 
class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([100, 100])
        # player colour
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        # sets player shape
        self.rect.x = 100
        self.rect.y = 100
        # player starts standing still
        self.xMovement = 0
        self.yMovement = 0
    # player movement direction
    def movement(self, input):
        # resets movement every frame
        self.xMovement = 0
        self.yMovement = 0
        # sets player direction - uses ASCII
        if input == 97:
            self.xMovement = -100
        if input == 115:
            self.yMovement = 100   
        if input == 100:
            self.xMovement = 100
        if input == 119:
            self.yMovement = -100 
        # moves player
        self.rect.x += self.xMovement
        self.rect.y += self.yMovement

        
        



# variables 

# sprite groups
playerGroup = pygame.sprite.Group()
playerTemp = player()
playerGroup.add(playerTemp)       

# maps
worldMap = []#fill with zeros, determine map size later]

mapTemp =  [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],]

# draws map - temp
#for i in corresponding map:
    #for j in i:
        #if j == number that corresponds to object class:
            #adds map object
        #x-coordinate increase by 100
    #resets x-coordinate 
    #y-coordinate increase by 100
    
        
    





# maps

#game loop
done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            done = True
        # key inputs
        elif event.type == pygame.KEYDOWN:
            # quit application
            if event.key == pygame.K_ESCAPE:
                openSettings(1000, 1000)
                #done = True
            # player movement
            tempMovement = event.key
            print(tempMovement)
            playerTemp.movement(tempMovement)



            
            
        
            
        print()
    print() 
    # coding code
    
    # update objects


    # drawing code
    screen.fill(BLACK)

    # create sprite groups
    playerGroup.draw(screen)

    # end of game loop
    pygame.display.flip()
    clock.tick(60)