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
    def __init__(self, X, Y):
        super().__init__()
        self.image = pygame.Surface([100, 100])
        # player colour
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        # sets player shape
        self.rect.x = X
        self.rect.y = Y
        # player starts standing still
        self.xMove = 0
        self.yMove = 0
    # player movement direction
    def movement(self, input, map, mapY, mapX):
        # Calculate movement direction
        newX, newY = mapX, mapY
        if input == 97:  # 'a'
            if mapX - 1 == 0:
                print("placeholder")
            else:
                if map[mapY][mapX - 1] in traversableTiles:
                    self.xMove = -100
                    newX -= 1
        elif input == 115:  # 's'
            if mapY + 1 == len(map):
                print("placeholder")
            else:
                if map[mapY + 1][mapX] in traversableTiles:
                    self.yMove = 100
                    newY += 1
        elif input == 100:  # 'd'
            if mapX + 1 == len(map[mapY]):
                print("placeholder")
            else:
                if map[mapY][mapX + 1] in traversableTiles:
                    self.xMove = 100
                    newX += 1
        elif input == 119:  # 'w'
            if mapY - 1 == 0:
                print("placeholder")
            else:
                if map[mapY - 1][mapX] in traversableTiles:
                    self.yMove = -100
                    newY -= 1
        
        self.rect.x += self.xMove
        self.rect.y += self.yMove

        # Reset movement deltas
        self.xMove = 0
        self.yMove = 0

        return newX, newY



class tile(pygame.sprite.Sprite):
    def __init__(self, XCoord, YCoord):
        super().__init__()
        self.image = pygame.Surface([100, 100])
        self.image.fill(BROWN)
        self.rect=self.image.get_rect()
        self.rect.x = XCoord
        self.rect.y = YCoord
#class enemy(pygame.sprite.Sprite):
    #def __init__(self, XCoord, YCoord, hitpoints):
        #super().__init__()
        #self.image = pygame.Surface([100, 100])
        #self.image.fill(RED)
        #self.rect=self.image.get_rect()
        #self.rect.x = XCoord
        #self.rect.y = YCoord
        #self.hitpoints = hitpoints
    #def idle(self, )
    #def chase(self, )
    #def hurt(self, )
    #def die(self, )
    #def attack(self, ) - POLYMORPHISM

#class item(pygame.sprite.Sprite):
    #def __init__(self, XCoord, YCoord):
        #super().__init__()
        #self.image = pygame.Surface([100, 100])
        #self.image.fill(WHITE)
        #self.rect=self.image.get_rect()
        #self.rect.x = XCoord
        #self.rect.y = YCoord
    #def interacted(self, ):

#class template(pygame.sprite.Sprite):
    #def __init__(self, XCoord, YCoord):
        #super().__init__()
        #self.image = pygame.Surface([100, 100])
        #self.image.fill(WHITE)
        #self.rect=self.image.get_rect()
        #self.rect.x = XCoord
        #self.rect.y = YCoord
    

    
        
        
        



# variables 

# sprite groups
playerGroup = pygame.sprite.Group()

tileGroup = pygame.sprite.Group()

# maps
worldMap = [] # fill with zeros, determine map size later


# starting coordinates of player
playerMapX = 5
playerMapY = 5
# list of symbols that correspond to tiles that the player can travel through
traversableTiles = [0, 2, "P"]
# list of symbols that correspond to tiles that the player cannot travel through
nonTraversableTiles = [1]

map1 =      [[1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
            [1, 2, 1, 0, 0, 0, 0, 0, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, "P", 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
            [1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 0, 1, 1, 1, 1],]

# draws mapTemp
tileXCoord = 0
tileYCoord = 0
for i in map1:
    for j in i:
        if j == 1:
            tileTemp = tile(tileXCoord, tileYCoord)
            tileGroup.add(tileTemp)
        if j == "P":
            PLAYER = player(tileXCoord, tileYCoord)
            playerGroup.add(PLAYER)
        #if j == :  etc.
        tileXCoord += 100
    tileYCoord += 100
    tileXCoord = 0

        
    





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
            playerMapX, playerMapY = PLAYER.movement(event.key, map1, playerMapY, playerMapX)



            
            
        
            
    # coding code
    
    # update objects


    # drawing code
    screen.fill(BLACK)
    tileGroup.draw(screen)
    playerGroup.draw(screen)

    # end of game loop
    pygame.display.flip()
    clock.tick(60)