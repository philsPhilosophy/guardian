import pygame
import sys
import random
import os
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

door_x, door_y, door_w, door_h = 570, 60, 90, 40
door = pygame.Rect(door_x,door_y,door_w, door_h)

books_x, books_y, books_width, books_height = 700, 175, 80, 350
books = pygame.Rect(books_x, books_y, books_width, books_height)

# Define screens as constants
CABIN = "cabin"
DREAMS = "dreams"
GAME_SCREEN = "game_screen"
OUTSIDE = "outside"

# Global State: Current screen
current_screen = CABIN
character_x = screen_width // 2  # Start at the center of the screen
character_y = screen_height // 2
current_direction = "down"
character_speed = .35  # Movement speed

trans = False
outsidetrans = False

# --------------------- Screen Functions ---------------------

def cabin():
    global character_x, character_y, current_direction, character_speed, original_y, original_x, GAME_SCREEN, GAME_OVER, trans, outsidetrans
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
    if keys[pygame.K_w]:
        menu()

    character_rect = pygame.Rect(character_x, character_y, character_width, character_height)
        # Check for interaction with the bed
    if character_rect.colliderect(bed_rect):
        character_x = original_x
        character_y = original_y
        show_text = True
    if show_text:
        text_box_rect = pygame.Rect(character_x+58, character_y-22, 250, 20)
        pygame.draw.rect(screen, (0, 0, 0), text_box_rect)
        pygame.draw.rect(screen, (255, 255, 255), text_box_rect, 2)
        question_text = font.render("Would you like to sleep? (Y/N)", True, (255, 255, 255))
        screen.blit(question_text, (character_x+60, character_y-20))
        if keys[pygame.K_y]:
            fade_surface = pygame.Surface((screen_width, screen_height))  # Create a black surface
            fade_surface.fill(BLACK)  # Fill it with black
            for alpha in range(0, 255, 5):  # Gradually increase alpha
                fade_surface.set_alpha(alpha)  # Set transparency level
                screen.blit(fade_surface, (0, 0))  # Blit the surface on the screen
                pygame.display.flip()  # Update display
                pygame.time.delay(30)  # Delay for smooth transition
            trans = True
    if character_rect.colliderect(door):
        outsidetrans = True
    if character_rect.colliderect(books):
        text_box_rect = pygame.Rect(character_x - 58, character_y - 22, 250, 20)
        pygame.draw.rect(screen, (0, 0, 0), text_box_rect)
        pygame.draw.rect(screen, (255, 255, 255), text_box_rect, 2)
        question_text = font.render("   Would you like to read? (Y/N)", True, (255, 255, 255))
        screen.blit(question_text, (character_x - 60, character_y - 20))
        if keys[pygame.K_y]:
            menu()

    if character_rect.colliderect(left_wall) or character_rect.colliderect(right_wall) or character_rect.colliderect(
            bot_wall) or character_rect.colliderect(top_wall):
        character_x = original_x
        character_y = original_y
    if character_rect.colliderect(fire):
        character_x = original_x
        character_y = original_y




    # Draw the character image based on the current direction
    screen.blit(character_images[current_direction], (character_x, character_y))
'''
    pygame.draw.rect(screen, (255, 255, 255), (bed_x, bed_y, bed_width, bed_height), 2)
    pygame.draw.rect(screen, (255, 255, 255), (left_wall_x, left_wall_y, wall_width, wall_height), 2)
    pygame.draw.rect(screen, (255, 255, 255), (top_wall_x, top_wall_y, top_width, top_height), 2)
    pygame.draw.rect(screen, (255, 255, 255), (right_wall_x, right_wall_y, rwall_width, rwall_height), 2)
    pygame.draw.rect(screen, (255, 255, 255), (bot_wall_x, bot_wall_y, bwall_width, bwall_height), 2)
    pygame.draw.rect(screen, (255, 255, 255), (fire_x, fire_y, fire_width, fire_height), 2)
    pygame.draw.rect(screen, (255,255,255), (door_x, door_y, door_w, door_h),2 )
    pygame.draw.rect(screen, (255,255,255), (books_x, books_y, books_width, books_height), 2)

'''



def dreams():
    """Dream Screen"""

    global current_screen, trans, k, font
    font = pygame.font.Font(None, 34)
    fontd =pygame.font.Font(None, 48)
    dreamO= ['Dreaming...']
    dream = [['','I dream that I am a dream character inside the mind of a god.','The god dreams my exsistence and life.','That way the god can simulate the questions it wonders.'],
             [ '', 'I dream that I am Zhuang Zhou dreaming that he is a butterfly.', 'When he awakes he is unsure of whether he is Zhuang Zhou or',' the butterfly dreaming he is Zhuang Zhou.','I awake not knowing if I am a butterfly, Zhuang Zhou, or myself.'],
             ['', 'I dream that a voice states:','All Your Fears are Illusory.']]
    running = True
    i = 0
    screen.fill((0, 0, 0))
    randomdream = random.choice(dream)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:  # Check for a key press event
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:  # If spacebar is pressed
                    print('space pressed', i)
                    i += 1

        # Render text and update the screen

        if i < len(randomdream):  # Only render if within bounds

            screen.fill((0, 0, 0))  # Clear the screen
            dreamopening = fontd.render(dreamO[0], True, (255, 255, 255))
            screen.blit(dreamopening, (0,0))
            pygame.time.delay(30)
            for j in range(min(i, len(randomdream))+1):
                dream_text = font.render(randomdream[j], True, (255, 255, 255))
                screen.blit(dream_text, (50,  (100+j * 50)))

            pygame.display.flip()  # Update display
        else:
            print('end dream loop')
            trans = False
            current_screen = CABIN
            break

        pygame.display.flip()  # Update display




def outside():
    """Game Over Screen"""
    global outsidetrans, CABIN, current_screen, trans, character_y
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 36)
    y=0
    text_l = [
        "We are on our way to the outward regions,",
        "to Mars and other places.",
        "But here is a journey inward.",
        "A Journey In Mind"
    ]


    # Define initial vertical position

    i = 0
    # Render and display each line
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:  # Check for a key press event
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:  # If spacebar is pressed
                    print('space pressed', i)
                    i += 1

        # Render text and update the screen

        if i < len(text_l):  # Only render if within bounds

            screen.fill((0, 0, 0))  # Clear the screen
            pygame.time.delay(30)
            for j in range(min(i, len(text_l)) + 1):
                dream_text = font.render(text_l[j], True, (255, 255, 255))
                screen.blit(dream_text, (50, (100 + j * 50)))

            pygame.display.flip()  # Update display
        else:

            outsidetrans = False
            character_y += 40

            current_screen = CABIN
            break

        pygame.display.flip()  # Update display


fontM = pygame.font.Font(None, 40)

bg_color = (255, 105, 220)
text_color = (0, 0, 0)
highlight_color = (255, 255, 255)

topics = {
    "Mathematics": [
                ("Foundations of Geometry, Hilbert", "assets/Books/Hilbert.pdf"),
                ("Elements, Euclid","assets/Books/Elements.pdf"),
                ("On Formally Undecidable Propositions, Godel", "assets/Books/Godel.pdf"),
                ("Calculus, Early Transcendentals, Stewart","assets/Books/calculus.pdf"),
                ("On Computable Numbers, Turing", "assets/Books/Computable.pdf"),
                ("A New Kind of Science, Wolfram", "assets/Books/ANewKindofScience.pdf")
    ],

    "History": [
                ("Sapiens, A Brief History of Humankind, Harari", "assets/Books/Harari.pdf"),
                ("The Black Death, A Personal History, Hatcher", "assets/Books/Hatcher.pdf")
    ],

    "Philosophy":[
                ("Thus Spoke Zarathustra, Nietzsche","assets/Books/Zarathustra.pdf")
    ],
    "Fiction":[
                ("All The Pretty Horses, McCarthy", "assets/Books/AllThePrettyHorses.pdf")
    ],
    "Computer Science":[
                ("Introduction to Algorithms, CLRS", "assets/Books/IntroAlgo.pdf"),
                ("Advances in Financial Machine Learning, Lopez de Prado","assets/Books/FML.pdf"),
                ("On Computable Numbers, Turing", "assets/Books/Computable.pdf"),
                ("A New Kind of Science, Wolfram", "assets/Books/ANewKindofScience.pdf")
    ],
    "Psychology":[
                ("The Interpretation of Dreams, Freud", "assets/Books/Freud.pdf"),
                ("Stories of Love, Vikings to Tinder, Larsen","assets/Books/StoriesofLovefromVikingstoTinder.pdf")
    ]
}

menu_state = "topics"  # Can be "topics" or "texts"
selected_topic = None
selected_index = 0

def draw_menu(options, selected_index):
    screen.fill(bg_color)
    for i, option in enumerate(options):
        color = highlight_color if i == selected_index else text_color
        text = fontM.render(option, True, color)
        screen.blit(text, (50, 100 + i * 50))
    pygame.display.flip()

def open_pdf(pdf_path):
    try:
        os.startfile(pdf_path)  # For Windows
    except AttributeError:
        os.system(f"open {pdf_path}")  # For macOS/Linux

def menu():
    global menu_state, selected_index, selected_topic
    running = True
    while running:
        # Determine menu options based on the current state
        if menu_state == "topics":
            options = list(topics.keys())
        else:  # menu_state == "texts"
            options = [text[0] for text in topics[selected_topic]] + ["Back"]

        draw_menu(options, selected_index)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_index = max(0, selected_index - 1)
                elif event.key == pygame.K_DOWN:
                    selected_index = min(len(options) - 1, selected_index + 1)
                elif event.key == pygame.K_RETURN:
                    if menu_state == "topics":
                        # Transition to the texts menu
                        selected_topic = options[selected_index]
                        menu_state = "texts"
                        selected_index = 0
                    elif menu_state == "texts":
                        if selected_index == len(options) - 1:  # "Back" option
                            menu_state = "topics"
                            selected_topic = None
                            selected_index = 0
                        else:
                            # Open the selected PDF
                            pdf_path = topics[selected_topic][selected_index][1]
                            open_pdf(pdf_path)

# --------------------- Main Game Loop ---------------------


 # Global state for screen transitions

clock = pygame.time.Clock()
running = True
k = 0
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

            # Event Handling for Screen Transitions
        if current_screen == CABIN:
            if trans:
                current_screen = DREAMS
            if outsidetrans:
                current_screen = OUTSIDE

       # Rendering Screens
    if current_screen == CABIN:
        cabin()

    elif current_screen == DREAMS:
        dreams()

    elif current_screen == OUTSIDE:
        outside()

    pygame.display.flip()  # Update display


