# Codes for the tutorial at https://pythonprogramming.net/adding-score-pygame-video-game/
# Added comments and custom notes
import pygame
import time
import random

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

# Draw rect at x,y coords with given width and height
def draw_rect(x, y, width, height, color):
    pygame.draw.rect(gameDisplay, color, [x, y, width, height])

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

def dodged_obstacle(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, BLACK)
    gameDisplay.blit(text,(0,0))

"""
Events taking place every frame
"""
def game_loop():
    # Initial car position, upper left corner
    x =  (display_width * 0.45)
    y = (display_height * 0.8)
    crashed = False

    # Define obstacle rect
    ob_startX = random.randrange(0, display_width)
    ob_startY = -600
    # Speed in pixels per frame
    ob_speed = 7
    ob_width = 100
    ob_height = 100

    dodged = 0

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

        # Draw objects
        draw_rect(ob_startX, ob_startY, ob_width, ob_height, BLACK)
        draw_car(x,y)

        # Display score
        dodged_obstacle(dodged)

        # Move object to player
        ob_startY += ob_speed

        # If car gets out of the screen, display text about ending game
        if x > display_width - car_width or x < 0:
            # Display crash text
            crash()

            # End Game
            crashed = True

        # When obstacle passes edge of screen move it back
        # to top of the display
        if ob_startY > display_height:
            ob_startY = -ob_height
            ob_startX = random.randrange(0, display_width)

            # Add to score anytime player passes obstacle
            # And increase difficulty
            dodged +=1
            ob_speed += 1
            ob_width += (dodged * 1.2)

        if y < ob_startY + ob_height:
            print('y crossover')

            # If car is between X coordinates of the obstacle
            # Entire if statment has to be in () if it's to beroken to several lines
            if ((x > ob_startX and x < ob_startX + ob_width) or
             (x + car_width > ob_startX and x + car_width < ob_startX + ob_width)):
                print('x crossover')
                crash()

                crashed = True

        # Render all objects
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
