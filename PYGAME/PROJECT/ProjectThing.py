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
GREY = (100, 100, 100)

# screen
size = (1000, 1000)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("LEGEND OF THE LAND")
# start screen
def startMenu(X, Y):
    # menu image code
    menuImage = pygame.image.load("PYGAME/tempStartMenu.png")
    menuImage = pygame.transform.scale(menuImage, (X, Y))
    closeStartMenu = False
    while closeStartMenu == False:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_ESCAPE:
                    closeStartMenu == True
                # can add save files at a later date, potentially
        screen.blit(menuImage, (0, 0))
        pygame.display.flip()
# settings screen
def openSettings(X, Y):
    global done
    closeSettings = False
    font = pygame.font.SysFont('arial', 32)
    text = font.render(str("temp"), True, RED)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 2)
    # displays text
    while closeSettings == False:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # if event.key == pygame.K_BACKSPACE:
                #    closeSettings = True
                # add more settings at a later date
                # volume, accessiblity (difficulty, etc.)
                # a way to quit the program
                if event.key == pygame.K_ESCAPE:
                    closeSettings = True
                if event.key == pygame.K_BACKSPACE:
                    closeSettings = True
                    done = True

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
    def getPlayerX(self):
        return self.rect.x
    def getPlayerY(self):
        return self.rect.y
    def movement(self, input, map, mapY, mapX, worldX, worldY):
        # Calculate movement direction
        newX, newY = mapX, mapY
        if input == 97:  # 'a'
            if mapX == 0:
                print("placeholder")
                worldX = worldX - 1
                groupReset()
                newX = 9 - newX
                self.rect.x = 900 - self.rect.x
            else:
                if map[mapY][mapX - 1] in traversableTiles:
                    self.xMove = -100
                    newX -= 1

        elif input == 115:  # 's'
            if mapY + 1 == len(map):
                print("placeholder")
                worldY = worldY + 1
                groupReset()
                newY = 9 - newY
                self.rect.y = 900 - self.rect.y
            else:
                if map[mapY + 1][mapX] in traversableTiles:
                    self.yMove = 100
                    newY += 1
        elif input == 100:  # 'd'
            if mapX + 1 == len(map[mapY]):
                print("placeholder")
                worldX = worldX + 1
                groupReset()
                newX = 9 - newX
                self.rect.x = 900 - self.rect.x
            else:
                if map[mapY][mapX + 1] in traversableTiles:
                    self.xMove = 100
                    newX += 1
        elif input == 119:  # 'w'
            if mapY == 0:
                print("placeholder")
                worldY = worldY - 1
                groupReset()
                newY = 9 - newY
                self.rect.y = 900 - self.rect.y
            else:
                if map[mapY - 1][mapX] in traversableTiles:
                    self.yMove = -100
                    newY -= 1
        
        self.rect.x += self.xMove
        self.rect.y += self.yMove

        # Reset movement deltas
        self.xMove = 0
        self.yMove = 0

        return newX, newY, worldX, worldY



class tile(pygame.sprite.Sprite):
    def __init__(self, X, Y):
        super().__init__()
        self.image = pygame.Surface([100, 100])
        self.image.fill(BROWN)
        self.rect=self.image.get_rect()
        self.rect.x = X
        self.rect.y = Y

class teleporter(tile):
    def __init__(self, X, Y, mapTemp):
        super().__init__(X, Y)
        self.image.fill(GREY)
        self.savedMap = mapTemp
        self.mapReturn = False

    def getTeleportX(self):
        return self.rect.x
    def getTeleportY(self):
        return self.rect.y    
    def getMap(self):
        return self.savedMap
    def getMapReturn(self):
        return self.mapReturn
    def teleportCheck(self, playerX, playerY):
        if playerX == self.rect.x and playerY == self.rect.y:
            groupReset()
            if self.mapReturn == False:
                generateMap(caveMap, PLAYER, tileGroup, playerGroup)
                self.mapReturn = True
            elif self.mapReturn == True:
                generateMap(worldMap[worldMapY][worldMapX], PLAYER, tileGroup, playerGroup)
                self.mapReturn = False

class enemy(tile):
    def __init__(self, X, Y):
        super().__init__(X, Y)
        self.image.fill(RED)
        self.xMove = 0
        self.yMove = 0
        self.mapX = int(X / 100)
        self.mapY = int(Y / 100)
    def enemyMovement(self, playerMapX, playerMapY, map):
        # horizontal
        if playerMapX > self.mapX: # to the right
            if map[self.mapY][self.mapX + 1] in traversableTiles:
                self.xMove = 100
                self.mapX += 1
        elif playerMapX < self.mapX: # to the left
            if map[self.mapY][self.mapX - 1] in traversableTiles:
                self.xMove = -100
                self.mapX -= 1

        # vertical
        elif playerMapY < self.mapY: # upwards
            if map[self.mapY - 1][self.mapX] in traversableTiles:
                self.yMove = -100
                self.mapY -= 1
        elif playerMapX > self.mapX: #downwards
            if map[self.mapY + 1][self.mapX] in traversableTiles:
                self.yMove = 100
                self.mapY += 1
        
        # movement + reset
        self.rect.x += self.xMove
        self.rect.y += self.yMove
        self.xMove = 0
        self.yMove = 0



                
            
    

# class enemy(pygame.sprite.Sprite):
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
# closeProgram = False


# sprite groups
playerGroup = pygame.sprite.Group()

tileGroup = pygame.sprite.Group()

teleporterGroup = pygame.sprite.Group()

enemyGroup = pygame.sprite.Group()


worldMap = [] # fill with zeros, determine map size later


# starting coordinates of player
playerMapX = 5
playerMapY = 5

# list of symbols that correspond to tiles that the player can travel through
traversableTiles = [0, 2, 3, "P"]
# list of symbols that correspond to tiles that the player cannot travel through
# nonTraversableTiles = [1, 3]

#def createObject(XCoord, YCoord, group, _class):
#    temp = _class(XCoord, YCoord)
#    group.add(temp)

# maps
 
# starting map
map1 =      [[1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
            [1, 2, 1, 1, 0, 0, 0, 1, 1, 1],
            [1, 0, 1, 0, 0, 0, 0, 0, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, "P", 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
            [1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 0, 1, 1, 1, 1],]

caveMap = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 2, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 1, 1, 1, 1],
            [1, 1, 0, 0, 0, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],]
inCaveMap = False

# 3, 2
map2 = [[1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 1, 1, 1, 0, 0, 0, 1],
        [1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 1, 0, 1, 1, 1, 1, 1],]

# 3, 4
map3 = [[1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
        [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
        [1, 0, 0, 1, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 1, 1, 0, 0, 0, 0, 1, 1],
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],]

# 4, 3
map4 = [[1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
        [1, 1, 0, 0, 0, 0, 1, 1, 0, 1],
        [1, 1, 0, 1, 0, 1, 1, 0, 0, 1],
        [1, 0, 0, 1, 1, 1, 1, 0, 0, 1],
        [1, 0, 0, 1, 0, 0, 0, 0, 1, 1],
        [1, 0, 0, 1, 1, 0, 0, 0, 1, 1],
        [1, 1, 0, 1, 1, 1, 1, 0, 0, 1],
        [1, 1, 0, 0, 1, 1, 1, 0, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],]

# 2, 3
map5 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 0, 1, 0, 1, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 1, 1, 1],
        [1, 1, 0, 0, 0, 0, 1, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],]

map6 = [[1, 1, 0, 1, 0, 1, 1, 1, 1, 1],
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 0, 1, 1, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [0, 3, 0, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 3, 0, 1, 1],
        [1, 1, 1, 1, 0, 0, 0, 0, 1, 1],
        [1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 0, 1, 1, 1, 1],]

map7 = [[1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 1, 1, 0, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],]

map8 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
        [0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],]

map9 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 3, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 3, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 3, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],]

map10 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1, 1, 1, 1],
        [1, 0, 1, 0, 1, 0, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 1, 1, 1, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 1, 0, 1, 0, 1, 0, 1],]

map11 = [[1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 1, 1, 1, 0, 0],
        [1, 0, 1, 0, 0, 0, 0, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],]

map12 = [[1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 0, 1, 1, 0, 1],
        [1, 0, 1, 1, 0, 0, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 0, 1, 1, 0, 1],
        [1, 0, 1, 1, 0, 0, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],]

map13 = [[1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 0, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],]

map14 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        [1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],]

map15 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
        [0, 0, 1, 0, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],]

map16 = [[1, 1, 1, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 1, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 1, 0, 0, 0, 0, 0, 1, 1],]

map17 = [[1, 1, 1, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 1, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 1, 1, 1, 1, 0, 0, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],]

map18 = [[1, 1, 0, 0, 0, 1, 1, 1, 1, 1],
        [1, 1, 0, 0, 0, 1, 1, 1, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 0, 0, 0, 0, 1, 1],]

map19 = [[1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 1, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 1, 1],
        [0, 0, 0, 0, 1, 1, 1, 0, 1, 1],
        [1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 0, 0, 1],]

map20 = [[1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 0, 0, 1, 1],
        [0, 1, 0, 0, 0, 1, 0, 0, 1, 1],
        [0, 0, 0, 1, 0, 0, 0, 0, 1, 1],
        [1, 1, 1, 1, 1, 1, 0, 0, 1, 1],
        [1, 1, 1, 0, 0, 1, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 1, 1, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 1, 0, 1, 1],
        [1, 1, 0, 0, 0, 1, 1, 1, 1, 1],]

map21 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 1, 1, 0, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 1, 1, 1, 0, 1, 1],
        [1, 0, 0, 1, 0, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 0, 0, 0, 1],]

map22 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 0, 0, 1, 1, 0, 0, 0, 0],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
        [1, 0, 0, 0, 0, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 0, 1, 1, 0, 1, 1],
        [1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
        [1, 1, 0, 0, 1, 1, 0, 0, 1, 1],]

map23 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
        [1, 1, 0, 1, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 1, 1, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],]

map24 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 0, 1, 1, 0, 1],
        [1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 1, 1, 0, 1],
        [1, 0, 1, 1, 0, 0, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],]

mapBoss = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],]

mapTemplate = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],]


# world map
worldMap = [[mapBoss, map24, map23, map22, map21],
            [map9, map8, map5, map19, map20],
            [map10, map2, map1, map3, map18],
            [map11, map6, map4, map7, map16], 
            [map12, map13, map14, map15, map17],]

# coords of current map
worldMapX = 2
worldMapY = 2

# check if current map needs to be changed
tempWorldMapX = 0
tempWorldMapY = 0

def generateMap(map, tempPlayer, tileGroup, playerGroup): # enemyGroup, etc.
    mapXCoord = 0
    mapYCoord = 0
    for i in map:
        for j in i:
            if j == 1:
                tileTemp = tile(mapXCoord, mapYCoord)
                tileGroup.add(tileTemp)
            if j == "P":
                # tempPlayer = player(mapXCoord, mapYCoord)
                playerGroup.add(tempPlayer)
            if j == 2:
                teleporterTemp = teleporter(mapXCoord, mapYCoord, worldMap[worldMapY][worldMapX])
                tileGroup.add(teleporterTemp)
                teleporterGroup.add(teleporterTemp)
            if j == 3:
                enemyTemp = enemy(mapXCoord, mapYCoord)
                tileGroup.add(enemyTemp)
                enemyGroup.add(enemyTemp)
            # if j == :... etc.
            mapXCoord += 100
        mapYCoord += 100
        mapXCoord = 0
    return tileGroup, playerGroup, tileTemp, tempPlayer, teleporterGroup # enemyGroup, etc.

def groupReset(): # enemyGroup, etc.
    groups = [tileGroup] # enemyGroup, etc.
    for group in groups:
        for sprite in group.sprites():
            sprite.kill()

PLAYER = player(500, 500)
generateMap(map1, PLAYER, tileGroup, playerGroup)




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
                
                
            # object updates
            # movement
            tempWorldMapX = worldMapX
            tempWorldMapY = worldMapY
            playerMapX, playerMapY, worldMapX, worldMapY = PLAYER.movement(event.key, worldMap[worldMapY][worldMapX], playerMapY, playerMapX, worldMapX, worldMapY)
            for enemyTemp2 in enemyGroup:
                enemyTemp2.enemyMovement(playerMapX, playerMapY, worldMap[worldMapY][worldMapX])

            if tempWorldMapX != worldMapX or tempWorldMapY != worldMapY:
                generateMap(worldMap[worldMapY][worldMapX], PLAYER, tileGroup, playerGroup)

      #      for teleTemp in teleporterGroup.sprites():
	 #           if teleTemp.getMap() == worldMap[worldMapY][worldMapX]:
    #                    teleTemp.teleportCheck(PLAYER.getPlayerX(), PLAYER.getPlayerY())
   #                     if teleTemp.getMapReturn() == False:
  #                          playerMapX, playerMapY, worldMapX, worldMapY = PLAYER.movement(event.key, caveMap, playerMapY, playerMapX, worldMapX, worldMapY)
 #                       else:
#                            playerMapX, playerMapY, worldMapX, worldMapY = PLAYER.movement(event.key, worldMap[worldMapY][worldMapX], playerMapY, playerMapX, worldMapX, worldMapY)
             
    # drawing
    screen.fill(BLACK)
    #startMenu(1000, 1000)
    tileGroup.draw(screen)
    playerGroup.draw(screen)

    # end of game loop
    pygame.display.flip()
    clock.tick(60)