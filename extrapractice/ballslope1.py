from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys, time, math

ball_x = -300
ball_y = 150
ball_rotation = 0  # rotation angle of the ball

def init():
    glClearColor(1, 1, 1, 1)
    gluOrtho2D(-400, 400, -400, 400)

def draw_ball():
    global ball_rotation
    glPushMatrix()
    glTranslatef(ball_x, ball_y, 0)  # move to ball position
    glRotatef(ball_rotation, 0, 0, 1)  # rotate ball about its center
    
    # Draw the outer circle (wheel rim)
    glColor3f(0, 0, 1)
    glBegin(GL_LINE_LOOP)
    for i in range(360):
        glVertex2f(50*math.cos(math.radians(i)), 50*math.sin(math.radians(i)))
    glEnd()

    # Draw spokes
    glColor3f(1, 0, 0)  # white spokes
    for i in range(0,360,45):
        glBegin(GL_LINES)
        glVertex2f(0, 0)
        glVertex2f(50 * math.cos(math.radians( i)), 50 * math.sin(math.radians(i)))
        glEnd()

    glPopMatrix()


def ground():
    glColor3f(1, 0, 0)
    glLineWidth(3)
    glBegin(GL_LINES)
    glVertex2f(-300, -300)
    glVertex2f(300, -300)
    glEnd()

def draw_slope1():
    glColor3f(1, 0, 0)
    glLineWidth(3)
    glBegin(GL_LINE_LOOP)
    glVertex2f(-300, -300)
    glVertex2f(-100, -300)
    glVertex2f(-300, 100)
    glEnd()

def draw_slope2():
    glColor3f(1, 0, 0)
    glLineWidth(3)
    glBegin(GL_LINE_LOOP)
    glVertex2f(100, -300)
    glVertex2f(300, -300)
    glVertex2f(300, 100)
    glEnd()

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    ground()
    draw_slope1()
    draw_slope2()
    draw_ball()
    glutSwapBuffers()

def animate(temp):
    global ball_x, ball_y, ball_rotation
    
    # Compute distance moved this frame
    old_x = ball_x
    
    if ball_x <= -100:
        ball_x += 5
        ball_y = (-2 * ball_x - 500) + 50
    elif ball_x > -100 and ball_x <= 100:
        ball_x += 4
        ball_y = -300 + 50  # staying on flat ground here
    elif ball_x > 100 and ball_x <= 300:
        ball_x += 1
        ball_y = (2 * ball_x - 500) + 50
    
    distance_moved = abs(ball_x - old_x)
    # Update rotation angle based on distance moved and ball's circumference
    circumference = 2 * math.pi * 50  # radius 50
    rotation_degrees = (distance_moved / circumference) * 360
    ball_rotation = (ball_rotation + rotation_degrees ) % 360 # keep in 0-360
    
    glutPostRedisplay()
    glutTimerFunc(30, animate, 0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(600, 0)
    glutCreateWindow(b"Ball Rolling on Slope with Rotation")
    glutDisplayFunc(draw)
    glutTimerFunc(0, animate, 0)
    init()
    glutMainLoop()

main()
