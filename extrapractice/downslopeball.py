from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import time,sys,math
ball_x=-300
ball_y=250
angle=0
def init():
    glClearColor(1,1,1,1)
    gluOrtho2D(-400,400,-400,400)

def slope():
    glColor3f(1,0,0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(-300,0)
    glVertex2f(-100,0)
    glVertex2f(-300,200)
    glEnd()

def ball():
    global ball_x,ball_y,angle
    glBegin(GL_LINE_LOOP)
    for i in range(360):
        glVertex2f(50*math.cos(math.radians(i)),50*math.sin(math.radians(i)))
    glEnd()

def draw():
    global ball_x,ball_y,angle
    glClear(GL_COLOR_BUFFER_BIT)
    slope()
    glPushMatrix()
    glTranslatef(ball_x,ball_y,0)
    glRotatef(angle,0,0,1)
    ball()
    for i in range(0,360,45):
        glBegin(GL_LINES)
        glVertex2f(0,0)
        glVertex2f(50*math.cos(math.radians(i)),50*math.sin(math.radians(i)))
        glEnd()
    glPopMatrix()
    glutSwapBuffers()

def animate(temp):
    global ball_x,ball_y,angle
    glutPostRedisplay()
    old_x=ball_x
    if ball_x<=-100 and ball_y>=0:
        ball_x+=2
        ball_y=(-1*ball_x-100)+50
    d=abs(ball_x-old_x)
    n=(d*360)/(2*math.pi*50)
    angle=(angle+n)%360
    glutTimerFunc(20,animate,0)
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(600,0)
    glutCreateWindow(b"Ball down a slope")
    glutDisplayFunc(draw)
    glutTimerFunc(0,animate,0)
    init()
    glutMainLoop()
main()