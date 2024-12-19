import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Cabin")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

background_image = pygame.image.load("assets/cabin.png")
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
# Define the character's properties
character_images = {
    "up": pygame.image.load("assets/NcharU.png"),
    "down": pygame.image.load("assets/NcharD.png"),
    "left": pygame.image.load("assets/NcharL.png"),
    "right": pygame.image.load("assets/NcharR.png"),
}

character_image = pygame.image.load("assets/NcharD.png")
character_width, character_height = 150, 150  # Adjust to fit your character size


for direction in character_images:
    character_images[direction] = pygame.transform.scale(
        character_images[direction], (character_width, character_height)
    )



fire_x, fire_y, fire_width, fire_height = 360, 0, 120,150
fire = pygame.Rect(fire_x, fire_y, fire_width, fire_height)

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

# Define screens as constants
CABIN = "cabin"
DREAMS = "dreams"
GAME_SCREEN = "game_screen"
GAME_OVER = "game_over"

# Global State: Current screen
current_screen = CABIN
character_x = screen_width // 2  # Start at the center of the screen
character_y = screen_height // 2
current_direction = "down"
character_speed = .35  # Movement speed

trans = False

# --------------------- Screen Functions ---------------------

def cabin():
    global character_x, character_y, current_direction, character_speed, original_y, original_x, GAME_SCREEN, GAME_OVER, trans
    screen.blit(background_image, (0, 0))
    show_text=False
    font = pygame.font.Font(None, 24)
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

    character_rect = pygame.Rect(character_x, character_y, character_width, character_height)
        # Check for interaction with the bed
    if character_rect.colliderect(bed_rect):
        character_x = original_x
        character_y = original_y
        show_text = True
    if show_text:
        text_box_rect = pygame.Rect(200, 150, 400, 100)
        pygame.draw.rect(screen, (0, 0, 0), text_box_rect)
        pygame.draw.rect(screen, (255, 255, 255), text_box_rect, 2)
        question_text = font.render("Would you like to sleep? (Y/N)", True, (255, 255, 255))
        screen.blit(question_text, (220, 180))
        if keys[pygame.K_y]:
            fade_surface = pygame.Surface((screen_width, screen_height))  # Create a black surface
            fade_surface.fill(BLACK)  # Fill it with black
            for alpha in range(0, 255, 5):  # Gradually increase alpha
                fade_surface.set_alpha(alpha)  # Set transparency level
                screen.blit(fade_surface, (0, 0))  # Blit the surface on the screen
                pygame.display.flip()  # Update display
                pygame.time.delay(30)  # Delay for smooth transition
            trans = True


    if character_rect.colliderect(left_wall) or character_rect.colliderect(right_wall) or character_rect.colliderect(
            bot_wall) or character_rect.colliderect(top_wall):
        character_x = original_x
        character_y = original_y
    if character_rect.colliderect(fire):
        character_x = original_x
        character_y = original_y




    # Draw the character image based on the current direction
    screen.blit(character_images[current_direction], (character_x, character_y))
    pygame.draw.rect(screen, (255, 255, 255), (bed_x, bed_y, bed_width, bed_height), 2)
    pygame.draw.rect(screen, (255, 255, 255), (left_wall_x, left_wall_y, wall_width, wall_height), 2)
    pygame.draw.rect(screen, (255, 255, 255), (top_wall_x, top_wall_y, top_width, top_height), 2)
    pygame.draw.rect(screen, (255, 255, 255), (right_wall_x, right_wall_y, rwall_width, rwall_height), 2)
    pygame.draw.rect(screen, (255, 255, 255), (bot_wall_x, bot_wall_y, bwall_width, bwall_height), 2)
    pygame.draw.rect(screen, (255, 255, 255), (fire_x, fire_y, fire_width, fire_height), 2)





def dreams():
    """Dream Screen"""
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 24)




def game_over():
    """Game Over Screen"""
    screen.fill((255, 0, 0))
    font = pygame.font.Font(None, 36)
    text = font.render("Game Over: Press R to Restart", True, BLACK)
    screen.blit(text, (200, 300))


# --------------------- Main Game Loop ---------------------


 # Global state for screen transitions

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

            # Event Handling for Screen Transitions
        if current_screen == CABIN:

            if trans:
                current_screen = DREAMS
        elif current_screen == GAME_SCREEN:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                current_screen = GAME_OVER
        elif current_screen == GAME_OVER:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                current_screen = CABIN

        # Rendering Screens
    if current_screen == CABIN:
        cabin()
    elif current_screen == DREAMS:
        dreams()
    elif current_screen == GAME_OVER:
        game_over()

    pygame.display.flip()  # Update display


