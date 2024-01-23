import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
PLAYER_SIZE = 50
BLOCK_SIZE = 50
FPS = 60

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Pygame Game")

# Player
player_x = (WIDTH - PLAYER_SIZE) // 2
player_y = HEIGHT - PLAYER_SIZE - 10
player_speed = 5

# Bullets
bullet_speed = 7
bullets = []

# Blocks
blocks = []

def draw_player(x, y):
    pygame.draw.rect(screen, WHITE, [x, y, PLAYER_SIZE, PLAYER_SIZE])

def draw_bullet(x, y):
    pygame.draw.rect(screen, BLUE, [x, y, 5, 10])

def draw_block(x, y):
    pygame.draw.rect(screen, RED, [x, y, BLOCK_SIZE, BLOCK_SIZE])

def collision_check(bullet_x, bullet_y, block_x, block_y):
    return block_x < bullet_x < block_x + BLOCK_SIZE and block_y < bullet_y < block_y + BLOCK_SIZE

# Game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - PLAYER_SIZE:
        player_x += player_speed

    # Shooting bullets
    if keys[pygame.K_SPACE]:
        bullets.append([player_x + PLAYER_SIZE // 2, player_y])

    # Move bullets
    bullets = [[bx, by - bullet_speed] for bx, by in bullets]

    # Spawn new blocks
    if random.randint(1, 50) <= 7:
        blocks.append([random.randint(0, WIDTH - BLOCK_SIZE), 0])

    # Move blocks
    blocks = [[bx, by + 2] for bx, by in blocks]

    # Check for collisions
    for bullet in bullets:
        for block in blocks:
            if collision_check(bullet[0], bullet[1], block[0], block[1]):
                bullets.remove(bullet)
                blocks.remove(block)

    # Draw everything
    screen.fill((0, 0, 0))

    draw_player(player_x, player_y)

    for bullet in bullets:
        draw_bullet(bullet[0], bullet[1])

    for block in blocks:
        draw_block(block[0], block[1])

    pygame.display.flip()
    clock.tick(FPS)