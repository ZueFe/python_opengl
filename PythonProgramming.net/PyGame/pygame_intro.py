# Codes for the tutorial at https://pythonprogramming.net/pygame-python-3-part-1-intro/
# Added comments and custom notes

import pygame

# Initialize pygame context
pygame.init()

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('A bit Racey')

clock = pygame.time.Clock()

crashed = False

while not crashed:
    # Run through all events that happened in the frame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)

    # Refresh the window, this can update only specific parts of screen
    # To update entire screen at once use flip(), without parameter update() == flip()
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
