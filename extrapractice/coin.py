import math
import time
from OpenGL import * 
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
# Take input from user
x=0
y=0
r=40
orbit_r=100
angle=0
def circle():
	glColor3f(0,0,0.9)
	glBegin(GL_TRIANGLE_FAN)
	for i in range(0,361):
		glVertex2f(r*math.cos(math.pi*i/180),r*math.sin(math.pi*i/180))
	glEnd()
def orbit(x,y):
  glColor3f(1,1,0)
  glBegin(GL_LINE_LOOP)
  for i in range(0,361):
    glVertex2f(x+orbit_r*math.cos(math.pi*i/180),y+orbit_r*math.sin(math.pi*i/180))
  glEnd()

def ploat():
	glClear(GL_COLOR_BUFFER_BIT)
	orbit(0,0)
	glPushMatrix()
	glRotatef(angle,0,0,1)
	glTranslatef(70,70,1)
	glRotatef(angle,1,0,0)
	circle()
	glPopMatrix()
	glFlush()		
def animate(value):
	global angle	
	angle+=5
	if angle>=360:
		angle=0
	glutPostRedisplay()
	glutTimerFunc(50,animate,0)	
def init():
	glClearColor(1,1,1,0)
	gluOrtho2D(-300,300,-300,300)
def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGBA)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(600,0)
	glutCreateWindow(b'SAMPLE')
	glutDisplayFunc(lambda:ploat())
	glutTimerFunc(50,animate,0)	
	init()
	glutMainLoop()
main()