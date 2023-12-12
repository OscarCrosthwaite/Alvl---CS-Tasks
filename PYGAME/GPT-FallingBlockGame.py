import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
PLAYER_SIZE = 50
FPS = 60
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodger Game")

clock = pygame.time.Clock()

# Player variables
player = pygame.Rect(WIDTH // 2 - PLAYER_SIZE // 2, HEIGHT - 2 * PLAYER_SIZE, PLAYER_SIZE, PLAYER_SIZE)
player_speed = 5

# Obstacle variables
obstacle_speed = 5
obstacle_list = []

# Score variables
score = 0
font = pygame.font.SysFont(None, 36)

def draw_elements():
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, player)

    for obstacle in obstacle_list:
        pygame.draw.rect(screen, RED, obstacle)

    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

def create_obstacle():
    x = random.randint(0, WIDTH - PLAYER_SIZE)
    y = -PLAYER_SIZE
    obstacle = pygame.Rect(x, y, PLAYER_SIZE, PLAYER_SIZE)
    obstacle_list.append(obstacle)

def move_obstacles():
    for obstacle in obstacle_list:
        obstacle.y += obstacle_speed

def check_collision():
    global score
    for obstacle in obstacle_list:
        if obstacle.colliderect(player):
            return True
    return False

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x - player_speed > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.x + player_speed < WIDTH - PLAYER_SIZE:
        player.x += player_speed

    screen.fill(WHITE)

    if random.randint(1, 100) < 10:
        create_obstacle()

    move_obstacles()

    if check_collision():
        running = False

    obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.y < HEIGHT]

    score += 1

    draw_elements()

    pygame.display.flip()
    clock.tick(FPS)

# Game over screen
screen.fill(WHITE)
game_over_text = font.render(f"Game Over! Your score: {score}", True, (0, 0, 0))
screen.blit(game_over_text, (WIDTH // 2 - 150, HEIGHT // 2 - 20))
pygame.display.flip()

pygame.time.wait(2000)  # Display game over for 2 seconds
pygame.quit()
sys.exit()