import pygame, sys, time, random, math
import heapq
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

def gameOver():
    global done, playerMapX, playerMapY, worldMapX, worldMapY, PLAYER
    closeGameOver = False
    font = pygame.font.SysFont('arial', 32)
    text = font.render(str("Press 'R' to retry"), True, RED)
    textRect = text.get_rect()
    textRect.center = (500, 400)
    text2 = font.render(str("Press 'ESC' to quit"), True, RED)
    textRect2 = text2.get_rect()
    textRect2.center = (500, 600)

    while closeGameOver == False:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    closeGameOver = True
                if event.key == pygame.K_ESCAPE:
                    closeGameOver = True
                    done = True
        screen.fill(BLACK)
        screen.blit(text, textRect)
        screen.blit(text2, textRect2)
        pygame.display.flip()
    groupReset()
    PLAYER.resetPlayerPosition()
    playerMapX, playerMapY, worldMapX, worldMapY  = 5, 5, 2, 2
    generateMap(worldMap[worldMapY][worldMapX], PLAYER, tileGroup, playerGroup)

            
    

        



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
    def resetPlayerPosition(self):
        self.rect.x = 500
        self.rect.y = 500

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
    
    def attack(self):
        
        print()



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
    def __init__(self, X, Y, g, h):
        super().__init__(X, Y)
        self.image.fill(RED)
        self.xMove = 0
        self.yMove = 0
        self.mapX = int(X / 100)
        self.mapY = int(Y / 100)

        # A* attributes
        self.distance = g
        self.heuristic = h
        self.total = g + h # f
        self.parent = None # parent node
        self.path = []


    def getMapX(self):
        return self.mapX
    def getMapY(self):
        return self.mapY

    def findHeuristic(self):
        return abs(self.mapX - playerMapX) + abs(self.mapY - playerMapY)

    def aStarMovement(self, map, occupiedNodes):
        unvisitedNodes = []
        startNode = node(self.mapX, self.mapY, 0, self.findHeuristic())
        heapq.heappush(unvisitedNodes, (0, node(self.mapX, self.mapY, self.distance, self.heuristic))) #(self.mapX, self.mapY)))
        visitedNodes = set()
        nodes = {(self.mapX, self.mapY): startNode} # node dictionary

        while unvisitedNodes:
            _, currentNode = heapq.heappop(unvisitedNodes)
            if (currentNode.getX(), currentNode.getY()) == (playerMapX, playerMapY):
                # print("placeholder")
                while currentNode:
                    self.path.append((currentNode.getX(), currentNode.getY()))
                    currentNode = currentNode.parent
                self.path.reverse()
                return self.path
            
            visitedNodes.add((currentNode.getX(), currentNode.getY()))

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = currentNode.getX() + dx, currentNode.getY() + dy
                if 0 <= nx < 10 and 0 <= ny < 10 and map[ny][nx] == 0 and (nx, ny) not in visitedNodes and (nx, ny) not in occupiedNodes:
                    # print("placeholder")
                    g = currentNode.g + 1
                    h = self.findHeuristic()
                    neighbour = node(nx, ny, g, h)
                    if (nx, ny) in nodes:
                        # neighbour = nodes[(nx, ny)]
                        if g < neighbour.getG():
                            neighbour.setG(g)
                            neighbour.setParent(currentNode)
                    else:

                        neighbour.setParent(currentNode)
                        nodes[(nx, ny)] = neighbour

                        heapq.heappush(unvisitedNodes, (neighbour.getTotal(), neighbour))

                    #neighbour = nodes.get((nx, ny), node(nx, ny, g, h))
                    #if (neighbour[0], neighbour[1]) not in nodes or g < self.distance:
                    #    g, f, neighbour.parent = g, g+ h, currentNode
                    #    heapq.heappush(unvisitedNodes, (neighbour.f, neighbour))
                    #    nodes[(nx, ny)] = neighbour
                    #self.distance = g        

    def findPath(self, map):
        occupiedNodes = []
        for enemyTemp3 in enemyGroup:
            occupiedNodes.append((enemyTemp3.getMapX(), enemyTemp3.getMapY()))
        self.path = enemy.aStarMovement(self, map, occupiedNodes)

    def playerDestruction(self):
        if (self.mapX, self.mapY) == (playerMapX, playerMapY):
            gameOver()
    
    def move(self):
        if self.path:
            self.mapX, self.mapY = self.path.pop(1)
            self.rect.x = self.mapX * 100
            self.rect.y = self.mapY * 100
        self.playerDestruction()
        

class node():
    def __init__(self, x, y, g, h):
        self.x = x
        self.y = y
        self.g = g
        self.h = h
        self.parent = None
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getG(self):
        return self.g
    def setG(self, newG):
        self.g = newG
    def getTotal(self):
        return self.g + self.h
    def setParent(self, newParent):
        self.parent = newParent
    def __lt__(self, other):
        return self.getTotal() < other.getTotal()



        

                    





                
            


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
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
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
                enemyTemp = enemy(mapXCoord, mapYCoord, 0, 0)
                tileGroup.add(enemyTemp)
                enemyGroup.add(enemyTemp)
            # if j == :... etc.
            mapXCoord += 100
        mapYCoord += 100
        mapXCoord = 0
    return tileGroup, playerGroup, tileTemp, tempPlayer, teleporterGroup, enemyGroup # enemyGroup, etc.

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
                enemyTemp2.findPath(worldMap[worldMapY][worldMapX])
                enemyTemp2.move()

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