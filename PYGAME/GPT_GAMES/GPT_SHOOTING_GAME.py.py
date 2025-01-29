import pygame
import random
import math

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Alien Dodger")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Clock and FPS
clock = pygame.time.Clock()
FPS = 60

# Fonts
font = pygame.font.Font(None, 36)

# Player properties
player_size = 50
player_x = WIDTH // 2
player_y = HEIGHT - player_size - 10
player_speed = 7
player_color = GREEN

# Alien properties
alien_size = 50
alien_speed = 3
alien_color = RED
max_aliens = 10

# Bullet properties
bullet_width = 5
bullet_height = 10
bullet_speed = 10
bullet_color = BLUE

# Score and lives
score = 0
lives = 3

# Game states
aliens = []
bullets = []

# Function to spawn aliens
def spawn_alien():
    x = random.randint(0, WIDTH - alien_size)
    y = random.randint(-150, -50)
    aliens.append([x, y])

# Function to draw text
def draw_text(surface, text, font, color, x, y):
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, (x, y))

# Main game loop
running = True
while running:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed
    if keys[pygame.K_SPACE]:
        if len(bullets) < 5:  # Limit bullets
            bullets.append([player_x + player_size // 2, player_y])

    # Update alien positions
    for alien in aliens:
        alien[1] += alien_speed
        if alien[1] > HEIGHT:
            aliens.remove(alien)
            lives -= 1

    # Update bullet positions
    for bullet in bullets:
        bullet[1] -= bullet_speed
        if bullet[1] < 0:
            bullets.remove(bullet)

    # Collision detection
    for alien in aliens[:]:
        alien_rect = pygame.Rect(alien[0], alien[1], alien_size, alien_size)
        for bullet in bullets[:]:
            bullet_rect = pygame.Rect(bullet[0], bullet[1], bullet_width, bullet_height)
            if alien_rect.colliderect(bullet_rect):
                aliens.remove(alien)
                bullets.remove(bullet)
                score += 1
                break

    # Spawn aliens
    if len(aliens) < max_aliens and random.random() < 0.02:
        spawn_alien()

    # Draw player
    pygame.draw.rect(screen, player_color, (player_x, player_y, player_size, player_size))

    # Draw aliens
    for alien in aliens:
        pygame.draw.rect(screen, alien_color, (alien[0], alien[1], alien_size, alien_size))

    # Draw bullets
    for bullet in bullets:
        pygame.draw.rect(screen, bullet_color, (bullet[0], bullet[1], bullet_width, bullet_height))

    # Draw score and lives
    draw_text(screen, f"Score: {score}", font, WHITE, 10, 10)
    draw_text(screen, f"Lives: {lives}", font, WHITE, 10, 50)

    # Check for game over
    if lives <= 0:
        draw_text(screen, "Game Over", font, RED, WIDTH // 2 - 100, HEIGHT // 2)
        pygame.display.flip()
        pygame.time.wait(3000)
        running = False

    # Update display
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
