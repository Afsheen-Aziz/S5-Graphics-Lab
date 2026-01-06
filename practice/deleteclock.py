from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys,math,time

def init():
    glClearColor(1,1,1,1)
    gluOrtho2D(-300,300,-300,300)

def draw_circle(xc,yc,r):
    glBegin(GL_LINE_LOOP)
    for i in range(361):
        glVertex2f(xc+r*math.cos(math.radians(i)),yc+r*math.sin(math.radians(i)))
    glEnd()

def draw_hands(length,angle):
    glBegin(GL_LINES)
    glVertex2f(0,0)
    glVertex2f(length*math.cos(math.radians(angle)),length*math.sin(math.radians(angle)))
    glEnd()

def draw_clock():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.5,0.5,0.5)
    draw_circle(0,0,150)
    glColor3f(1,0,0)
    t=time.localtime()
    sec_angle=90-(t.tm_sec*6)
    min_angle=90-(t.tm_min*6)
    hr_angle=90-(t.tm_hour%12)*30+t.tm_min*0.5
    draw_hands(100,sec_angle)
    glColor3f(0,1,0)
    draw_hands(80,min_angle)
    glColor3f(0,0,1)
    draw_hands(50,hr_angle)
    glutSwapBuffers()
def animate(temp):
    glutPostRedisplay()
    glutTimerFunc(1000,animate,0)
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(600,0)
    glutCreateWindow(b"CLock")
    init()
    glutDisplayFunc(draw_clock)
    glutTimerFunc(0,animate,0)
    glutMainLoop()
main()
