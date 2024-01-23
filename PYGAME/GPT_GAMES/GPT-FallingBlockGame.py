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
GREEN = (0, 255, 0)

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
min_obstacle_distance = 2 * PLAYER_SIZE  # Minimum distance between obstacles

# Power-up variables
power_up_active = False
power_up_duration = 5000  # in milliseconds
power_up_end_time = 0

# Score variables
score = 0
font = pygame.font.SysFont(None, 36)

# Define different shapes for obstacles
shapes = [
    pygame.Rect(0, 0, PLAYER_SIZE, PLAYER_SIZE),
    pygame.Rect(0, 0, PLAYER_SIZE * 2, PLAYER_SIZE),
    pygame.Rect(0, 0, PLAYER_SIZE // 2, PLAYER_SIZE * 2),
    # Add more shapes as needed
]

def draw_elements():
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, player)

    for obstacle in obstacle_list:
        pygame.draw.rect(screen, RED, obstacle)

    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    if power_up_active:
        pygame.draw.rect(screen, GREEN, player)

def create_obstacle():
    shape = random.choice(shapes)
    x = random.randint(0, WIDTH - shape.width)
    y = -shape.height
    obstacle = pygame.Rect(x, y, shape.width, shape.height)
    
    # Ensure minimum distance between obstacles
    while any(obstacle.colliderect(existing_obstacle) for existing_obstacle in obstacle_list):
        obstacle.y -= min_obstacle_distance
    
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

def activate_power_up():
    global player, power_up_active, power_up_end_time
    original_size = player.size
    player.size = (PLAYER_SIZE // 2, PLAYER_SIZE // 2)  # Make the player smaller
    power_up_active = True
    power_up_end_time = pygame.time.get_ticks() + power_up_duration
    pygame.time.set_timer(pygame.USEREVENT, power_up_duration)  # Set a timer event to revert the size back

def deactivate_power_up():
    global player, power_up_active
    player.size = (PLAYER_SIZE, PLAYER_SIZE)  # Reset the player's size to normal
    power_up_active = False

def game_over():
    screen.fill(WHITE)
    game_over_text = font.render(f"Game Over! Your score: {score}", True, (0, 0, 0))
    screen.blit(game_over_text, (WIDTH // 2 - 150, HEIGHT // 2 - 20))
    pygame.display.flip()
    pygame.time.wait(2000)  # Display game over for 2 seconds

# Outer game loop
while True:
    # Reset variables for a new game
    player = pygame.Rect(WIDTH // 2 - PLAYER_SIZE // 2, HEIGHT - 2 * PLAYER_SIZE, PLAYER_SIZE, PLAYER_SIZE)
    obstacle_list = []
    score = 0
    running = True
    power_up_active = False
    power_up_end_time = 0

    

    # Inner game loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.USEREVENT and power_up_active:
                deactivate_power_up()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - player_speed > 0:
            player.x -= player_speed
        if keys[pygame.K_RIGHT] and player.x + player_speed < WIDTH - player.width:
            player.x += player_speed

        screen.fill(WHITE)

        if random.randint(1, 100) < 2 and not power_up_active:
            activate_power_up()

        if power_up_active and pygame.time.get_ticks() > power_up_end_time:
            deactivate_power_up()

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

    game_over()