from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glOrtho(-6, 6, -6, 6, -1, 1)
    
def AlgDDA():
    
    x1 = 7
    y1 = -1
    x2 = -4
    y2 = -6
    x = x1
    y = y1

    dx = x2 - x1;
    dy = y2 - y1;

    
    if (dx > dy):
        steps = dx
    else:
        steps = dy;

    
    x_inc = dx / steps
    y_inc = dy / steps

    
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINE_STRIP)
    glVertex2f(-4.0, -6.0)
    glVertex2f(-3.0, -5.5)
    glVertex2f(-2.0, -5.1)
    glVertex2f(-1.0, -4.65)
    glVertex2f(0.0, -4.2)
    glVertex2f(1.0, -3.75)
    glVertex2f(2.0, -3.3)
    glVertex2f(3.0, -2.85)
    glVertex2f(4.0, -2.4)
    glVertex2f(5.0, -1.95)
    glVertex2f(6.0, -1.5)
    glVertex2f(7.0, -1.0)
    glEnd()
    glFlush()


if __name__ == '__main__':
    glutInit()
    glutInitWindowSize(800,800)
    glutInitWindowPosition(100,100)
    glutCreateWindow("Algoritma DDA")
    glutInitDisplayMode(GLUT_SINGLE| GLUT_RGBA)
    glutDisplayFunc(AlgDDA)
    init()
    glutMainLoop()
    
    
