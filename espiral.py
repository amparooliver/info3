from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import sys

initial_limit = 15  # Ajusta este valor según tu preferencia
position = [150, 150]  # Posición inicial (x, y)
scale_factor = 1

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(0.0, 300.0, 0.0, 300.0)

    glEnable(GL_BLEND)
    glEnable(GL_LINE_SMOOTH)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glHint(GL_LINE_SMOOTH_HINT, GL_NICEST)

def circle(x, y, radius, limit):
    a, b = 0, 0
    glColor3f(0.0, 0.0, 0.0)
    glPointSize(50)
    glLineWidth(5.5 + (scale_factor*5))  # Grosor de la línea vinculado al factor de escala
    glBegin(GL_LINE_STRIP)
    for i in range(int(limit * 20)):
        a += 0.1 * scale_factor
        b += 0.1 * scale_factor
        tx = x + b * math.cos(i * 0.05)
        ty = y + a * math.sin(i * 0.05)
        glVertex2f(tx, ty)
    glEnd()
    glLineWidth(1.0)

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    global position, initial_limit, scale_factor
    x, y = position
    circle(x, y, 1 * scale_factor, initial_limit)
    glFlush()

def keypress(key, x, y):
    global initial_limit, position, scale_factor
    if key == b'\x1b':
        sys.exit()
    elif key == b'q':
        initial_limit += 0.05
        draw()
    elif key == b'w':
        initial_limit -= 0.05
        draw()
    elif key == GLUT_KEY_UP:
        position[1] += 5
        draw()
    elif key == GLUT_KEY_DOWN:
        position[1] -= 5
        draw()
    elif key == GLUT_KEY_LEFT:
        position[0] -= 5
        draw()
    elif key == GLUT_KEY_RIGHT:
        position[0] += 5
        draw()
    elif key == b'm':
        scale_factor += 1
        draw()
    elif key == b'n':
        scale_factor -= 1
        draw()
    glutPostRedisplay()

def main():
    glutInit(sys.argv)
    glutInitWindowPosition(10, 10)
    glutInitWindowSize(500, 500)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutCreateWindow(b"Spiral")
    init()
    glutDisplayFunc(draw)
    glutKeyboardFunc(keypress)
    glutSpecialFunc(keypress)

    glutMainLoop()

if __name__ == "__main__":
    main()
