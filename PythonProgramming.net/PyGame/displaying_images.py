# Codes for the tutorial at https://pythonprogramming.net/displaying-images-pygame/
# Added comments and custom notes
import pygame

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')

# Color constants
BLACK = (0,0,0)
WHITE = (255,255,255)

clock = pygame.time.Clock()
crashed = False
carImg = pygame.image.load('img//racecar.png')

# Draw car image at coordinates X, Y
def draw_car(x,y):
    gameDisplay.blit(carImg, (x,y))

# Initial car position, upper left corner
x =  (display_width * 0.45)
y = (display_height * 0.8)

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    # Give window white background
    gameDisplay.fill(WHITE)
    draw_car(x,y)

    # Render all objects
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
