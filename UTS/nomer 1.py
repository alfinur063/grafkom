from math import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random
import sys
import math

xAxisLimits = [-300, 300]
yAxisLimits = [-300, 300]


def randomColor():
    return [i/255 for i in random.choices(range(256), k=3)]

def randomEllipseRadius():
    return random.randint(0,(xAxisLimits[1]-xAxisLimits[0])/2)

def randomCenter():
    return [i for i in random.choices(range(-150,150),k=2)]

def generalEllipseY(center, rx, ry, x):
    cal = (ry/rx)*(((rx)**2-(center[0]-x)**2)**0.5)
    return [center[1] + cal, center[1]-cal]


def generalEllipseX(center, rx, ry, y):
    cal = (rx/ry)*(((ry)**2-(center[1]-y)**2)**0.5)
    return [center[0] + cal, center[0]-cal]


def EllipseParaX(center, rx, ry, theta):
    return int(center[0] + rx * cos(theta))


def EllipseParaY(center, rx, ry, theta):
    return int(center[1]+ry*sin(theta))


def draw():
    glClearColor(1.0, 1.0, 1.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT)
    drawEllipseGeneral(randomCenter(), randomEllipseRadius(), randomEllipseRadius(), randomColor())
    glFlush()


def drawEllipseGeneral(center, xL, yL, color):
    glColor3f(color[1], color[1], color[2])
    cx, cy = center[0], center[1]
    glBegin(GL_POINTS)
    if xL >= yL:
        for i in range(cx-xL, int(cx+xL)+1):
            l = generalEllipseY(center, xL, yL, i)
            glVertex2i(i, int(l[0]))
            glVertex2i(i, int(l[1]))
    else:
        for i in range(cy-yL, int(cy+yL)+1):
            l = generalEllipseX(center, xL, yL, i)
            glVertex2i(int(l[0]), i)
            glVertex2i(int(l[1]), i)
    glEnd()




glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowPosition(50, 50)
glutInitWindowSize(1000, 720)
glutCreateWindow("Ellipse")
glClearColor(1, 5, 1, 3)
glMatrixMode(GL_PROJECTION)
gluOrtho2D(xAxisLimits[0], xAxisLimits[1], yAxisLimits[0], yAxisLimits[1])
glutDisplayFunc(draw)
glutMainLoop()

