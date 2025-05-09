import pygame
from utils import set_background, read_move, show_position
from moviepy import VideoFileClip


pygame.init()
screen_info = pygame.display.Info()
x = screen_info.current_w

WINDOW_WIDTH = (3 * x) // 5 #1536
WINDOW_HEIGHT = (9 * x) // 20 #1152
pygame.display.set_icon(pygame.image.load('Assets\icon.png'))
pygame.display.set_caption("東方風神録2")

screen, background = set_background(WINDOW_WIDTH, WINDOW_HEIGHT)

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

player_pos = [WINDOW_WIDTH // 2, 4*WINDOW_HEIGHT // 5]
player_radius = 5
player_speed = 5

running = True
clock = pygame.time.Clock()
    
while running:

    screen.blit(background, (0, 0))
    pygame.draw.rect(screen, (0, 0, 0), (WINDOW_WIDTH*19//384, WINDOW_HEIGHT*5//144, WINDOW_WIDTH*77//128, WINDOW_HEIGHT*1073//1152))
    player_pos = read_move(player_pos, player_radius, player_speed, pygame.key.get_pressed(), WINDOW_WIDTH, WINDOW_HEIGHT)
    
    show_position(screen, player_pos)
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
    


    pygame.draw.circle(screen, GREEN, player_pos, player_radius)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()