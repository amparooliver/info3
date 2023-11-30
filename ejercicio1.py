from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Número de triángulos en la base
n = 11

def draw_triangle(x, y, size):
    glBegin(GL_TRIANGLES)
    glColor3f(0.5, 0.8, 1.0)
    glVertex2f(x, y)
    glVertex2f(x + size, y)
    glVertex2f(x + size / 2, y + size * 0.866)  # Altura del triángulo equilátero
    glEnd()

def draw_pyramid():
    size = 0.1  # Tamaño de los triángulos
    for i in range(n):
        row_offset = i * size * 0.866  # Desplazamiento vertical para cada fila
        for j in range(n - i):
            x = j * size + i * size / 2
            y = row_offset
            draw_triangle(x, y, size)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_pyramid()
    glutSwapBuffers()

def main():
    size = 0.1  # Tamaño de los triángulos
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(400, 400)
    glutCreateWindow(b'Piramide de Triangulos')

    glClearColor(1.0, 1.0, 1.0, 1.0)  # Fondo blanco
    gluOrtho2D(0.0, n * size, 0.0, n * size * 0.866)  # Establece la matriz de proyección

    glutDisplayFunc(display)
    glutMainLoop()

main()
