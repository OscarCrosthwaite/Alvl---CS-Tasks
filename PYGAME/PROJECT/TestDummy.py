import pygame, sys, time, random, math
import heapq
import threading

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
CYAN = (0, 255, 255)
PURPLE = (128, 0, 128) 

# screen
size = (1000, 1000)
screen = pygame.display.set_mode(size)

# name of application
pygame.display.set_caption("LEGEND OF THE LAND")

# graphics/images for objects
startMenuImage = pygame.image.load('PYGAME/PROJECT/PICTURES/startMenuImage.png')

    # player graphics
playerDownImage = pygame.image.load('PYGAME/PROJECT/PICTURES/playerDown.png')
playerLeftImage = pygame.image.load('PYGAME/PROJECT/PICTURES/playerLeft.png')
playerRightImage = pygame.image.load('PYGAME/PROJECT/PICTURES/playerRight.png')
playerUpImage = pygame.image.load('PYGAME/PROJECT/PICTURES/playerUp.png')

    # object graphics
tileImage = pygame.image.load('PYGAME/PROJECT/PICTURES/rockyTile.png')
enemyImage = pygame.image.load('PYGAME/PROJECT/PICTURES/enemy.png')
chestImage = pygame.image.load('PYGAME/PROJECT/PICTURES/chest.png')
swordImage = pygame.image.load('PYGAME/PROJECT/PICTURES/sword.png')
arrowImage = pygame.image.load('PYGAME/PROJECT/PICTURES/arrow.png')
bossImage = pygame.image.load('PYGAME/PROJECT/PICTURES/boss.png')

# menus

# title screen
def startMenu():
    # title screen image
    menuImage = pygame.transform.scale(startMenuImage, (1000, 1000))
    # menu input loop
    closeStartMenu = False
    while closeStartMenu == False:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    closeStartMenu = True
                # can add save files at a later date, potentially
        screen.blit(menuImage, (0, 0))
        pygame.display.flip()

# settings screen
def openSettings():
    # global variables originally intended to be temporary
    global done, coins
    closeSettings = False

    # line one
    font = pygame.font.SysFont('arial', 32)
    text = font.render(str("Press ESCAPE to quit menu"), True, RED)
    textRect = text.get_rect()
    textRect.center = (800, 250)

    # line two
    text2 = font.render(str("Press BACKSPACE to quit game"), True, RED)
    textRect2 = text2.get_rect()
    textRect2.center = (800, 350)

    # line three
    text3 = font.render(str("Use WASD to move. Use Q and E to attack."), True, RED)
    textRect3 = text3.get_rect()
    textRect3.center = (275, 800)

    # line four
    text5 = font.render(str(f"You have {coins} coins"), True, RED)
    textRect5 = text5.get_rect()
    textRect5.center = (800, 450)
    screen.fill(BLACK)

    # display world map and position of Player on world map
    createMiniMap(100, 100)

    while closeSettings == False:
        # stopwatch code
            # deletes prior time displayed on screen
        pygame.draw.rect(screen, BLACK, (550, 750, 200, 100))
        stopwatch = pygame.time.get_ticks() // 1000
        text4 = font.render(f"Timer: {str(stopwatch)}", True, RED)
        textRect4 = text4.get_rect()
        textRect4.center = (600, 800)
        # settings input loop
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # could add more inputs/settings at later date
                    # such as difficulty or volume and so on and so forth
                if event.key == pygame.K_ESCAPE: # just closes settings
                    closeSettings = True
                if event.key == pygame.K_BACKSPACE: # closes entire game
                    closeSettings = True
                    done = True

        # draws components of settings menu
        screen.blit(text, textRect)
        screen.blit(text2, textRect2)
        screen.blit(text3, textRect3)
        screen.blit(text4, textRect4)
        screen.blit(text5, textRect5)
        pygame.display.flip()

def createMiniMap(X, Y): # X and Y connote position of top left of mini map
    # ranges for row and column refer to playerMapX and playerMapY
    for row in range(5): 
        for column in range(5):
            pygame.draw.rect(screen, WHITE, (X + column * 100, Y + row * 100, 100, 100)) # prints a white square for each map
            pygame.draw.rect(screen, BLACK, (X + column * 100, Y + row * 100, 100, 100), 5) # grid lines
    pygame.draw.rect(screen, GREEN, (100 + worldMapX * 100, 100 + worldMapY * 100, 100, 100)) # prints a green square to indicate which map the Player is in
    pygame.display.flip()

def gameOver():
    # again, global variables originally intended to be temporary, but kept in to save time
    global done, playerMapX, playerMapY, worldMapX, worldMapY, PLAYER, coins
    closeGameOver = False
    # resets how many coins the Player has
    coins = 0
    font = pygame.font.SysFont('arial', 32)

    # line one
    text = font.render(str("Press 'R' to retry"), True, RED)
    textRect = text.get_rect()
    textRect.center = (500, 400)

    # line two
    text2 = font.render(str("Press 'ESC' to quit"), True, RED)
    textRect2 = text2.get_rect()
    textRect2.center = (500, 600)

    # game over input loop
    while closeGameOver == False:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # same design as settings meny
                if event.key == pygame.K_r: # just closes settings
                    closeGameOver = True
                if event.key == pygame.K_ESCAPE: # closes entire game
                    closeGameOver = True
                    done = True
        screen.fill(BLACK)
        screen.blit(text, textRect)
        screen.blit(text2, textRect2)
        pygame.display.flip()
    
    # resets game
    groupReset()
    # puts Player back on first map
    PLAYER.resetPlayerPosition()
    # resets coords
    playerMapX, playerMapY, worldMapX, worldMapY  = 5, 5, 2, 2
    generateMap(worldMap[worldMapY][worldMapX], PLAYER, tileGroup, playerGroup)

def victoryScreen():
    global coins, done
    closeVictoryScreen = False
    font = pygame.font.SysFont('arial', 32)

    # line one
    # "secret ending" for Players who have collected more coins
    if coins > 50:
        text = font.render(str("You have completed the game and got all the coins! Congratulations!"), True, RED)
    else: 
        text = font.render(str("You have completed the game! Congratulations!"), True, RED)
    textRect = text.get_rect()
    textRect.center = (500, 500)

    # line two
    text2 = font.render(str("Press 'ESC' to quit"), True, RED)
    textRect2 = text2.get_rect()
    textRect2.center = (500, 600)

    screen.fill(BLACK)
    while closeVictoryScreen == False:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # no option for Player to restart the game
                if event.key == pygame.K_ESCAPE: # closes the game
                    closeVictoryScreen = True
                    done = True

        # opportunity for drawn victory screen        
        screen.blit(text, textRect)
        screen.blit(text2, textRect2)
        pygame.display.flip()

# classes 

class player(pygame.sprite.Sprite):
    def __init__(self, X, Y):
        super().__init__()
        # creates (image of) Player
        self.image = pygame.transform.scale(playerDownImage, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = X
        self.rect.y = Y
        # player starts standing still
        self.xMove = 0
        self.yMove = 0
    
    # getter methods
    def getPlayerX(self):
        return self.rect.x
    def getPlayerY(self):
        return self.rect.y
    
    # setter methods
    def resetPlayerPosition(self):
        self.rect.x = 500
        self.rect.y = 500

    # movement method
    # responsible for moving the Player and switching between maps
    def movement(self, input, map, mapY, mapX, worldX, worldY):
        newX, newY = mapX, mapY # sort of redundant
        if input == 97:  # 'a'
            # swaps image of the Player
            self.image = pygame.transform.scale(playerLeftImage, (100, 100))
            if mapX == 0: # if the Player would leave the current map by moving
                # alters world map coords (swaps map)
                worldX = worldX - 1
                groupReset()
                # corrects Player coords
                newX = 9 - newX
                self.rect.x = 900 - self.rect.x
            else:
                if map[mapY][mapX - 1] in traversableTiles: # is the Player allowed to move into the next tile
                    self.xMove = -100
                    newX -= 1

        elif input == 115:  # 's'
            self.image = pygame.transform.scale(playerDownImage, (100, 100))
            if mapY + 1 == len(map):
                worldY = worldY + 1
                groupReset()
                newY = 9 - newY
                self.rect.y = 900 - self.rect.y
            else:
                if map[mapY + 1][mapX] in traversableTiles:
                    self.yMove = 100
                    newY += 1

        elif input == 100:  # 'd'
            self.image = pygame.transform.scale(playerRightImage, (100, 100))
            if mapX + 1 == len(map[mapY]):
                worldX = worldX + 1
                groupReset()
                newX = 9 - newX
                self.rect.x = 900 - self.rect.x
            else:
                if map[mapY][mapX + 1] in traversableTiles:
                    self.xMove = 100
                    newX += 1

        elif input == 119:  # 'w'
            self.image = pygame.transform.scale(playerUpImage, (100, 100))
            if mapY == 0:
                worldY = worldY - 1
                groupReset()
                newY = 9 - newY
                self.rect.y = 900 - self.rect.y
            else:
                if map[mapY - 1][mapX] in traversableTiles:
                    self.yMove = -100
                    newY -= 1

        # actually moves the Player
        self.rect.x += self.xMove
        self.rect.y += self.yMove

        # instead of the Player moving in a straight line until a new input is given
        # the Player stops moving after moving one tile
        self.xMove = 0
        self.yMove = 0

        # updates global coords
        return newX, newY, worldX, worldY
    
    # determines position and orientation of the sword
    def swordAttack(self, input, enemyGroup, swordGroup):
        # using 'input' is necesary to determine which way the sword is pointing
        if input == 97:  # 'a'
            self.killEnemies(-100, 0, enemyGroup, swordGroup, "horizontal", "left")
        elif input == 115:  # 's'
            self.killEnemies(0, 100, enemyGroup, swordGroup, "vertical", "down")
        elif input == 100:  # 'd'
            self.killEnemies(100, 0, enemyGroup, swordGroup, "horizontal", "right")
        elif input == 119:  # 'w'
            self.killEnemies(0, -100, enemyGroup, swordGroup, "vertical", "up")

    # creates instance of the sword, and eliminates struck enemies
    def killEnemies(self, inputX, inputY, enemyGroup, swordGroup, orientation, direction):
        swordTemp = sword(self.rect.x + inputX, self.rect.y + inputY, orientation, direction)
        swordGroup.add(swordTemp)

        killedEnemies = [] # list of enemies struck by the sword - will only ever be one
        for enemyTemp4 in enemyGroup:
            if swordTemp.rect.colliderect(enemyTemp4.rect):
                killedEnemies.append(enemyTemp4)

        # kills all struck enemies
        for enemyTemp5 in killedEnemies:
            enemyTemp5.kill()
    
    # determines position and orientation of the arrow
    def bowAttack(self, input, arrowGroup):
        if input == 97:  # 'a'
            self.fireArrow(10, 0, "left", "horizontal", arrowGroup)
        elif input == 115:  # 's'
            self.fireArrow(0, 50, "down", "vertical", arrowGroup)
        elif input == 100:  # 'd'
            self.fireArrow(50, 0, "right", "horizontal", arrowGroup)
        elif input == 119:  # 'w'
            self.fireArrow(0, 10, "up", "vertical", arrowGroup)

    # just creates instance of the arrow
    # collision detection is done in the main game loop
    def fireArrow(self, inputX, inputY, direction, orientation, arrowGroup):
        arrowTemp = bullet(self.rect.x + inputX, self.rect.y + inputY, direction, orientation)
        arrowGroup.add(arrowTemp)
        

class tile(pygame.sprite.Sprite):
    def __init__(self, X, Y):
        super().__init__()
        # simple attributes as they will be inherited
        self.image = pygame.transform.scale(tileImage, (100, 100))
        self.rect=self.image.get_rect()
        self.rect.x = X
        self.rect.y = Y

    # getter methods
    # useful for various subclasses
    def getX(self):
        return self.rect.x
    def getY(self):
        return self.rect.y


class sword(pygame.sprite.Sprite):
    def __init__(self, X , Y, orientation, direction):
        super().__init__()
        # creates sword image
        self.image = pygame.transform.scale(swordImage, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = X
        self.rect.y = Y

        # sets which way sword is facing
        if direction == "left":
            self.image = pygame.transform.rotate(self.image, 0)
        if direction == "up":
            self.image = pygame.transform.rotate(self.image, 90)
        elif direction == "left":
            self.image = pygame.transform.rotate(self.image, 180)
        elif direction == "down":
            self.image = pygame.transform.rotate(self.image, 270)

        # lifespan of sword
        self.timer = threading.Timer((1/3), self.cooldown) # singular use of threading library
        self.timer.start()
    
    # timer triggers self-destruction
    def cooldown(self):
        self.kill()


class bullet(pygame.sprite.Sprite):
    def __init__(self, X, Y, direction, orientation):
        super().__init__()
        # orientation makes a difference here (unlike the sword)
        # since the image is not 100 by 100, but smaller at 60 by 60
        if orientation == "horizontal":
            self.image = pygame.transform.scale(arrowImage, (60, 60))
            self.rect=self.image.get_rect()
            # measurements are not absolutely symmetrical, but just look it
            self.rect.x = X - 1
            self.rect.y = Y + 24
        elif orientation == "vertical":
            self.image = pygame.transform.scale(arrowImage, (60, 60))
            self.rect=self.image.get_rect()
            # measurements are not absolutely symmetrical, but just look it
            self.rect.x = X + 24
            self.rect.y = Y - 15

        self.speed = 50 # easier to adjust speed across the entire class if it is a variable

        # determines which way bullet is pointing
        self.direction = direction
        if direction == "left":
            self.image = pygame.transform.rotate(self.image, 0)
        if direction == "up":
            self.image = pygame.transform.rotate(self.image, 90)
        elif direction == "left":
            self.image = pygame.transform.rotate(self.image, 180)
        elif direction == "down":
            self.image = pygame.transform.rotate(self.image, 270)
    # moves bullet - collision done in main game loop
    def movement(self):
        if self.direction == "up":
            self.rect.y -= self.speed
        elif self.direction == "down":
            self.rect.y += self.speed
        elif self.direction == "left":
            self.rect.x -= self.speed
        elif self.direction == "right":
            self.rect.x += self.speed


# proper subclass of tile (unlike enemy)
class chest(tile):
    def __init__(self, X, Y):
        super().__init__(X, Y)
        self.image = pygame.transform.scale(chestImage, (100, 100))
        self.value = random.randint(1, 50)
        self.opened = False
    
    # interacting with chest done in main game loop
    # this is just effect of interacting with chest
    def open(self):
        global coins
        if self.opened == False:
            coins += self.value
            self.opened = True
            self.image.fill(BLACK)

# an easy way to end the game (just interacting with a special chest)
class victory(chest):
    def __init__(self, X, Y):
        super().__init__(X, Y)
    
    # polymorphism!
    def open(self):
        victoryScreen()
            

class enemy(tile):
    def __init__(self, X, Y, g, h):
        super().__init__(X, Y)
        self.image = pygame.transform.scale(enemyImage, (100, 100))
        self.xMove = 0
        self.yMove = 0
        # map coords are important for enemies thanks to pathfinding
        self.mapX = int(X / 100)
        self.mapY = int(Y / 100)

        # A* attributes
        self.distance = g
        self.heuristic = h # is it really a heuristic if it is always 100% accurate?
        self.total = g + h # f
        self.parent = None # parent node
        self.path = [] # will contain optimal route from enemy to the Player

    # getter methods
    def getMapX(self):
        return self.mapX
    def getMapY(self):
        return self.mapY

    # creates a perfect heuristic
    def findHeuristic(self):
        return abs(self.mapX - playerMapX) + abs(self.mapY - playerMapY)

    def aStarMovement(self, map, occupiedNodes):
        unvisitedNodes = []
        startNode = node(self.mapX, self.mapY, 0, self.findHeuristic()) # starting node must be created before while loop

        # I decided to use a heapq both to challenge myself
        # and since the heapq can very quickly retrieve the smallest data point it contains
        # which happens to be whatever node has the smallest heuristic
        heapq.heappush(unvisitedNodes, (0, node(self.mapX, self.mapY, self.distance, self.heuristic)))

        visitedNodes = set() # a set contains only unique items, and hence won't store any duplicate nodes
        nodes = {(self.mapX, self.mapY): startNode} # node dictionary compatible with tuples

        while unvisitedNodes:
            _, currentNode = heapq.heappop(unvisitedNodes)
            if (currentNode.getX(), currentNode.getY()) == (playerMapX, playerMapY): # has the algorithm found a way to the Player?
                while currentNode:
                    self.path.append((currentNode.getX(), currentNode.getY()))
                    currentNode = currentNode.parent # runs back through the visited nodes that lead to the Player
                self.path.reverse() # necesary since self.path will be popped to find the next node to move to
                return self.path
            
            # being placed in visitedNodes means the pathfinding algorithm doesn't need to visit said node again
            visitedNodes.add((currentNode.getX(), currentNode.getY()))
            
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]: # all four directions
                nx, ny = currentNode.getX() + dx, currentNode.getY() + dy # adjacent nodes
                if 0 <= nx < 10 and 0 <= ny < 10 and map[ny][nx] == 0 and (nx, ny) not in visitedNodes and (nx, ny) not in occupiedNodes: # can this potential node be moved to?
                    # data needed for comparison
                    g = currentNode.g + 1
                    h = self.findHeuristic()
                    neighbour = node(nx, ny, g, h)

                    if (nx, ny) in nodes: # only discovered nodes (i.e. in dictionary) can be updated
                        if g < neighbour.getG(): # checks if new path to the current node is shorter than the pre-existing one
                            neighbour.setG(g)
                            neighbour.setParent(currentNode)
                    else: # if not a logged node, the node is logged
                        neighbour.setParent(currentNode)
                        nodes[(nx, ny)] = neighbour
                        heapq.heappush(unvisitedNodes, (neighbour.getTotal(), neighbour)) # new node added to heapq

    def findPath(self, map):
        # ensures that enemies won't try to move through each other
        occupiedNodes = []
        for enemyTemp3 in enemyGroup: 
            occupiedNodes.append((enemyTemp3.getMapX(), enemyTemp3.getMapY()))
        
        # executes the pathfinding algorithm to create the path from enemy to the Player
        self.path = enemy.aStarMovement(self, map, occupiedNodes)

    # if the enemy touches the Player, the Player loses the game
    # this method is run every cycle of the game loop, as part of .move()
    def playerDestruction(self):
        if (self.mapX, self.mapY) == (playerMapX, playerMapY):
            gameOver()
    
    # uses the self.path generated to move the enemy closer to the Player
    def move(self):
        if self.path:
            self.mapX, self.mapY = self.path.pop(1)
            self.rect.x = self.mapX * 100
            self.rect.y = self.mapY * 100
        self.playerDestruction()
        
class boss(enemy):
    def __init__(self, X, Y, g, h, lives):
        super().__init__(X, Y, g, h)
        # boss has different image and is of a different size 
        self.image = pygame.transform.scale(bossImage, (200, 200))
        
        # I would have liked to add more to the boss class
        # Great spot for future development

class node():
    def __init__(self, x, y, g, h):
        # coords
        self.x = x
        self.y = y
        # A* data
        self.g = g
        self.h = h
        self.parent = None

    # getter methods
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getG(self):
        return self.g
    def getTotal(self):
        return self.g + self.h
    
    # setter methods
    def setG(self, newG):
        self.g = newG
    def setParent(self, newParent):
        self.parent = newParent

    # automatic comparison required by the heapq library
    # in order to compare the nodes
    def __lt__(self, other):
        return self.getTotal() < other.getTotal()
    
# used for reference
#class template(pygame.sprite.Sprite):
    #def __init__(self, XCoord, YCoord):
        #super().__init__()
        #self.image = pygame.Surface([100, 100])
        #self.image.fill(WHITE)
        #self.rect=self.image.get_rect()
        #self.rect.x = XCoord
        #self.rect.y = YCoord
    

# global variables 
tempKey = None
coins = 0 

# sprite groups
playerGroup = pygame.sprite.Group()

tileGroup = pygame.sprite.Group()

enemyGroup = pygame.sprite.Group()

swordGroup = pygame.sprite.Group()

arrowGroup = pygame.sprite.Group()

chestGroup = pygame.sprite.Group()

bossGroup = pygame.sprite.Group()


# maps, coordinates and instantiation

# starting coordinates of player
playerMapX = 5
playerMapY = 5

# list of symbols that correspond to tiles that the player can travel through
traversableTiles = [0, 2, 3, 4, 5, 6,"P"]
# list of symbols that correspond to tiles that the player cannot travel through
# nonTraversableTiles = [1]
# above isn't actually needed, since I can just see what's not in traversableTiles

 
# starting map 
# 3, 3
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

# 2, 3
map2 = [[1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
        [1, 0, 4, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 1, 1, 1, 0, 0, 0, 1],
        [1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 1, 0, 1, 1, 1, 1, 1],]

# 4, 3
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

# 3, 4
map4 = [[1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
        [1, 1, 0, 0, 0, 0, 1, 1, 3, 1],
        [1, 1, 0, 1, 0, 1, 1, 0, 0, 1],
        [1, 0, 0, 1, 1, 1, 1, 0, 0, 1],
        [1, 0, 0, 1, 4, 0, 0, 0, 1, 1],
        [1, 0, 0, 1, 1, 0, 0, 0, 1, 1],
        [1, 1, 0, 1, 1, 1, 1, 0, 0, 1],
        [1, 1, 0, 0, 1, 1, 1, 0, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],]

# 3, 2
map5 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 0, 1, 0, 1, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 3, 0, 1],
        [1, 1, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 3, 0, 0, 0, 0, 1, 1, 1, 1],
        [1, 1, 0, 0, 0, 0, 1, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],]

# 2, 4
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

# 4, 4
map7 = [[1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 1, 1, 0, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 3, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],]

# 2, 2
map8 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 4, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 1, 3, 1, 1],
        [0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 4, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
        [0, 0, 0, 3, 0, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],]

# 1, 2
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

# 1, 3
map10 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
        [1, 3, 0, 0, 0, 0, 1, 1, 1, 1],
        [1, 0, 1, 0, 1, 0, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 1, 1, 1, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 1, 0, 1, 0, 1, 0, 1],]

# 1, 4
map11 = [[1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 3, 1, 1, 1, 1, 0, 0],
        [1, 0, 1, 0, 0, 0, 0, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],]

# 1, 5
map12 = [[1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 0, 1, 1, 0, 1],
        [1, 0, 1, 1, 0, 0, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 4, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 0, 1, 1, 0, 1],
        [1, 3, 1, 1, 0, 0, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],]

# 2, 5
map13 = [[1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 3, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 4, 1],
        [1, 1, 0, 0, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 0, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 3, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],]

# 3, 5
map14 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
        [0, 0, 0, 3, 1, 1, 3, 0, 0, 0],
        [1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],]

# 4, 5
map15 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 4, 3, 1, 0, 1],
        [0, 0, 1, 0, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],]

# 5, 4
map16 = [[1, 1, 1, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 1, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
        [1, 1, 3, 0, 0, 0, 0, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
        [1, 1, 3, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 1, 0, 0, 0, 0, 0, 1, 1],]

# 5, 5
map17 = [[1, 1, 1, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 1, 3, 0, 0, 0, 0, 1, 1],
        [1, 1, 1, 1, 1, 1, 0, 0, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],]

# 5, 3
map18 = [[1, 1, 0, 0, 0, 1, 1, 1, 1, 1],
        [1, 1, 0, 0, 0, 1, 1, 1, 3, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 4, 1, 1, 1, 1],
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 3, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 0, 0, 0, 0, 1, 1],]

# 4, 2
map19 = [[1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 1, 0, 0, 0, 0],
        [1, 0, 1, 0, 3, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 1, 1],
        [0, 0, 0, 4, 1, 1, 1, 0, 1, 1],
        [1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 0, 0, 1],]

# 5, 2
map20 = [[1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 0, 0, 1, 1],
        [0, 1, 0, 0, 0, 1, 0, 0, 1, 1],
        [0, 0, 0, 1, 0, 0, 0, 0, 1, 1],
        [1, 1, 1, 1, 1, 1, 0, 0, 1, 1],
        [1, 1, 1, 3, 0, 1, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 1, 1, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 1, 0, 1, 1],
        [1, 1, 0, 0, 0, 1, 1, 1, 1, 1],]

# 5, 1
map21 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 3, 0, 0, 1, 1],
        [1, 1, 1, 1, 0, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 3, 1, 1, 1, 1, 0, 1, 1],
        [1, 0, 0, 1, 0, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 0, 0, 0, 1],]

# 4, 1
map22 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 0, 0, 1, 1, 0, 0, 0, 0],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
        [1, 0, 0, 3, 0, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 0, 1, 1, 0, 1, 1],
        [1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
        [1, 1, 0, 0, 1, 1, 0, 0, 1, 1],]

# 3, 1
map23 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
        [1, 1, 3, 1, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 4, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 1, 1, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],]

# 2, 1
map24 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 3, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 0, 1, 1, 0, 1],
        [1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
        [1, 1, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 1, 1, 0, 1],
        [1, 0, 1, 1, 0, 0, 1, 1, 0, 1],
        [1, 0, 0, 3, 0, 0, 1, 3, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],]

# 1, 1
mapBoss = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 6, 0, 5, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],]

# -, -
# mapTemplate = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],]


# world map
# contains all of the other maps
worldMap = [[mapBoss, map24, map23, map22, map21],
            [map9, map8, map5, map19, map20],
            [map10, map2, map1, map3, map18],
            [map11, map6, map4, map7, map16], 
            [map12, map13, map14, map15, map17],]

# coords of current map
worldMapX = 2
worldMapY = 2

# check if current map needs to be changed
# used in the main game loop
tempWorldMapX = 0
tempWorldMapY = 0

# what map to create referenced from world map using world map coords
def generateMap(map, tempPlayer, tileGroup, playerGroup):
    mapXCoord = 0
    mapYCoord = 0

    for i in map:
        for j in i:
            # each symbol featured on the regular maps refers to a certain class of object
            if j == 1:
                tileTemp = tile(mapXCoord, mapYCoord)
                tileGroup.add(tileTemp)
            if j == "P":
                #tempPlayer = player(mapXCoord, mapYCoord)
                playerGroup.add(tempPlayer)
            if j == 3:
                enemyTemp = enemy(mapXCoord, mapYCoord, 0, 0)
                tileGroup.add(enemyTemp)
                enemyGroup.add(enemyTemp)
            if j == 4:
                chestTemp = chest(mapXCoord, mapYCoord)
                tileGroup.add(chestTemp)
                chestGroup.add(chestTemp)
            if j == 5:
                bossTemp = boss(mapXCoord, mapYCoord, 0, 0, 3)
                tileGroup.add(bossTemp)
                enemyGroup.add(bossTemp)
                bossGroup.add(bossTemp)
            if j == 6:
                victoryTemp = victory(mapXCoord, mapYCoord)
                tileGroup.add(victoryTemp)
                chestGroup.add(victoryTemp)
            # if j == :... etc.
            mapXCoord += 100
        mapYCoord += 100
        mapXCoord = 0

    return tileGroup, playerGroup, tileTemp, tempPlayer, enemyGroup, chestGroup, bossGroup # all groups included here

# deletes EVERYTHING other than the Player
def groupReset(): 
    groups = [tileGroup, arrowGroup]
    for group in groups:
        for sprite in group.sprites():
            # whether objects are removed their object groups is irrelevant
            sprite.kill()

# creates the one and only instance of the Player
PLAYER = player(500, 500)
# creates first map
generateMap(map1, PLAYER, tileGroup, playerGroup)


# game loop
done = False
clock = pygame.time.Clock()

startMenu() # loads start menu before main game can begin
while not done:
    # input detection
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        # key inputs
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: # open settings
                openSettings()
            if event.key == pygame.K_e: # sword attack
                PLAYER.swordAttack(tempKey, enemyGroup, swordGroup)
            if event.key == pygame.K_q: # bow attack
                PLAYER.bowAttack(tempKey, arrowGroup)
            if event.key == pygame.K_f: # open chest
                for chestTemp2 in chestGroup:
                    if (chestTemp2.getX(), chestTemp2.getY()) == (playerMapX * 100, playerMapY * 100):
                        chestTemp2.open()
                
            # movement

            # used later to check if a new map should be generated
            tempWorldMapX = worldMapX
            tempWorldMapY = worldMapY

            # main movement method
            # the Player has to move for any other object to move automatically
            playerMapX, playerMapY, worldMapX, worldMapY = PLAYER.movement(event.key, worldMap[worldMapY][worldMapX], playerMapY, playerMapX, worldMapX, worldMapY)

            # moves all enemies
            for enemyTemp2 in enemyGroup:
                enemyTemp2.findPath(worldMap[worldMapY][worldMapX])
                enemyTemp2.move()

            # sword collision algorithm in main game loop
            killedEnemies = []
            for enemyTemp4 in enemyGroup:
                for swordTemp in swordGroup:
                    if swordTemp.rect.colliderect(enemyTemp4.rect):
                        killedEnemies.append(enemyTemp4)
                for enemyTemp5 in killedEnemies:
                    enemyTemp5.kill()
                    coins += random.randint(1, 10)
            
            # arrow collision algorithm in main game loop
            for arrowTemp in arrowGroup:
                arrowTemp.movement()
                # if arrow leaves the screen, arrow is deleted
                if not arrowTemp.rect.colliderect(screen.get_rect()):
                    arrowTemp.kill()

                # if arrow collides with an enemy, arrow and enemy are deleted
                for enemyTemp6 in enemyGroup:
                    if arrowTemp.rect.colliderect(enemyTemp6.rect):
                        arrowTemp.kill()
                        enemyTemp6.kill()
                        coins += random.randint(1, 5)
                
                # if arrow collides with tile (other than enemy), arrow is deleted
                for tileTemp2 in tileGroup:
                    if arrowTemp.rect.colliderect(tileTemp2.rect):
                        arrowTemp.kill()

            # again, checks to see if new map should be generated
            if tempWorldMapX != worldMapX or tempWorldMapY != worldMapY:
                generateMap(worldMap[worldMapY][worldMapX], PLAYER, tileGroup, playerGroup)
            tempKey = event.key
            
    # drawing
    
    # background colour
    screen.fill(BLACK)

    # draws all objects in object groups
    tileGroup.draw(screen)
    playerGroup.draw(screen)
    swordGroup.draw(screen)
    arrowGroup.draw(screen)
    bossGroup.draw(screen)

    # end of game loop
    pygame.display.flip()
    clock.tick(60)