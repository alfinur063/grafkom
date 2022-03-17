from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def initFun():
    glClearColor(1.0,1.0,1.0,0.0)
    glColor3f(128.0,0.0, 0.0)
    glPointSize(5.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D (0.0,500.0,0.0,500.0)
    
def AlgDDA():
    #tentukan titik awal dan akhir
    x1 = 7
    y1 = -1
    x2 = -4
    y2 = 6
    x = x1
    y = y1

    #hitung dx dan dy
    dx = (x2 - x1)
    dy = (y2 - y1)
    
    #hitung p 
    d1 = 2* dy
    d2 = 2* (dx-dy)
    p = d1 - d2
    
    #tentukan titik awal dan akhir
    if (x1 > x2):
        x = x2
        y = y2
        xend = x1
    else:
        x = x1
        y = y1
        xend = x2
    

    #gambar titik awal
    glBegin(GL_POINTS)
    glVertex2i(x, y)

    #perulangan untuk menggambar titik-titik 
    while (x < xend):
        x = x+1
        if (p < 0):
            p = p -  d1
            y = y
            x = x
        else:
            if (y1 > y2):
                y = y-1
            else:
                y = y+1
            p = p + d1
            y=y
            x=x+1
        glVertex2i(x, y)

    glEnd()
    glFlush()

if __name__ == '__main__':
    glutInit()
    glutInitWindowSize(500,500)
    glutInitWindowPosition(100,100)
    glutCreateWindow("Komputer Grafik - Algoritma Lingkaran")
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutDisplayFunc(AlgDDA)
    initFun()
    glutMainLoop()