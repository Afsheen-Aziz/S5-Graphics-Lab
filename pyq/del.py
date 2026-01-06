from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

r = 25
x = -250
y = 10
speed = 10.0
m = 0.75
loss = 0.99
top = 250
angle_spin = 0

phase = 0  # 0 = down right, 1 = flat right, 2 = up right,
            # 3 = down left, 4 = flat left, 5 = up left

def init():
    glClearColor(1, 1, 1, 1)
    gluOrtho2D(-300, 300, -300, 300)

def draw_slope():
    glColor3f(0, 0, 0)
    glLineWidth(3)
    glBegin(GL_LINES)
    glVertex2f(-250, 0)
    glVertex2f(-50, -150)
    glVertex2f(-50, -150)
    glVertex2f(50, -150)
    glVertex2f(50, -150)
    glVertex2f(250, 0)
    glEnd()

def draw_ball(x, y):
    glColor3f(1, 0, 0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x, y)
    for i in range(361):
        angle = math.radians(i)
        glVertex2f(x + r * math.cos(angle), y + r * math.sin(angle))
    glEnd()

def draw_spokes():
    glColor3f(0,0,0)
    glBegin(GL_LINES)
    glVertex2f(0,27)
    glVertex2f(0,-27)
    glVertex2f(27,0)
    glVertex2f(-27,0)
    glEnd()


def display():
    global x,y
    glClear(GL_COLOR_BUFFER_BIT)
    draw_slope()
    glPushMatrix()
    glTranslatef(x,y,0)
    glRotatef(angle_spin,0,0,1)
    draw_ball(0,0)
    draw_spokes()
    glPopMatrix()
    glFlush()

def animate(val):
    global x, y, speed, phase, m ,loss,top, angle_spin

    # --- DOWN RIGHT ---
    if phase == 0:
        x+= speed
        y = -m * (x + 250) + 25
        if x >= -50:
            phase = 1

    # --- FLAT RIGHT ---
    elif phase == 1:
        x += speed
        y = -150 + 25
        speed *= loss
        top *= loss
        if x >= 50:
            phase = 2

    # --- UP RIGHT ---
    elif phase == 2:
        x += speed
        y = m * (x - 50) - 150 + 25
        if x >= top:
            phase = 3


    # --- DOWN LEFT ---
    elif phase == 3:
        x -= speed
        y = m * (x - 50) - 150 + 25
        if x <= 50:
            phase = 4

    # --- FLAT LEFT ---
    elif phase == 4:
        x -= speed
        y = -150 + 25
        speed *= loss
        top *= loss
        if x <= -50:
            phase = 5

    # --- UP LEFT ---
    elif phase == 5:
        x -= speed
        y = -m * (x + 250) + 25
        if x <= -top:
            phase = 0  # repeat loop


    if speed < 0.2:
        speed = 0

    angle_spin += speed*3
    if angle_spin > 360:
        angle_spin = -360

    glutPostRedisplay()
    glutTimerFunc(50, animate, 0)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"Ball Rolling in Pit - 6 Phases")
    init()
    glutDisplayFunc(display)
    glutTimerFunc(0, animate, 0)
    glutMainLoop()

main()