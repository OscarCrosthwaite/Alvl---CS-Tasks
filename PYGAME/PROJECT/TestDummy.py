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
pygame.display.set_caption("LEGEND OF THE LAND")
# start screen
def startMenu(X, Y):
    menuImage = pygame.image.load("")
    closeStartMenu = False
    # put image code here
    while closeStartMenu == False:
        print("placeholder")



# settings screen
def openSettings(X, Y):
    closeSettings = False
    font = pygame.font.SysFont('arial', 32)
    text = font.render(str("temp"), True, RED)
    textRect = text.get_rect()
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
                if event.key == pygame.K_ESCAPE:
                    closeSettings = True
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
            if mapX == 0:
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
            if mapY == 0:
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

def createObject(XCoord, YCoord, group, _class):
    temp = _class(XCoord, YCoord)
    group.add(temp)


map1 =      [[1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
            [1, 2, 1, 0, 0, 0, 0, 0, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, "P", 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
            [1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 0, 1, 1, 1, 1],]

# draws mapTemp
mapXCoord = 0
mapYCoord = 0
for i in map1:
    for j in i:
        if j == 1:
            tileTemp = tile(mapXCoord, mapYCoord)
            tileGroup.add(tileTemp)
        if j == "P":
            PLAYER = player(mapXCoord, mapYCoord)
            playerGroup.add(PLAYER)
        #if j == :  etc.
        mapXCoord += 100
    mapYCoord += 100
    mapXCoord = 0

        
    





# maps

#game loop
done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        # key inputs
        if event.type == pygame.KEYDOWN:
            # quit application
            if event.key == pygame.K_ESCAPE:
                openSettings(1000, 1000)   
                if event.key == pygame.K_ESCAPE:
                    done = True                    
                
            # object updates
            # movement
            playerMapX, playerMapY = PLAYER.movement(event.key, map1, playerMapY, playerMapX)


    # drawing
    screen.fill(BLACK)



    tileGroup.draw(screen)
    playerGroup.draw(screen)

    # end of game loop
    pygame.display.flip()
    clock.tick(60)