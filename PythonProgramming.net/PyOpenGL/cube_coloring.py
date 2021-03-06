# This code is taken from tutorial at https://pythonprogramming.net/coloring-pyopengl-surfaces-python-opengl/
# Slight modification were made in terms of syntax. Comments added to explain some nuances of OpenGL.

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Create cube vertices
vertices = (
    (1,-1,-1),
    (1,1,-1),
    (-1,1,-1),
    (-1,-1,-1),
    (1,-1,1),
    (1,1,1),
    (-1,-1,1),
    (-1,1,1)
)

# Create edges of the cube
edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
)

# Colors of the cube, OpenGL also accepts unsigned chars
# For colors (aka in range of [0,255])
colors = (
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (0,1,0),
    (1,1,1),
    (0,1,1),
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (1,0,0),
    (1,1,1),
    (0,1,1),
)

# Quads of the cube. For efficiency triangles can be used also
surfaces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
    )

"""
Surface representation of the cube. With colors
glBegin and glEnd are GL2 construct (used in OpenGL2).
Weirdness caused when cube is rotated, where it almost looks transparent,
is due to disabled Depth Test.
"""
def draw_cube():
    glBegin(GL_QUADS)
    for surface in surfaces:
        x = 0
        for vertex in surface:
            x += 1

            glColor3fv(colors[x])
            glVertex3fv(vertices[vertex])
    glEnd()

    # To highlight cube lines. If you don't reaquire
    # Edges to be visible, this part is no necessary
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    # Notify pygame we will be using OpenGL context
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    # Parameters: FOV, aspect ratio, near clipping plane, far clipping plane
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    # Move all objects drawn from here on by -5 in Z axis. GL2 construct.
    # Translation is done through shaders in GL4 (similar in rotation).
    glTranslatef(0.0,0.0,-5.0)

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Note that usually you want to clear transformation matrix at least
        # In every run of the main loop and keep rotation angle separate
        glRotatef(1,3,1,1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        draw_cube()
        pygame.display.flip()
        pygame.time.wait(10)

# Run main game loop
if __name__ == '__main__':
    main()
