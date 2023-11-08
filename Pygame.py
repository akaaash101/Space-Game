import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Game")

# Player 1
player1_x = 50
player1_y = HEIGHT // 2
player1_speed = 5

# Player 2
player2_x = WIDTH - 50
player2_y = HEIGHT // 2
player2_speed = 5

# Main game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player 1 controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player1_y -= player1_speed
    if keys[pygame.K_s]:
        player1_y += player1_speed

    # Player 2 controls
    if keys[pygame.K_UP]:
        player2_y -= player2_speed
    if keys[pygame.K_DOWN]:
        player2_y += player2_speed

    # Update the screen
    screen.fill(WHITE)
    pygame.draw.rect(screen, (0, 0, 255), (player1_x, player1_y, 20, 20))  # Player 1's ship
    pygame.draw.rect(screen, (255, 0, 0), (player2_x, player2_y, 20, 20))  # Player 2's ship
    pygame.display.update()

    # Limit frame rate
    clock.tick(60)

# Quit the game
pygame.quit()
sys.exit()
