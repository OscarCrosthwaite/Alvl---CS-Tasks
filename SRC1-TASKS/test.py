import pygame
done = False
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
size = (1000, 1000)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("TEMP NAME")

while not done:
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True

    screen.fill(BLACK)
    pygame.display.flip()
    clock.tick(60)