from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math, sys

angle1 = 0
angle2 = 0
sangle1 = 0
sangle2 = 0

def init():
    glClearColor(1, 1, 1, 1)
    gluOrtho2D(-300, 300, -300, 300)

def draw_circle(r):
    glBegin(GL_LINE_LOOP)
    for i in range(360):
        glVertex2f(r * math.cos(math.radians(i)), r * math.sin(math.radians(i)))
    glEnd()

def draw_orbit(r):
    glColor3f(0, 0, 0)
    glBegin(GL_LINE_LOOP)
    for i in range(360):
        glVertex2f(r * math.cos(math.radians(i)), r * math.sin(math.radians(i)))
    glEnd()

def draw():
    global angle1, angle2, sangle1, sangle2
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw Sun
    glColor3f(1, 1, 0)
    draw_circle(75)

    # Planet 1
    glPushMatrix()
    glColor3f(0, 0, 0)
    draw_orbit(150)

    glRotatef(angle1, 0, 0, 1)   # rotate the coordinate system for revolution
    glTranslatef(150, 0, 0)      # move out from the sun

    glPushMatrix()
    glRotatef(sangle1, 0, 0, 1)  # spin on own axis
    glColor3f(1, 0, 0)
    draw_circle(50)
    for i in range(0, 360, 45):
        glBegin(GL_LINES)
        glVertex2f(0, 0)
        glVertex2f(50 * math.cos(math.radians(i)), 50 * math.sin(math.radians(i)))
        glEnd()
    glPopMatrix()
    glPopMatrix()

    # Planet 2
    glPushMatrix()
    draw_orbit(250)
    glRotatef(angle2, 0, 0, 1)
    glTranslatef(250, 0, 0)
    glPushMatrix()
    glRotatef(sangle2, 0, 0, 1)
    glColor3f(0, 1, 0)
    draw_circle(50)
    for i in range(0, 360, 45):
        glBegin(GL_LINES)
        glVertex2f(0, 0)
        glVertex2f(50 * math.cos(math.radians(i)), 50 * math.sin(math.radians(i)))
        glEnd()
    glPopMatrix()
    glPopMatrix()

    glutSwapBuffers()

def animate(value):
    global angle1, angle2, sangle1, sangle2

    # Revolution speeds
    angle1 = (angle1 + 5) % 360
    angle2 = (angle2 + 2) % 360

    # Spin speeds
    sangle1 = (sangle1 + 10) % 360
    sangle2 = (sangle2 + 6) % 360

    glutPostRedisplay()
    glutTimerFunc(100, animate, 0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(600, 100)
    glutCreateWindow(b"Solar System ")
    init()
    glutDisplayFunc(draw)
    glutTimerFunc(0, animate, 0)
    glutMainLoop()

main()
