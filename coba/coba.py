from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def initFun():
    glClearColor(1.0,1.0,1.0,0.0)
    glColor3f(128.0,0.0, 0.0)
    glPointSize(5.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D (0.0,100.0,0.0,100.0)
    
def AlgDDA():
    #tentukan titik awal dan akhir
    x1 = 7
    y1 = -1
    x2 = -4
    y2 = 6
    x = x1
    y = y1

    #hitung dx dan dy
    dx = x2 - x1;
    dy = y2 - y1;

    #hitung steps
    if (dx > dy):
        steps = dx
    else:
        steps = dy;

    #hitung perubahan nilai x (x_inc) dan y (y_inc)
    x_inc = dx / steps
    y_inc = dy / steps

    #gambar titik awal
    glBegin(GL_POINTS);
    glVertex2i(x, y); #gambar titik awal

    #perulangan untuk menggambar titik-titik

    while x < x2:
        x += x_inc
        y += y_inc

    glEnd()
    glFlush()

if __name__ == '__main__':
    glutInit()
    glutInitWindowSize(800,800)
    glutInitWindowPosition(100,100)
    glutCreateWindow("Algoritma DDA")
    glutInitDisplayMode(GLUT_SINGLE| GLUT_RGBA)
    glutDisplayFunc(AlgDDA)
    initFun()
    glutMainLoop()
    
    
