import math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

r = 50
angle = 0  # for oscillation motion (flapping phase)

def init():
    glClearColor(0, 0, 0, 1)
    gluOrtho2D(-300, 300, -300, 300)

def circle():
    glColor3f(225/255, 78/255, 31/255)
    glBegin(GL_TRIANGLE_FAN)
    for i in range(0, 361):
        glVertex2f(r * math.cos(math.radians(i)), r * math.sin(math.radians(i)))
    glEnd()

def triangle(offset_y):
    glColor3f(0, 1, 0)
    glBegin(GL_TRIANGLES)
    # left wing
    glVertex2f(0, 0)
    glVertex2f(-150, 50 + offset_y)
    glVertex2f(-150, -50 + offset_y)
    glEnd()

def triangle_right(offset_y):
    glColor3f(0, 1, 0)
    glBegin(GL_TRIANGLES)
    # right wing
    glVertex2f(0, 0)
    glVertex2f(150, 50 + offset_y)
    glVertex2f(150, -50 +offset_y)
    glEnd()

def draw():
    global angle
    glClear(GL_COLOR_BUFFER_BIT)

    # Create mirrored up/down motion using sine wave
    offset_y = 50 * math.sin(math.radians(angle))

    # Draw wings (triangles)
    triangle(offset_y)       # left triangle moves up and down
    triangle_right(offset_y) # right triangle mirrors motion

    # Draw center circle (stationary body)
    circle()

    glFlush()

def animate(value):
    global angle
    angle += 5
    if angle >= 360:
        angle = 0
    glutPostRedisplay()
    glutTimerFunc(30, animate, 0)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(600, 0)
    glutCreateWindow(b"Flapping Wings Animation - OpenGL")
    init()
    glutDisplayFunc(draw)
    glutTimerFunc(30, animate, 0)
    glutMainLoop()

main()