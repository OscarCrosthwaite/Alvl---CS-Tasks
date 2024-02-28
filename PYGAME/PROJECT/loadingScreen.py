import pygame, sys, time, random, math
pygame.init()
pygame.font.init()

# colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLUE = (125, 125, 255)
BROWN = (150, 75, 0)

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
    text = font.render(str("temp"), True, RED)
    # creates drawable object containing text
    textRect = text.get_rect()
    # centers object
    textRect.center = (X // 2, Y // 2)
    # displays text
    while closeSettings == False:
        #registers keys
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                #closes settings when BACKSPACE pressed
                if event.key == pygame.K_BACKSPACE:
                    closeSettings = True
                # add more settings at a later date
                # volume, accessiblity (difficulty, etc.)
                # a way to quit the program
        # draws settings menu
        screen.fill(WHITE)
        screen.blit(text, textRect)
        pygame.display.flip()

    

        



# classes 
# all enemies need to be in the same class - use subclasses    

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

class tile(pygame.sprite.Sprite):
    def __init__(self, mapX, mapY):
        super().__init__()
        self.image = pygame.Surface([100, 100])
        self.image.fill(BROWN)
        self.rect=self.image.get_rect()
        self.rect.x = mapX
        self.rect.y = mapY
#class baseEnemy(self, ):
    
        
        
        



# variables 

# sprite groups
playerGroup = pygame.sprite.Group()
playerTemp = player()
playerGroup.add(playerTemp)

tileGroup = pygame.sprite.Group()

# maps
worldMap = [] # fill with zeros, determine map size later

map1 =  [[1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
            [1, 2, 1, 0, 0, 0, 0, 0, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
            [1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 0, 1, 1, 1, 1],]

# draws mapTemp
mapX = 0
mapY = 0
for i in map1:
    for j in i:
        if j == 1:
            tileTemp = tile(mapX, mapY)
            tileGroup.add(tileTemp)
        mapX += 100
    mapY += 100
    mapX = 0

        
    





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
                

            # player movement
            tempMovement = event.key
            #print(tempMovement)
            playerTemp.movement(tempMovement)



            
            
        
            
        print()
    print() 
    # coding code
    
    # update objects


    # drawing code
    screen.fill(BLACK)
    tileGroup.draw(screen)

    # create sprite groups
    playerGroup.draw(screen)

    # end of game loop
    pygame.display.flip()
    clock.tick(60)