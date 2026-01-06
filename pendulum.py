from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

angle = 0        # current swing angle
direction = 1    # swing direction
length = 200     # length of the string

def init():
    glClearColor(1, 1, 1, 1)
    gluOrtho2D(-300, 300, -300, 300)


def draw():
    global angle, length
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0, 0, 1)

    # Pivot point (top fixed point)
    pivot_x, pivot_y = 0, 250

    # Compute bob position using angle
    bob_x = pivot_x + length * math.sin(math.radians(angle))
    bob_y = pivot_y - length * math.cos(math.radians(angle))

    # Draw string (line)
    glLineWidth(5)
    glBegin(GL_LINES)
    glVertex2f(pivot_x, pivot_y)
    glVertex2f(bob_x, bob_y)
    glEnd()

    # Draw bob (small filled circle)
    glBegin(GL_TRIANGLE_FAN)
    for i in range(360):
        glVertex2f(bob_x + 30 * math.cos(math.radians(i)),
                   bob_y + 30 * math.sin(math.radians(i)))
    glEnd()

    glutSwapBuffers()

def animate(value):
    global angle, direction
    # Swing between -45° and +45°
    if angle >= 45:
        direction = -1
    elif angle <= -45:
        direction = 1

    angle += direction * 2      # change angle a bit
    glutPostRedisplay()         # redraw screen
    glutTimerFunc(50, animate, 0)  # recall after 50 ms


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(600, 0)
    glutCreateWindow(b"Simple Pendulum")
    init()
    glutDisplayFunc(draw)
    glutTimerFunc(0, animate, 0)
    glutMainLoop()

main()
