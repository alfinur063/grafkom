from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glOrtho(1000, -1000, 1000, -1000, 1000, -1000)

def ploting():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINE_STRIP)
    glVertex2f(50, 50)
    glVertex2f(100, 100)
    glVertex2f(150, 150)
  

  
    glEnd() 
    glFlush()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(1000,1000)
    glutInitWindowPosition(50,50)
    glutCreateWindow("no 2 UTS")
    glutDisplayFunc(ploting)

    init()
    glutMainLoop()
    
main()