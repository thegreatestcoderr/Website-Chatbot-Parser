import pygame
pygame.init()
screenwidth = 800
screenheight = 800
screen = pygame.display.set_mode((screenwidth, screenheight))
pygame.display.set_caption("Pygame Pong")
Red = (255, 0, 0)
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 90
BALL_SIZE = 1
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
player_paddle = pygame.rect(50, screenheight // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
player_speed = 6
opponent_paddle = pygame.rect(screenwidth - 50 - PADDLE_WIDTH, screenheight // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
opponent_speed = 6
ball = pygame.rect(screenwidth // 2, BALL_SIZE //2, screenheight // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
ball_speed_x = 7 * 1
ball_speed_y = 7 * 1
clock = pygame.time.Clock()
FPS = 60
running = True
ball.x += ball_speed_x
ball.y += ball_speed_y
if ball.colliderect(player_paddle) or ball.colliderect(opponent_paddle):
    ball_speed_x *= -1
    

