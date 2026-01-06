from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import time,sys,math

n=3
angle=0
speed=10
acc=0.1
cloud_x=-300

def init():
    glClearColor(1,1,1,1)
    gluOrtho2D(-300,300,-300,300)

def draw_cloud():
    glColor3f(0,0,1)
    glLineWidth(4)
    glBegin(GL_POLYGON)
    for i in range(361):
        glVertex2f(cloud_x+(50*math.cos(math.radians(i))),100+(50*math.sin(math.radians(i))))
    for i in range(361):
        glVertex2f((cloud_x-50)+(50*math.cos(math.radians(i))),100+(50*math.sin(math.radians(i))))
    for i in range(361):
        glVertex2f((cloud_x-100)+(50*math.cos(math.radians(i))),100+(50*math.sin(math.radians(i))))
    glEnd()
def draw_body():
    glColor3f(1,0,0)
    glLineWidth(4)
    glBegin(GL_LINE_LOOP)
    glVertex2f(0,100)
    glVertex2f(-50,-250)
    glVertex2f(50,-250)
    glEnd()
def draw_blade():
    glColor3f(1,0,0)
    glLineWidth(4)
    glBegin(GL_LINE_LOOP)
    glVertex2f(0,0)
    glVertex2f(-10,100)
    glVertex2f(10,100)
    glEnd()

def draw_mill():
    global angle
    glClear(GL_COLOR_BUFFER_BIT)
    draw_body()
    for i in range(n):
        glPushMatrix()
        glTranslatef(0,100,0)
        glRotatef(angle+(i*(360/n)),0,0,1)
        draw_blade()
        glPopMatrix()
    draw_cloud()
    glutSwapBuffers()

def animate(temp):
    global angle,speed,cloud_x
    if cloud_x<300:
        cloud_x+=1
    if cloud_x==300:
        cloud_x=-300
    angle+=speed
    if cloud_x>=-100 and cloud_x<=200:
        angle-=15
    angle+=speed
    if angle>360:
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
    glutDisplayFunc(draw_mill)
    glutTimerFunc(0,animate,0)
    glutMainLoop()

main()