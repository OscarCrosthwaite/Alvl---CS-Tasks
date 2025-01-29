import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Clock and FPS
clock = pygame.time.Clock()
FPS = 60

# Fonts
font = pygame.font.Font(None, 36)

# Player properties
player_width, player_height = 50, 50
player_x = WIDTH // 2
player_y = HEIGHT - player_height - 10
player_speed = 5
player_color = GREEN
player_vel_y = 0
player_jump = -15
player_gravity = 0.8
is_jumping = False

# Platform properties
platforms = [
    pygame.Rect(0, HEIGHT - 20, WIDTH, 20),  # Ground
    pygame.Rect(200, 450, 150, 20),
    pygame.Rect(400, 350, 150, 20),
    pygame.Rect(100, 250, 150, 20),
    pygame.Rect(300, 150, 150, 20)
]
platform_color = BLUE

# Collectible properties
collectibles = []
collectible_size = 20
collectible_color = YELLOW
for _ in range(5):
    x = random.randint(50, WIDTH - collectible_size - 50)
    y = random.randint(50, HEIGHT - collectible_size - 50)
    collectibles.append(pygame.Rect(x, y, collectible_size, collectible_size))

# Enemy properties
enemies = []
enemy_size = 30
enemy_color = RED
enemy_speed = 3
for _ in range(3):
    x = random.randint(0, WIDTH - enemy_size)
    y = random.randint(0, HEIGHT // 2)
    enemies.append(pygame.Rect(x, y, enemy_size, enemy_size))

# Score and levels
score = 0
level = 1

# Function to draw text
def draw_text(surface, text, font, color, x, y):
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, (x, y))

# Function to handle player movement
def handle_player_movement(keys, player_rect):
    global is_jumping, player_vel_y
    if keys[pygame.K_LEFT] and player_rect.x > 0:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT] and player_rect.x < WIDTH - player_width:
        player_rect.x += player_speed

    # Jump logic
    if keys[pygame.K_SPACE] and not is_jumping:
        player_vel_y = player_jump
        is_jumping = True

# Function to check for collisions with platforms
def handle_platform_collision(player_rect):
    global is_jumping, player_vel_y
    player_rect.y += player_vel_y
    player_vel_y += player_gravity

    for platform in platforms:
        if player_rect.colliderect(platform) and player_vel_y > 0:
            player_rect.y = platform.y - player_height
            player_vel_y = 0
            is_jumping = False
            break

# Function to handle enemies
def move_enemies():
    for enemy in enemies:
        enemy.y += enemy_speed
        if enemy.y > HEIGHT:
            enemy.y = random.randint(-100, -40)
            enemy.x = random.randint(0, WIDTH - enemy_size)

def check_enemy_collision(player_rect):
    global running
    for enemy in enemies:
        if player_rect.colliderect(enemy):
            draw_text(screen, "Game Over!", font, RED, WIDTH // 2 - 100, HEIGHT // 2)
            pygame.display.flip()
            pygame.time.wait(3000)
            running = False

# Main game loop
running = True
player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
while running:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    handle_player_movement(keys, player_rect)
    handle_platform_collision(player_rect)

    # Enemy movement
    move_enemies()
    check_enemy_collision(player_rect)

    # Check for collectible collisions
    for collectible in collectibles[:]:
        if player_rect.colliderect(collectible):
            collectibles.remove(collectible)
            score += 1

    # Level up logic
    if not collectibles:
        level += 1
        for _ in range(5):
            x = random.randint(50, WIDTH - collectible_size - 50)
            y = random.randint(50, HEIGHT - collectible_size - 50)
            collectibles.append(pygame.Rect(x, y, collectible_size, collectible_size))
        for _ in range(level):
            x = random.randint(0, WIDTH - enemy_size)
            y = random.randint(-100, -40)
            enemies.append(pygame.Rect(x, y, enemy_size, enemy_size))

    # Draw platforms
    for platform in platforms:
        pygame.draw.rect(screen, platform_color, platform)

    # Draw collectibles
    for collectible in collectibles:
        pygame.draw.rect(screen, collectible_color, collectible)

    # Draw enemies
    for enemy in enemies:
        pygame.draw.rect(screen, enemy_color, enemy)

    # Draw player
    pygame.draw.rect(screen, player_color, player_rect)

    # Draw score and level
    draw_text(screen, f"Score: {score}", font, WHITE, 10, 10)
    draw_text(screen, f"Level: {level}", font, WHITE, 10, 50)

    # Update display
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
 