from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

x=-300
y=0
def init():
    glClearColor(1,1,1,1)
    gluOrtho2D(-300,300,-300,300)

def quad():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0,0,1)
    glLineWidth(3)
    glBegin(GL_QUADS)
    glVertex2f(x,y)
    glVertex2f(x+100,y)
    glVertex2f(x+100,y+100)
    glVertex2f(x,y+100)
    glEnd()
    glutSwapBuffers()

def animate(temp):
    global x,y
    if x>300:
        x=-300
    x+=50
    glutPostRedisplay()
    glutTimerFunc(50,animate,0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(600,0)
    glutCreateWindow(b"Sample")
    glutDisplayFunc(lambda:quad())
    glutTimerFunc(0,animate,0)
    init()
    glutMainLoop()

main()
