import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Cabin")
screen_width, screen_height = 800, 600
# Load the background image
background_image = pygame.image.load("cabin.png")
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
# Define the character's properties
character_images = {
    "up": pygame.image.load("NcharU.png"),
    "down": pygame.image.load("NcharD.png"),
    "left": pygame.image.load("NcharL.png"),
    "right": pygame.image.load("NcharR.png"),
}

character_image = pygame.image.load("NcharD.png")
character_width, character_height = 150, 150  # Adjust to fit your character size
for direction in character_images:
    character_images[direction] = pygame.transform.scale(
        character_images[direction], (character_width, character_height)
    )

# Define the character's initial position
character_x = screen_width // 2  # Start at the center of the screen
character_y = screen_height // 2
character_speed = .35  # Movement speed
current_direction = "down"

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
        current_direction = "up"
    if keys[pygame.K_DOWN]:
        character_y += character_speed
        current_direction = "down"
    if keys[pygame.K_LEFT]:
        character_x -= character_speed
        current_direction = "left"
    if keys[pygame.K_RIGHT]:
        character_x += character_speed
        current_direction = "right"

    # Prevent the character from going off-screen
    if character_x < 0:
        character_x = 0
    if character_x + character_width > screen_width:
        character_x = screen_width - character_width
    if character_y < 0:
        character_y = 0
    if character_y + character_height > screen_height:
        character_y = screen_height - character_height

    # Draw the background
    screen.blit(background_image, (0, 0))

    # Draw the character image based on the current direction
    screen.blit(character_images[current_direction], (character_x, character_y))

    # Update the display
    pygame.display.flip()


# Quit Pygame
pygame.quit()
sys.exit()
