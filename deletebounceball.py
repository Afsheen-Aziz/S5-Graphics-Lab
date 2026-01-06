from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math,sys

x,y=0,0
dx,dy=2,3
r=50
def init():
    glClearColor(1,1,1,1)
    gluOrtho2D(-300,300,-300,300)

def circle(r):
    global x,y
    glBegin(GL_POLYGON)
    for i in range(361):
        glVertex2f(x+r*math.cos(math.radians(i)),y+r*math.sin(math.radians(i)))
    glEnd()

def draw():
    global x,y
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0,0,1)
    circle(r)
    glutSwapBuffers()

def animate(temp):
    global x,y,dx,dy
    x+=dx
    y+=dy
    if (x+r>300) or (x-r<-300):
        dx=-dx
    if (y+r>300) or (y-r<-300):
        dy=-dy
    glutPostRedisplay()
    glutTimerFunc(20,animate,0)

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