import pygame
import os
import time
import random

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 30

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Player Pokemon
player_pokemon = {"name": "Pikachu", "level": 10, "max_health": 50, "current_health": 50, "attack": 10}

# Enemy Pokemon
enemy_pokemon = {"name": "Charmander", "level": 8, "max_health": 40, "current_health": 40, "attack": 8}

# Initialize Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pokemon Battle Simulator")
clock = pygame.time.Clock()

# Fonts
font = pygame.font.SysFont(None, 36)

# Function to display text on the screen
def display_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Game loop
def battle():
    global player_pokemon, enemy_pokemon

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            

        # Player action
        display_text("Choose an action:", BLACK, 20, 450)
        pygame.draw.rect(screen, RED, (20, 500, 150, 50))  # Attack button
        display_text("Attack", WHITE, 70, 510)

        pygame.display.flip()

        player_action = None
        waiting_for_input = True
        while waiting_for_input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if 20 <= x <= 170 and 500 <= y <= 550:
                        player_action = "Attack"
                        waiting_for_input = False

        # Enemy action
        enemy_action = random.choice(["Attack"])

        # Resolve actions
        if player_action == "Attack":
            damage = player_pokemon["attack"] * player_pokemon["level"]
            enemy_pokemon["current_health"] -= damage

        # Check if the battle is over
        if enemy_pokemon["current_health"] <= 0:
            display_text(f"You defeated {enemy_pokemon['name']}!", BLACK, 20, 200)
            pygame.display.flip()
            pygame.time.delay(2000)  # Delay for 2 seconds
            reset_game()

        if player_pokemon["current_health"] <= 0:
            display_text(f"{player_pokemon['name']} fainted!", BLACK, 20, 200)
            pygame.display.flip()
            pygame.time.delay(2000)  # Delay for 2 seconds
            reset_game()

        # Display current stats
        screen.fill(WHITE)
        display_text(f"{player_pokemon['name']} - Level {player_pokemon['level']}", BLACK, 20, 20)
        display_text(f"Health: {player_pokemon['current_health']}/{player_pokemon['max_health']}", BLACK, 20, 60)
        display_text(f"{enemy_pokemon['name']} - Level {enemy_pokemon['level']}", BLACK, 20, 120)
        display_text(f"Health: {enemy_pokemon['current_health']}/{enemy_pokemon['max_health']}", BLACK, 20, 160)

        pygame.display.flip()
        clock.tick(FPS)

# Function to reset the game state
def reset_game():
    global player_pokemon, enemy_pokemon

    player_pokemon["current_health"] = player_pokemon["max_health"]
    enemy_pokemon["current_health"] = enemy_pokemon["max_health"]
    battle()

# Start the battle
battle()