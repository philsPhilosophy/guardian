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

bed_x, bed_y, bed_width, bed_height = 100, 360, 300, 100  #BED LOCATION
bed_rect = pygame.Rect(bed_x, bed_y, bed_width, bed_height) #BED RECT

left_wall_x, left_wall_y, wall_width, wall_height = 0, 0, 80, 520 #Left wall location & dim.
left_wall = pygame.Rect(left_wall_x, left_wall_y, wall_width, wall_height) #Left Wall

top_wall_x, top_wall_y, top_width, top_height = 0,0, 800, 80 #Top Wall Location & dim
top_wall = pygame.Rect(top_wall_x, top_wall_y, top_width, top_height) #Top Wall

right_wall_x, right_wall_y, rwall_width, rwall_height = 720, 0, 80, 520 #Right wall location & dim.
right_wall = pygame.Rect(right_wall_x, right_wall_y, rwall_width, rwall_height) #Right Wall

bot_wall_x, bot_wall_y,bwall_width, bwall_height = 0,540, 800, 80 #Bottom wall location & dim.
bot_wall = pygame.Rect(bot_wall_x, bot_wall_y,bwall_width, bwall_height)
# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #Position to revert to
    original_x = character_x
    original_y = character_y

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
    # Create a character rect for collision detection
    character_rect = pygame.Rect(character_x, character_y, character_width, character_height)

    # Check for interaction with the bed
    if character_rect.colliderect(bed_rect):
        character_x = original_x
        character_y = original_y
        if keys[pygame.K_e]:  # Press 'E' to interact
            print("Interacting with the bed!")
            # Add the fade-to-black or text display function here
    # Check for interaction with walls
    if character_rect.colliderect(left_wall) or character_rect.colliderect(right_wall) or character_rect.colliderect(bot_wall) or character_rect.colliderect(top_wall):
        character_x = original_x
        character_y = original_y

    # Draw the background
    screen.blit(background_image, (0, 0))

    # Draw the character image based on the current direction
    screen.blit(character_images[current_direction], (character_x, character_y))
    pygame.draw.rect(screen, (255, 255, 255), (bed_x, bed_y, bed_width, bed_height), 2)
    pygame.draw.rect(screen, (255, 255, 255), (left_wall_x, left_wall_y, wall_width, wall_height), 2)
    pygame.draw.rect(screen, (255, 255, 255), (top_wall_x, top_wall_y, top_width, top_height), 2)
    pygame.draw.rect(screen, (255, 255, 255), (right_wall_x, right_wall_y, rwall_width, rwall_height), 2)
    pygame.draw.rect(screen, (255, 255, 255),(bot_wall_x, bot_wall_y,bwall_width, bwall_height) , 2)
    # Update the display
    pygame.display.flip()


# Quit Pygame
pygame.quit()
sys.exit()
