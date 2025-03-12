def gameOver():
    font = pygame.font.SysFont('arial', 32)
    text = font.render(str("Press 'R' to retry"), True, RED)
    textRect = text.get_rect()
    textRect.center = (500, 400)
    text2 = font.render(str("Press 'ESC' to quit"), True, RED)
    textRect2 = text2.get_rect()
    textRect2.center = (500, 600)

    while closeGameOver == False:
        global done
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_R:
                    for playerTemp in playerGroup:
                        playerTemp.resetPlayerPosition()
                        playerMapX, playerMapY, worldMapX, worldMapY  = 5, 5
                    generateMap(worldMap[worldMapY][worldMapX], PLAYER, tileGroup, playerGroup)
                if event.key == pygame.K_ESCAPE:
                    closeGamerOver = True
                    done = True
        screen.fill(BLACK)
        screen.blit(text, textRect, text2, textRect2)
        pygame.display.flip()