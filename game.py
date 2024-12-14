import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Cabin")

# Load the background image
background_image = pygame.image.load("background.png")

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the background image
    screen.blit(background_image, (0, 0))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()

