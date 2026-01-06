from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import time
import math

# --- Global state ---
signal_state = 0  # 0 = Red, 1 = Yellow, 2 = Green

def init():
    glClearColor(0, 0, 0, 1)
    gluOrtho2D(-300, 300, -300, 300)

def draw_rectangle(x1, y1, x2, y2, r, g, b):
    glColor3f(r, g, b)
    glBegin(GL_POLYGON)
    glVertex2f(x1, y1)
    glVertex2f(x2, y1)
    glVertex2f(x2, y2)
    glVertex2f(x1, y2)
    glEnd()

def draw_circle(x, y, radius, r, g, b):
    glColor3f(r, g, b)
    glBegin(GL_POLYGON)
    for i in range(360):
        angle = i * 3.14 / 180
        glVertex2f(x + radius * math.cos(angle), y + radius * math.sin(angle))
    glEnd()

def display():
    global signal_state
    glClear(GL_COLOR_BUFFER_BIT)

    # --- Traffic light body ---
    draw_rectangle(-50, -150, 50, 150, 0.3, 0.3, 0.3)  # grey box
    draw_rectangle(-10, -250, 10, -150, 0.3, 0.3, 0.3) # pole

    # --- Lights ---
    # Red light
    if signal_state == 0:
        draw_circle(0, 100, 30, 1, 0, 0)  # bright red
        draw_circle(0, 0, 30, 0.2, 0.2, 0.2)
        draw_circle(0, -100, 30, 0.2, 0.2, 0.2)
    # Yellow light
    elif signal_state == 1:
        draw_circle(0, 100, 30, 0.2, 0.2, 0.2)
        draw_circle(0, 0, 30, 1, 1, 0)  # bright yellow
        draw_circle(0, -100, 30, 0.2, 0.2, 0.2)
    # Green light
    else:
        draw_circle(0, 100, 30, 0.2, 0.2, 0.2)
        draw_circle(0, 0, 30, 0.2, 0.2, 0.2)
        draw_circle(0, -100, 30, 0, 1, 0)  # bright green

    glutSwapBuffers()

def update(value):
    global signal_state
    signal_state = (signal_state + 1) % 3  # cycle through lights: 0→1→2→0
    glutPostRedisplay()
    # Duration for each light (Red=2s, Yellow=1s, Green=2s)
    if signal_state == 0:
        glutTimerFunc(2000, update, 0)
    elif signal_state == 1:
        glutTimerFunc(1000, update, 0)
    else:
        glutTimerFunc(2000, update, 0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(400, 100)
    glutCreateWindow(b"Traffic Signal Simulation")
    init()
    glutDisplayFunc(display)
    glutTimerFunc(0, update, 0)
    glutMainLoop()

main()
