from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import sys

# === Global Variables ===
x, y = 0, 0           # initial position of the ball
dx, dy = 2, 3          # change in position (speed in x and y)
radius = 30            # radius of the ball
window_size = 300      # defines boundary limits

def init():
    glClearColor(1, 1, 1, 1)   # white background
    gluOrtho2D(-window_size, window_size, -window_size, window_size)

def draw_ball():
    glColor3f(1, 0, 0)         # red ball
    glBegin(GL_POLYGON)
    for i in range(360): 
        glVertex2f(x + radius * math.cos(math.radians(i)), y + radius * math.sin(math.radians(i)))
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_ball()
    glutSwapBuffers()

def animate(value):
    global x, y, dx, dy

    # move ball
    x += dx
    y += dy

    # bounce on walls
    if x + radius > window_size or x - radius < -window_size:
        dx = -dx  # reverse x direction
    if y + radius > window_size or y - radius < -window_size:
        dy = -dy  # reverse y direction

    glutPostRedisplay()
    glutTimerFunc(10, animate, 0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(600, 0)
    glutCreateWindow(b"Bouncing Ball Animation")
    init()
    glutDisplayFunc(display)
    glutTimerFunc(0, animate, 0)
    glutMainLoop()

main()
