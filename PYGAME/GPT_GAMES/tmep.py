import pygame
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)

# Physics variables
gravity = 0.5
bike_speed = 0
bike_rotation = 0
bike_x, bike_y = 200, 300
bike_vy = 0
max_speed = 5  # Limit max speed
friction = 0.05  # Reduce speed over time

# Create track with more segments
def create_track():
    track_points = []
    for i in range(50):  # Extended the track length
        x = i * 80
        y = random.randint(300, 500)
        track_points.append((x, y))
    return track_points

track = create_track()

def get_track_height(x):
    for i in range(len(track) - 1):
        x1, y1 = track[i]
        x2, y2 = track[i + 1]
        if x1 <= x <= x2:
            # Linear interpolation to find the y value at the bike's x position
            t = (x - x1) / (x2 - x1)
            return y1 + t * (y2 - y1)
    return HEIGHT  # Default to ground level if out of bounds

running = True
while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        bike_speed = min(bike_speed + 0.2, max_speed)
    if keys[pygame.K_LEFT]:
        bike_speed = max(bike_speed - 0.2, -max_speed)
    
    # Apply friction
    if bike_speed > 0:
        bike_speed -= friction
    elif bike_speed < 0:
        bike_speed += friction
    
    # Apply gravity
    bike_vy += gravity
    bike_y += bike_vy
    bike_x += bike_speed
    
    # Collision detection with track
    track_y = get_track_height(bike_x)
    if bike_y >= track_y - 20:  # Adjusted to keep the bike on track
        bike_y = track_y - 20
        bike_vy = 0  # Stop falling
    
    # Camera offset to follow the bike
    offset_x = max(0, bike_x - WIDTH // 2)
    
    # Draw bike
    bike_rect = pygame.Rect(int(bike_x - offset_x), int(bike_y), 50, 20)
    pygame.draw.rect(screen, CYAN, bike_rect)
    
    # Draw track
    for i in range(len(track) - 1):
        x1, y1 = track[i]
        x2, y2 = track[i + 1]
        pygame.draw.line(screen, WHITE, (x1 - offset_x, y1), (x2 - offset_x, y2), 5)
    
    pygame.display.flip()
    clock.tick(50)

pygame.quit()