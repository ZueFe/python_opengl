# Codes for the tutorial at https://pythonprogramming.net/pygame-drawing-shapes-objects/
# Added comments and custom notes

import pygame

pygame.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

gameDisplay = pygame.display.set_mode((800,600))
gameDisplay.fill(BLACK)

# Deconstructing display to 2D matrix
pixAr = pygame.PixelArray(gameDisplay)
# Assigning green color to pixel (10,20)
pixAr[10][20] = GREEN

# Draw a line from pixel (100,200) to (300,450) with line thickness 5
pygame.draw.line(gameDisplay, BLUE, (100,200), (300,450), 5)
# Draw rectangle with upper left corner in pixel (400, 400), width 50 and height 25
pygame.draw.rect(gameDisplay, RED, (400,400,50,25))
# Draw circle with center in pixel (150, 150) and radius 75 pixels
pygame.draw.circle(gameDisplay, WHITE, (150, 150), 75)
# Draw polygon with points at given coordinates
pygame.draw.polygon(gameDisplay, GREEN, ((25,75), (76,125), (250,375), (400,25), (60, 540)))

# Wait for quit event
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()
