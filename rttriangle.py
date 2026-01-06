from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
angle=0
speed=2
x=0
def init():
    glClearColor(1,1,1,1)
    gluOrtho2D(-300,300,-300,300)

def triangle():
    glBegin(GL_POLYGON)
    glVertex2f(-25,-12.5)
    glVertex2f(25,-12.5)
    glVertex2f(0,25)
    glEnd()

def draw():
    global angle,speed,x
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0,0,1)
    glPushMatrix()
    glTranslatef(x,0,0)
    glRotatef(angle,0,0,1)
    triangle()
    glPopMatrix()
    glutSwapBuffers()

def animate(temp):
    global angle,speed,x
    angle+=speed
    x+=speed
    if x>300:
        x=-300
    if angle>360:
        angle-=360
    glutPostRedisplay()
    glutTimerFunc(10,animate,0)
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(600,0)
    glutCreateWindow(b"Sample")
    glutDisplayFunc(draw)
    glutTimerFunc(0,animate,0)
    init()
    glutMainLoop()
main()