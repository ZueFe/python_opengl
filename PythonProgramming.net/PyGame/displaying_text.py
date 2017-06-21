# Codes for the tutorial at https://pythonprogramming.net/displaying-text-pygame-screen/
# Added comments and custom notes
import pygame
import time

pygame.init()

display_width = 800
display_height = 600
# Defines the width of sprite (image)
car_width = 73

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')

# Color constants
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

car_speed = 0

clock = pygame.time.Clock()
carImg = pygame.image.load('img//racecar.png')

# Draw car image at coordinates X, Y
def draw_car(x,y):
    gameDisplay.blit(carImg, (x,y))

# Create text object and text bounding box
def text_objects(text, font):
    text_surfaces = font.render(text, True, BLACK)
    return text_surfaces, text_surfaces.get_rect()

# Display given text
def message_display(text):
    # Set up used font and its size
    large_Text = pygame.font.Font('freesansbold.ttf', 115)
    # Create text object and its encompassing rectangle
    text_surface, text_rect = text_objects(text, large_Text)
    # Center the text
    text_rect.center = ((display_width/2), (display_height/2))
    # Display text on the screen
    gameDisplay.blit(text_surface, text_rect)

    pygame.display.update()
    # Wait 2 seconds and go back to game_loop function
    time.sleep(2)


# Display message "You crashed"
def crash():
    message_display('You crashed')

"""
Events taking place every frame
"""
def game_loop():
    # Initial car position, upper left corner
    x =  (display_width * 0.45)
    y = (display_height * 0.8)
    crashed = False

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

            # Zero out X change, to avoid missing event handling
            # If for example FPS is low
            x_change = 0

            # Add the input control
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            # This is unnecessary if x_change is zeroed out in every frame
            #if event.type == pygame.KEYUP:
            #    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            #        x_change = 0

        # Get new X coordinate based on input control
        # Similar works for Y if implemeted
        x += x_change

        # To keep car within screen and don't crash game
        # Just remove the addition of x_change from above
        #if x > display_width - car_width or x < 0:
        #   x -= x_change

        # To "teleport" car to other side of screen
        # Modulo current x (with added x_change)
        #x = x % (display_width - car_width)

        # Give window white background
        gameDisplay.fill(WHITE)
        draw_car(x,y)

        # If car gets out of the screen, display text about ending game
        if x > display_width - car_width or x < 0:
            # Display crash text
            crash()

            # End Game
            crashed = True

        # Render all objects
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
