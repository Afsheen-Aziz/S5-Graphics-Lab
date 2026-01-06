import math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

angle = 30  # global for rotation angle
x=0
xc=0
yc=0
def init():
    glClearColor(0, 0, 0, 1)
    gluOrtho2D(-300, 300, -300, 300)

def ploat():
    global x,xc,yx
    glColor3f(1, 1, 0)  # Pacman yellow
    glLineWidth(2)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0, 0)
    # Start at 45 - x, end at 270 + x for symmetrical opening mouth
    for i in range(int(30 - x), int(270 + x) + 1):
        glVertex2f((50 * math.cos(math.pi * i / 180)), (50 * math.sin(math.pi * i / 180)))
    glEnd()


def draw():
    global angle,x
    glClear(GL_COLOR_BUFFER_BIT)
    glPushMatrix()
    glTranslatef(xc,0,0)
    glRotatef(angle, 0, 0, 1)  # rotate around z-axis
    ploat()
    glPopMatrix()
    glFlush()

def animate(temp):
    global x,angle,xc,yc
    xc+=2
    if xc>300:
        xc=-300
    if x<=90:
        x+=2
    if x>90:
        x=0
    glutPostRedisplay()
    glutTimerFunc(50,animate,0)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)  # Single buffer
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"Rotating Pacman")
    init()
    glutDisplayFunc(draw)
    glutTimerFunc(0, animate, 0)
    glutMainLoop()

main()
