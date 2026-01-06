from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

n = int(input("Enter number of blades: "))
target_speed=int(input("Enter speed: "))

angle=0
speed=0
max_acc=0.5

def init():
    glClearColor(1,1,1,1)
    gluOrtho2D(-300,300,-300,300)

def draw_blade():
    glColor3f(0,0,1)
    glBegin(GL_POLYGON)
    glVertex2f(0,0)
    glVertex2f(-20,100)
    glVertex2f(20,100)
    glEnd()

def draw_fan():
    global angle
    glClear(GL_COLOR_BUFFER_BIT)
    for i in range(n):
        glPushMatrix()
        glRotatef(angle+i*(360/n),0,0,1)
        draw_blade()
        glPopMatrix()
    glutSwapBuffers()

def animate(temp):
    global angle,speed
    if speed<target_speed:
        speed+=max_acc
    else:
        speed=target_speed
    angle+=speed
    if angle>=360:
        angle-=360
    glutPostRedisplay()
    glutTimerFunc(20,animate,0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(600,0)
    glutCreateWindow(b"Fan")
    init()
    glutDisplayFunc(draw_fan)
    glutTimerFunc(0,animate,0)
    glutMainLoop()
main()
