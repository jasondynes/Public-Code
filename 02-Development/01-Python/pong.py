import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
BALL_SPEED = 5
PADDLE_SPEED = 7
WHITE = (255, 255, 255)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Create paddles and ball
player_paddle = pygame.Rect(WIDTH - 20, HEIGHT // 2 - 40, 10, 80)
opponent_paddle = pygame.Rect(10, HEIGHT // 2 - 40, 10, 80)
ball = pygame.Rect(WIDTH // 2 - 10, HEIGHT // 2 - 10, 20, 20)

# Initialize ball direction
ball_direction = [random.choice([-1, 1]), random.choice([-1, 1])]

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move player paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_paddle.top > 0:
        player_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and player_paddle.bottom < HEIGHT:
        player_paddle.y += PADDLE_SPEED

    # Move opponent paddle
    if opponent_paddle.centery < ball.centery and opponent_paddle.bottom < HEIGHT:
        opponent_paddle.y += PADDLE_SPEED
    elif opponent_paddle.centery > ball.centery and opponent_paddle.top > 0:
        opponent_paddle.y -= PADDLE_SPEED

    # Move the ball
    ball.x += BALL_SPEED * ball_direction[0]
    ball.y += BALL_SPEED * ball_direction[1]

    # Ball collisions with walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_direction[1] *= -1

    # Ball collisions with paddles
    if (
        (ball.colliderect(player_paddle) and ball_direction[0] == 1)
        or (ball.colliderect(opponent_paddle) and ball_direction[0] == -1)
    ):
        ball_direction[0] *= -1

    # Check for scoring
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_direction = [random.choice([-1, 1]), random.choice([-1, 1])]
        ball.x = WIDTH // 2 - 10
        ball.y = HEIGHT // 2 - 10

    # Draw everything
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, WHITE, player_paddle)
    pygame.draw.rect(screen, WHITE, opponent_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Draw the center line
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)
