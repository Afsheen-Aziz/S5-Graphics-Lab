from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import time,math,sys
x=-300
speed=2
angle=0
def init():
    glClearColor(1,1,1,1)
    gluOrtho2D(-300,300,-300,300)

def drawbody():
    global x
    glColor3f(1,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(x,0)
    glVertex2f(x+200,0)
    glVertex2f(x+200,50)
    glVertex2f(x,50)
    glEnd()
    glColor3f(0,1,0)
    glBegin(GL_POLYGON)
    glVertex2f(x+50,50)
    glVertex2f(x+150,50)
    glVertex2f(x+150,100)
    glVertex2f(x+50,100)
    glEnd()

def drawwheel1():
    glPushMatrix()
    glColor3f(0,0,0)
    glTranslatef(x+50,-25,0)
    glRotatef(angle,0,0,1)
    glBegin(GL_POLYGON)
    for i in range(360):
        glVertex2f((25*math.cos(math.radians(i))),(25*math.sin(math.radians(i))))
    glEnd()
    glColor3f(0,1,1)
    for i in range(0,360,45):
        glBegin(GL_LINES)
        glVertex2f(0,0)
        glVertex2f(25*math.cos(math.radians(i)),25*math.sin(math.radians(i)))
        glEnd()
    glPopMatrix()

def drawwheel2():
    glPushMatrix()
    glColor3f(0,0,0)
    glTranslatef(x+150,-25,1)
    glRotatef(angle,0,0,1)
    glBegin(GL_POLYGON)
    for i in range(360):
        glVertex2f((25*math.cos(math.radians(i))),(25*math.sin(math.radians(i))))
    glEnd()
    glColor3f(0,1,1)
    for i in range(0,360,45):
        glBegin(GL_LINES)
        glVertex2f(0,0)
        glVertex2f(25*math.cos(math.radians(i)),25*math.sin(math.radians(i)))
        glEnd()
    glPopMatrix()

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    drawbody()
    drawwheel1()
    drawwheel2()
    glutSwapBuffers()

def animate(temp):
    global x,speed,angle
    x+=speed
    if x>=300:
        x=-300
    angle-=speed*(360/(2*math.pi*25))
    if angle>360:
        angle-=360
    glutPostRedisplay()
    glutTimerFunc(20,animate,0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(600,0)
    glutCreateWindow(b"Car")
    glutDisplayFunc(draw)
    glutTimerFunc(0,animate,0)
    init()
    glutMainLoop()
main()