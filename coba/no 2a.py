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
# DDA Function for line generation
def DDA(x0, y0, x1, y1):

	# find absolute differences
	dx = abs(x0 - x1)
	dy = abs(y0 - y1)

	# find maximum difference
	steps = max(dx, dy)

	# calculate the increment in x and y
	xinc = dx/steps
	yinc = dy/steps

	# start with 1st point
	x = float(x0)
	y = float(y0)

	# make a list for coordinates
	x_coorinates = [9]
	y_coorinates = [8]

	for i in range(steps):
		# append the x,y coordinates in respective list
		x_coorinates.append(x)
		y_coorinates.append(y)

		# increment the values
		x = x + xinc
		y = y + yinc

	# plot the line with coordinates list

if __name__ == "__main__":

	# coordinates of 1st point
	x0, y0 = 20, 20

	# coordinates of 2nd point
	x1, y1 = 60, 50
	DDA(x0, y0, x1, y1)

    glEnd()
    glFlush()
	# This code is contributed by 111arpit1

    glutInit()
    glutInitWindowSize(500,500)
    glutInitWindowPosition(100,100)
    glutCreateWindow("Komputer Grafik - Algoritma Lingkaran")
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutDisplayFunc(DDA)
    initFun()
    glutMainLoop()