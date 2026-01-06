from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT  import *
import math

wheel_angle=0
angle=0
orbit_r=180
def init():
  glClearColor(0,0,0,1)
  gluOrtho2D(-300,300,-300,300)
def circle(x,y):
  glColor3f(1,0,0)
  glLineWidth(2)
  glBegin(GL_TRIANGLE_FAN)
  for i in range(0,361):
    glVertex2f(x+40*math.cos(math.pi*i/180),y+40*math.sin(math.pi*i/180))
  glEnd()
def orbit(x,y):
  glColor3f(1,1,0)
  glBegin(GL_LINE_LOOP)
  for i in range(0,361):
    glVertex2f(x+orbit_r*math.cos(math.pi*i/180),y+orbit_r*math.sin(math.pi*i/180))
  glEnd()   
def draw():
  glClear(GL_COLOR_BUFFER_BIT)  
  circle(0,0)
  orbit(0,0)
  glPushMatrix()
  glRotatef(angle,0,0,1)
  glTranslatef(50, 70, 0)
  circle(50,70)
  wheel()
  glPopMatrix()
  glFlush()
def update(value):
  global angle
  angle+=5
  if angle>=360:
    angle=0
  glutPostRedisplay()
  glutTimerFunc(60,update,0)    
def wheel():
  glColor3f(0,1,0)
  glLineWidth(5)
  glBegin(GL_LINES)
  for i in range(7):
    theta=math.radians(wheel_angle+i*90)
    glVertex2f(50,70)
    glVertex2f(50+40*math.cos(theta),70+40*math.sin(theta))
  glEnd()    
def main():
  glutInit(sys.argv)
  glutInitDisplayMode(GL_RGBA)
  glutInitWindowSize(500,500)
  glutInitWindowPosition(600,0)
  glutCreateWindow(b'flower animation')
  glutDisplayFunc(draw)
  glutTimerFunc(60,update,0)   
  init()
  glutMainLoop()
main()