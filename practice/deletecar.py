from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import time, math, sys

wheel_radius=20
angle=0
speed=2
car_x=-300

def init():
    glClearColor(1,1,1,1)
    gluOrtho2D(-300,300,-300,300)

def draw_circle(xc,yc,r):
    glBegin(GL_POLYGON)
    for i in range(361):
        glVertex2f(xc+r*math.cos(math.radians(i)),yc+r*math.sin(math.radians(i)))
    glEnd()

def draw_wheel(xc,yc,r):
    global car_x,angle
    glColor3f(0,1,0)
    glPushMatrix()
    glTranslatef(xc,yc,0)
    glRotatef(angle,0,0,1)
    draw_circle(0,0,r)
    glColor3f(0,0,0)
    for i in range(0,360,45):
        glBegin(GL_LINES)
        glVertex2f(0,0)
        glVertex2f(r*math.cos(math.radians(i)),r*math.sin(math.radians(i)))
        glEnd()
    glPopMatrix()

def draw_car():
    global car_x,angle
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0,0,1)
    glBegin(GL_QUADS)
    glVertex2f(car_x,-20)
    glVertex2f(car_x+120,-20)
    glVertex2f(car_x+120,20)
    glVertex2f(car_x,20)
    glEnd()
    glColor3f(1,0,0)
    glBegin(GL_QUADS)
    glVertex2f(car_x+30,20)
    glVertex2f(car_x+90,20)
    glVertex2f(car_x+90,40)
    glVertex2f(car_x+30,40)
    glEnd()
    draw_wheel(car_x+20,-20,wheel_radius)
    draw_wheel(car_x+100,-20,wheel_radius)
    glutSwapBuffers()

def animate(temp):
    global car_x,angle
    car_x+=speed
    angle-=speed*(360/(2*math.pi*wheel_radius))
    if car_x>300:
        car_x=-300
    glutPostRedisplay()
    glutTimerFunc(30,animate,0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(600,0)
    glutCreateWindow(b"Car")
    init()
    glutDisplayFunc(draw_car)
    glutTimerFunc(0,animate,0)
    glutMainLoop()
    
main()
