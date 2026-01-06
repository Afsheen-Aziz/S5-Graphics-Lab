from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys, math

# Pendulum & ball parameters
angle, direction = 0, 1
length = 350
ball_x, ball_y = 120, -150
ball_dx, ball_hit = 0, False

def init():
    glClearColor(1, 1, 1, 1)
    gluOrtho2D(-300, 300, -300, 300)

def circle(x, y, r, color):
    glColor3f(*color)
    glBegin(GL_TRIANGLE_FAN)
    for i in range(360):
        glVertex2f(x + r * math.cos(math.radians(i)),
                   y + r * math.sin(math.radians(i)))
    glEnd()

def draw():
    global angle, direction, ball_x, ball_y, ball_dx, ball_hit

    glClear(GL_COLOR_BUFFER_BIT)

    # Pendulum position
    pivot_x, pivot_y = 0, 200
    bob_x = pivot_x + length * math.sin(math.radians(angle))
    bob_y = pivot_y - length * math.cos(math.radians(angle))

    # Draw ground, string, bob, and ball
    glColor3f(0, 0, 0)
    glBegin(GL_LINES)
    glVertex2f(-300, -180)
    glVertex2f(300, -180)
    glVertex2f(pivot_x, pivot_y)
    glVertex2f(bob_x, bob_y)
    glEnd()

    circle(bob_x, bob_y, 25, (0, 0, 1))
    circle(ball_x, ball_y, 35, (1, 0, 0))

    # Collision detection
    if not ball_hit:
        dx, dy = bob_x - ball_x, bob_y - ball_y
        if math.hypot(dx, dy) < 60:
            ball_hit, ball_dx = True, 15

    # Ball motion
    if ball_hit:
        ball_x += ball_dx
        ball_dx *= 0.93

    glutSwapBuffers()

def animate(value):
    global angle, direction
    angle += direction * 2
    if abs(angle) >= 60:
        direction *= -1
    glutPostRedisplay()
    glutTimerFunc(30, animate, 0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"Simple Pendulum Ball Hit")
    init()
    glutDisplayFunc(draw)
    glutTimerFunc(0, animate, 0)
    glutMainLoop()

main()
