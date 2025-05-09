import pygame

def set_background(WINDOW_WIDTH, WINDOW_HEIGHT):
    background = pygame.image.load('Assets\main_background.jpg')
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    background = pygame.transform.scale(background, (WINDOW_WIDTH, WINDOW_HEIGHT))
    screen.blit(background, (0, 0))
    return screen, background

def read_move(player_pos, player_radius, player_speed, keys, WINDOW_WIDTH, WINDOW_HEIGHT):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LSHIFT]:
        if keys[pygame.K_LEFT] and player_pos[0] - player_radius > 0:
            player_pos[0] -= player_speed-2
        if keys[pygame.K_RIGHT] and player_pos[0] + player_radius < WINDOW_WIDTH:
            player_pos[0] += player_speed-2
        if keys[pygame.K_UP] and player_pos[1] - player_radius > 0:
            player_pos[1] -= player_speed-2
        if keys[pygame.K_DOWN] and player_pos[1] + player_radius < WINDOW_HEIGHT:
            player_pos[1] += player_speed-2

    else:
        if keys[pygame.K_LEFT] and player_pos[0] - player_radius > 0:
            player_pos[0] -= player_speed 
        if keys[pygame.K_RIGHT] and player_pos[0] + player_radius < WINDOW_WIDTH:
            player_pos[0] += player_speed
        if keys[pygame.K_UP] and player_pos[1] - player_radius > 0:
            player_pos[1] -= player_speed
        if keys[pygame.K_DOWN] and player_pos[1] + player_radius < WINDOW_HEIGHT:
            player_pos[1] += player_speed

    return player_pos

def show_position(screen, player_pos):
    font = pygame.font.Font(None, 36)
    coord_text = font.render(f'X: {int(player_pos[0])}, Y: {int(player_pos[1])}', True, (255, 255, 255))
    screen.blit(coord_text, (10, 10))
