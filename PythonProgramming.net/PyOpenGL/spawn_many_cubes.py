# This code is taken from tutorial at https://pythonprogramming.net/random-cube-position-pyopengl-tutorial
# Slight modification were made in terms of syntax. Comments added to explain some nuances of OpenGL.

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random

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
def draw_cube(used_vertices):
    glBegin(GL_QUADS)
    for surface in surfaces:
        x = 0
        for vertex in surface:
            x += 1

            glColor3fv(colors[x])
            glVertex3fv(used_vertices[vertex])
    glEnd()

    # To highlight cube lines. If you don't reaquire
    # Edges to be visible, this part is no necessary
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(used_vertices[vertex])
    glEnd()

"""
Generate new position of vertices for cube.
Commented line contains shorter notation through lambda function.
"""
def set_vertices(max_distance):
    x_value_change = random.randrange(-10, 10)
    y_value_change = random.randrange(-10, 10)
    z_value_change = random.randrange(-1 * max_distance, -20)

    new_vertices = []

    """
    Through lambda:
    new_vertices = list(map(lambda x: [x[0] + x_value_change, x[1] + y_value_change, x[2] + z_value_change], vertices))
    """

    for vert in vertices:
        new_vert = []

        new_x = vert[0] + x_value_change
        new_y = vert[1] + y_value_change
        new_z = vert[2] + z_value_change

        new_vert.append(new_x)
        new_vert.append(new_y)
        new_vert.append(new_z)

        new_vertices.append(new_vert)

    return new_vertices

def main():
    pygame.init()
    # Use set_repeat to be able to move continually when arrow
    # key is held down. If first parameter is set to 0,
    # you have to keep pressing arrow to move
    pygame.key.set_repeat(1, 50)
    display = (800, 600)
    # Notify pygame we will be using OpenGL context
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    # Parameters: FOV, aspect ratio, near clipping plane, far clipping plane
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    # Move all objects drawn from here on by -5 in Z axis. GL2 construct.
    # Translation is done through shaders in GL4 (similar in rotation).
    glTranslatef(random.randrange(-5.0, 5.0), 0, -30)

    x_move = 0
    y_move = 0
    max_distance = 100
    cube_dict = {}

    for x in range(20):
        cube_dict[x] = set_vertices(max_distance)

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Used instead of KEYUP function
            x_move = 0
            y_move = 0

            # Generally, camera is moved instead of the object in CG (for optimization reasons)
            # No elifs used, otherwise the movement would be laggy
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_move = -0.3
                if event.key == pygame.K_RIGHT:
                    x_move = 0.3
                if event.key == pygame.K_UP:
                    y_move = 0.3
                if event.key == pygame.K_DOWN:
                    y_move = -0.3

            # This part is actually unnecessary if x_move and y_move are always zeroed out
            """
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_move = 0
                if event_key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_move = 0
            """

        # X is 4x4 matrix
        x = glGetDoublev(GL_MODELVIEW_MATRIX)
        camera_x = x[3][0]
        camera_y = x[3][1]
        camera_z = x[3][2]

        # Move by 0.5 in each frame (possible as transfomration matrix is never restarted)
        glTranslatef(x_move, y_move, 0.5)

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        for each_cube in cube_dict:
            draw_cube(cube_dict[each_cube])

        pygame.display.flip()
        pygame.time.wait(50)

        if camera_z <= 0:
            object_passed = True

# Run main game loop
if __name__ == '__main__':
    main()
