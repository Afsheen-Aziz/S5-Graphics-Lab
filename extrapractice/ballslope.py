from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys,time,math

ball_x=-300
ball_y=150
def init():
    glClearColor(1,1,1,1)
    gluOrtho2D(-400,400,-400,400)

def ball():
    glBegin(GL_TRIANGLE_FAN)
    for i in range(360):
        glVertex2f(ball_x+(50*math.cos(math.radians(i))),ball_y+(50*math.sin(math.radians(i))))
    glEnd()
def ground():
    glColor3f(1,0,0)
    glLineWidth(3)
    glBegin(GL_LINES)
    glVertex2f(-300,-300)
    glVertex2f(300,-300)
    glEnd()

def draw_slope1():
    glColor3f(1,0,0)
    glLineWidth(3)
    glBegin(GL_LINE_LOOP)
    glVertex2f(-300,-300)
    glVertex2f(-100,-300)
    glVertex2f(-300,100)
    glEnd()

def draw_slope2():
    glColor3f(1,0,0)
    glLineWidth(3)
    glBegin(GL_LINE_LOOP)
    glVertex2f(100,-300)
    glVertex2f(300,-300)
    glVertex2f(300,100)
    glEnd()

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    ground()
    draw_slope1()
    draw_slope2()
    glPushMatrix()
    glPopMatrix()
    ball()
    glutSwapBuffers()


def animate(temp):
    global ball_x, ball_y
    if ball_x <= -100:
        ball_x += 5
        ball_y = (-2 * ball_x - 500) + 50
    if ball_x>=-100 and ball_x<=100:
        ball_x+=4
    if ball_x>=100 and ball_x<=300:
        ball_x+=1
        ball_y = (2 * ball_x - 500) + 50
    glutPostRedisplay()
    glutTimerFunc(30, animate, 0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(600,0)
    glutCreateWindow(b"Ball Rolling on Slope")
    glutDisplayFunc(lambda:draw())
    glutTimerFunc(0,animate,0)
    init()
    glutMainLoop()
main()
