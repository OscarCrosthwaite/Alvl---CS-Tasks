import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Strategy Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Clock and FPS
clock = pygame.time.Clock()
FPS = 30

# Fonts
font = pygame.font.Font(None, 36)

# Game variables
TILE_SIZE = 50
GRID_WIDTH = WIDTH // TILE_SIZE
GRID_HEIGHT = HEIGHT // TILE_SIZE

# Units
units = []
base_health = 100
defense_positions = []

# Enemy waves
wave = 1
enemy_units = []

# Resources
resources = 100

# Define unit and enemy classes
class Unit:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = GREEN
        self.attack_power = 10
        self.range = 3

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x * TILE_SIZE, self.y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    def attack(self):
        for enemy in enemy_units[:]:
            distance = abs(self.x - enemy.x) + abs(self.y - enemy.y)
            if distance <= self.range:
                enemy.health -= self.attack_power
                if enemy.health <= 0:
                    enemy_units.remove(enemy)
                break

class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = RED
        self.health = 50

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x * TILE_SIZE, self.y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    def move(self):
        if self.y < GRID_HEIGHT - 1:
            self.y += 1
        else:
            global base_health
            base_health -= 10
            enemy_units.remove(self)

# Draw grid
def draw_grid():
    for x in range(0, WIDTH, TILE_SIZE):
        pygame.draw.line(screen, WHITE, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, TILE_SIZE):
        pygame.draw.line(screen, WHITE, (0, y), (WIDTH, y))

# Spawn enemies for each wave
def spawn_enemies(wave):
    for _ in range(wave * 2):
        x = random.randint(0, GRID_WIDTH - 1)
        enemy_units.append(Enemy(x, 0))

# Main game loop
running = True
spawn_enemies(wave)
while running:
    screen.fill(BLACK)
    draw_grid()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and resources >= 10:
            mx, my = pygame.mouse.get_pos()
            grid_x, grid_y = mx // TILE_SIZE, my // TILE_SIZE
            units.append(Unit(grid_x, grid_y))
            resources -= 10

    # Draw and update units
    for unit in units:
        unit.draw()
        unit.attack()

    # Draw and update enemies
    for enemy in enemy_units:
        enemy.draw()
        enemy.move()

    # Display base health and resources
    base_text = font.render(f"Base Health: {base_health}", True, WHITE)
    resources_text = font.render(f"Resources: {resources}", True, WHITE)
    wave_text = font.render(f"Wave: {wave}", True, WHITE)
    screen.blit(base_text, (10, 10))
    screen.blit(resources_text, (10, 40))
    screen.blit(wave_text, (10, 70))

    # Check game over
    if base_health <= 0:
        game_over_text = font.render("Game Over!", True, RED)
        screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2))
        pygame.display.flip()
        pygame.time.wait(3000)
        running = False

    # Check if wave is cleared
    if not enemy_units:
        wave += 1
        resources += 50
        spawn_enemies(wave)

    # Update display
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
