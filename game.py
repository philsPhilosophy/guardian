import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Moving Character Example")

# Load the background image
background_image = pygame.image.load("cabintestdrawing1.png")

# Define the character's properties
character_color = (255, 0, 0)  # Red
character_size = 30  # Radius for circle or side length for square
character_x = 400  # Initial x-coordinate
character_y = 300  # Initial y-coordinate
character_speed = 5  # Movement speed

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get key presses for movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        character_y -= character_speed
    if keys[pygame.K_DOWN]:
        character_y += character_speed
    if keys[pygame.K_LEFT]:
        character_x -= character_speed
    if keys[pygame.K_RIGHT]:
        character_x += character_speed

    # Draw the background
    screen.blit(background_image, (0, 0))

    # Draw the character (circle or square)
    # Circle
    pygame.draw.circle(screen, character_color, (character_x, character_y), character_size)
    # Uncomment below and comment above to use a square instead:
    # pygame.draw.rect(screen, character_color, (character_x, character_y, character_size, character_size))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
