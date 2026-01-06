from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys,math,time
y=50
dir=1
def init():
    glClearColor(1,1,1,1)
    gluOrtho2D(-300,300,-300,300)

def circle():
    glColor3f(1,0,0)
    glBegin(GL_POLYGON)
    for i in range(360):
        glVertex2f(50*math.cos(math.radians(i)),y+50*math.sin(math.radians(i)))
    glEnd()

def line():
    global y
    glColor3f(1,0,0)
    glBegin(GL_LINES)
    glVertex2f(0,300)
    glVertex2f(0,y)
    glEnd()

def draw():
    global y
    glClear(GL_COLOR_BUFFER_BIT)
    glPushMatrix()
    
    circle()
    line()
    glPopMatrix()
    glutSwapBuffers()

def animate(temp):
    global y,dir
    y+=dir*2
    if y <= -250:
        dir = 1
    elif y >= 250:
        dir = -1
        
    glutPostRedisplay()
    glutTimerFunc(5,animate,0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(600,0)
    glutCreateWindow(b"Yoyo")
    glutDisplayFunc(draw)
    glutTimerFunc(0,animate,0)
    init()
    glutMainLoop()
main()