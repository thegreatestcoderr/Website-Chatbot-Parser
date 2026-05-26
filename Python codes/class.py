import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

fps = 60
gravity = 1
jump_strength = 15
ground_y = 100

player_size = 50
player_x = 400
player_y = 600-ground_y-player_size
player_vel_y = 0
on_ground = True
move_speed = 4
running = True
while running:
    clock.tick(fps)
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= move_speed
    if keys[pygame.K_RIGHT]:
        player_x += move_speed
    if keys[pygame.K_UP] and on_ground:
        player_vel_y = -jump_strength
        on_ground = False
    player_vel_y += gravity
    player_y += player_vel_y
    if player_y + player_size >= 600-ground_y:
        player_y = 600-ground_y-player_size
        plaer_vel_y = 0
        on_ground = True
    pygame.draw.rect(screen, (0, 255, 0), (0, 600-ground_y, 800, ground_y))
    pygame.draw.rect(screen, (0, 0, 255), (player_x, player_y, player_size, player_size))

    pygame.display.update()


pygame.quit()
