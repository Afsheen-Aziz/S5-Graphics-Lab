import sys, math, time
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def init():
    glClearColor(1, 1, 1, 1)   # background
    gluOrtho2D(-300, 300, -300, 300)           # coordinate system

def draw_circle(xc, yc, r):
    glBegin(GL_LINE_LOOP)
    for theta in range(0, 360):
        glVertex2f(xc+r*math.cos(math.radians(theta)), yc+r*math.sin(math.radians(theta)))
    glEnd()

def draw_hand(length, angle):
    glBegin(GL_LINES)
    glVertex2f(0, 0)
    glVertex2f(length*math.cos(math.radians(angle)), length*math.sin(math.radians(angle)))
    glEnd()

def draw():
    glClear(GL_COLOR_BUFFER_BIT)

    # draw outer circle
    glColor3f(0.5, 0.5, 0.5)
    draw_circle(0, 0, 120)

    # get current time
    t = time.localtime()
    sec_angle = 90 - (t.tm_sec * 6)
    min_angle = 90 - (t.tm_min * 6)
    hr_angle = 90 - ((t.tm_hour % 12) * 30 + t.tm_min * 0.5)

    # draw hands
    glColor3f(1,0,0)   # seconds hand
    draw_hand(100, sec_angle)

    glColor3f(0, 1, 0)              # minutes hand
    draw_hand(80, min_angle)

    glColor3f(0, 0, 1)              # hours hand
    draw_hand(50, hr_angle)

    glutSwapBuffers()

def animate(temp):
    glutPostRedisplay()
    glutTimerFunc(1000, animate, 0)   # update every second

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(600, 0)
    glutCreateWindow(b"CLOCK")
    glutDisplayFunc(draw)
    glutTimerFunc(0, animate, 0)
    init()
    glutMainLoop()

main()
