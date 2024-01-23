import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Player constants
PLAYER_SIZE = 20
PLAYER_COLOR = (0, 255, 0)
PLAYER_SPEED = 5

# Maze constants
MAZE_SIZE = 20
MAZE_CELL_SIZE = WIDTH // MAZE_SIZE
MAZE_COLOR = (255, 0, 0)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Game")
clock = pygame.time.Clock()

# Player
player = pygame.Rect(0, 0, PLAYER_SIZE, PLAYER_SIZE)

# Maze
maze = [[random.choice([0, 1]) for _ in range(MAZE_SIZE)] for _ in range(MAZE_SIZE)]

# Start and End positions
start_pos = (0, 0)
end_pos = (MAZE_SIZE - 1, MAZE_SIZE - 1)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x - PLAYER_SPEED > 0:
        player.x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT] and player.x + PLAYER_SIZE + PLAYER_SPEED < WIDTH:
        player.x += PLAYER_SPEED
    if keys[pygame.K_UP] and player.y - PLAYER_SPEED > 0:
        player.y -= PLAYER_SPEED
    if keys[pygame.K_DOWN] and player.y + PLAYER_SIZE + PLAYER_SPEED < HEIGHT:
        player.y += PLAYER_SPEED

    # Check collision with maze walls
    player_rect = pygame.Rect(player.x, player.y, PLAYER_SIZE, PLAYER_SIZE)
    for row in range(MAZE_SIZE):
        for col in range(MAZE_SIZE):
            if maze[row][col] == 1:
                maze_rect = pygame.Rect(col * MAZE_CELL_SIZE, row * MAZE_CELL_SIZE, MAZE_CELL_SIZE, MAZE_CELL_SIZE)
                if player_rect.colliderect(maze_rect):
                    # Collision with maze wall
                    player.x, player.y = 0, 0  # Reset player position

    # Check if player reached the end
    if player.x // MAZE_CELL_SIZE == end_pos[0] and player.y // MAZE_CELL_SIZE == end_pos[1]:
        print("Congratulations! You reached the end.")
        running = False

    # Draw everything
    screen.fill(WHITE)

    # Draw maze
    for row in range(MAZE_SIZE):
        for col in range(MAZE_SIZE):
            if maze[row][col] == 1:
                pygame.draw.rect(screen, MAZE_COLOR, (col * MAZE_CELL_SIZE, row * MAZE_CELL_SIZE, MAZE_CELL_SIZE, MAZE_CELL_SIZE))

    # Draw start and end positions
    pygame.draw.rect(screen, (0, 0, 255), (start_pos[0] * MAZE_CELL_SIZE, start_pos[1] * MAZE_CELL_SIZE, MAZE_CELL_SIZE, MAZE_CELL_SIZE))
    pygame.draw.rect(screen, (0, 255, 0), (end_pos[0] * MAZE_CELL_SIZE, end_pos[1] * MAZE_CELL_SIZE, MAZE_CELL_SIZE, MAZE_CELL_SIZE))

    # Draw player
    pygame.draw.rect(screen, PLAYER_COLOR, player)

    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()