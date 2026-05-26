import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bullet Dodging Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Clock to control FPS
clock = pygame.time.Clock()

# Player settings
player_width, player_height = 50, 50
player_x = WIDTH // 2
player_y = HEIGHT - 100
player_speed = 7

# Bullet settings
bullet_width, bullet_height = 10, 30
bullet_speed = 7
bullets = []

# Score
score = 0
font = pygame.font.SysFont("Arial", 30)

# Function to create bullets
def create_bullet():
    bullet_x = random.randint(0, WIDTH - bullet_width)
    bullet_y = -bullet_height
    bullets.append(pygame.Rect(bullet_x, bullet_y, bullet_width, bullet_height))

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get keys pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < HEIGHT - player_height:
        player_y += player_speed

    # Create bullets periodically
    if random.randint(1, 20) == 1:  # Random bullet creation
        create_bullet()

    # Move bullets
    for bullet in bullets:
        bullet.y += bullet_speed
        if bullet.y > HEIGHT:  # Remove bullets that are off-screen
            bullets.remove(bullet)

    # Check for collisions
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    for bullet in bullets:
        if player_rect.colliderect(bullet):
            print("Game Over! Final Score:", score)
            pygame.quit()
            sys.exit()

    # Update score
    score += 1

    # Draw everything
    screen.fill(WHITE)  # Background
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))  # Player
    for bullet in bullets:
        pygame.draw.rect(screen, RED, bullet)  # Bullets

    # Draw score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Update display
    pygame.display.update()

    # Set FPS
    clock.tick(60)