import sys, math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Global variables
car_x = -300       # starting x position of the car
wheel_angle = 0    # rotation of wheels
speed = 2          # car movement speed
wheel_radius = 20  # radius of wheels

def init():
    glClearColor(1, 1, 1, 1) 
    gluOrtho2D(-300, 300, -300, 300) 

# Draw a circle (used for wheels)
def draw_circle(xc, yc, r):
    glBegin(GL_POLYGON)
    for theta in range(0, 360, 5):
        x = r * math.cos(math.radians(theta))
        y = r * math.sin(math.radians(theta))
        glVertex2f(xc + x, yc + y)
    glEnd()

# Draw a wheel at given position
def draw_wheel(xc, yc, r):
    glColor3f(0, 0, 0)  # black wheel
    glPushMatrix()
    glTranslatef(xc, yc, 0)
    glRotatef(wheel_angle, 0, 0, 1)  # rotate the wheel
    draw_circle(0, 0, r)
    # add simple spokes
    glColor3f(1, 1, 1)
    for i in range(0, 360, 45):
        glBegin(GL_LINES)
        glVertex2f(0, 0)
        glVertex2f(r * math.cos(math.radians(i)), r * math.sin(math.radians(i)))
        glEnd()
    glPopMatrix()

# Draw the car body
def draw_car():
    global car_x, wheel_angle
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(0, 0, 1)  # blue car body
    # Draw car rectangle
    glBegin(GL_QUADS)
    glVertex2f(car_x+30, 20)
    glVertex2f(car_x+90, 20)
    glVertex2f(car_x+90 , 40)
    glVertex2f(car_x+30, 40)
    glEnd()

    glColor3f(1, 0, 0)  # red car body
    # Draw car rectangle
    glBegin(GL_QUADS)
    glVertex2f(car_x, -20)
    glVertex2f(car_x + 120, -20)
    glVertex2f(car_x + 120, 20)
    glVertex2f(car_x, 20)
    glEnd()

    # Draw wheels
    draw_wheel(car_x + 20, -20, wheel_radius)  # front wheel
    draw_wheel(car_x + 100, -20, wheel_radius) # rear wheel

    glutSwapBuffers()

# Animation function
def animate(temp):
    global car_x, wheel_angle
    car_x += speed               # move the car
    wheel_angle -= speed * 360 / (2 * math.pi * wheel_radius)  # rotate wheels based on distance traveled

    # Reset car position if it goes off screen
    if car_x > 300:
        car_x = -300

    glutPostRedisplay()
    glutTimerFunc(30, animate, 0)  # update every 30 ms

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(600, 0)
    glutCreateWindow(b"Car Animation")
    glutDisplayFunc(draw_car)
    glutTimerFunc(0, animate, 0)
    init()
    glutMainLoop()

main()
