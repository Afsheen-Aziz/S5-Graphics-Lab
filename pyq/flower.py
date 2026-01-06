from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys, math

fangle=0
petal_radius = 50
petal_distance = 50

petal_colors = [
    (1, 0, 0),    
    (0, 1, 0),
    (0, 0, 1),
    (1, 1, 0.0),
    (0, 1, 1),
]

current_petal = 0

def draw_circle(cx, cy, r, color):
    glColor3f(*color)
    glLineWidth(4)
    glBegin(GL_LINE_LOOP)
    for i in range(360):
        angle = math.radians(i)
        glVertex2f(cx + r * math.cos(angle), cy + r * math.sin(angle))
    glEnd()

def draw():
    global current_petal,fangle
    glClear(GL_COLOR_BUFFER_BIT)
    glPushMatrix()
    glRotatef(fangle,0,0,1)

    # Draw petals
    for i in range(current_petal):
        angle = math.radians(360 * i / 5)
        px = petal_distance * math.cos(angle)
        py = petal_distance * math.sin(angle)
        color = petal_colors[i % 5]
        draw_circle(px, py, petal_radius, color)
    glPopMatrix()
    glutSwapBuffers()

def animate(value):
    global current_petal,fangle
    
    if current_petal < 5:
        current_petal += 1
    if current_petal==5:
        current_petal=5
        fangle+=10
        if fangle>=360:
            fangle-=360
    glutPostRedisplay()
    glutTimerFunc(500, animate, 0)

def init():
    glClearColor(1, 1, 1, 1)
    gluOrtho2D(-120, 120, -120, 120)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(450, 450)
    glutCreateWindow(b"Overlapping Circle Flower Animation")
    init()
    glutDisplayFunc(draw)
    glutTimerFunc(0, animate, 0)
    glutMainLoop()

main()
