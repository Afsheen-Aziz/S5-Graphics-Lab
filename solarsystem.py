from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import sys

# === Global rotation angles ===
earth_angle = 0
moon_angle = 0

def init():
    glClearColor(1, 1, 1, 1)  # black background
    gluOrtho2D(-300, 300, -300, 300)

def draw_circle(radius, r, g, b):
    glColor3f(r, g, b)
    glBegin(GL_POLYGON)
    for i in range(360):
        angle = math.radians(i)
        glVertex2f(radius * math.cos(angle), radius * math.sin(angle))
    glEnd()

def display():
    global earth_angle, moon_angle
    glClear(GL_COLOR_BUFFER_BIT)
    # --- Draw Sun ---
    glPushMatrix()
    draw_circle(30, 1, 1, 0)  # yellow Sun at center
    glPopMatrix()

    # --- Draw Earth orbiting around Sun ---
    glPushMatrix()
    glRotatef(earth_angle, 0, 0, 1)   # rotation for Earth's orbit
    glTranslatef(150, 0, 0)           # Earth orbit radius
    draw_circle(15, 0, 0, 1)          # blue Earth

    # --- Draw Moon orbiting around Earth ---
    glRotatef(moon_angle, 0, 0, 1)
    glTranslatef(40, 0, 0)            # Moon orbit radius
    draw_circle(6, 0.8, 0.8, 0.8)     # gray Moon
    glPopMatrix()

    glutSwapBuffers()

def update(value):
    global earth_angle, moon_angle
    earth_angle += 0.3     # Earth's rotation speed
    moon_angle += 2        # Moon's rotation speed

    # keep angles within 0–360
    if earth_angle >= 360:
        earth_angle -= 360
    if moon_angle >= 360:
        moon_angle -= 360

    glutPostRedisplay()
    glutTimerFunc(20, update, 0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(400, 100)
    glutCreateWindow(b"Solar System Simulation")
    init()
    glutDisplayFunc(display)
    glutTimerFunc(0, update, 0)
    glutMainLoop()
main()
