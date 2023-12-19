from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random
import math

# Posición inicial de la cámara
ojox, ojoy, ojoz = 1, 1, 2

# Tamaño de la ventana
width, height = 800, 800

# Posición inicial de la fuente de luz
light_position = [1.0, 1.0, 2.0, 0.0]

# Punto hacia el que apunta la luz
look_at_center = [0.0, 0.0, 0.0]

# Parámetros de la pirámide
largo = 0.35
cant_triangulos = 4
movEnX = 0
anguloy = 0
angulo_en_hipotenusa = 0

# Vértices de la hipotenusa de la pirámide
vertices_hipotenusa = [(0, largo, 0), (largo, 0, 0)]

# Función para dibujar los ejes
def ejes(largo):
    # EJE X
    glBegin(GL_LINES)
    glColor3f(1, 0, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(largo, 0, 0)

    # EJE Y
    glColor3f(0, 1, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(0, largo, 0)

    # EJE Z
    glColor3f(0, 0, 1)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 0, largo)
    glEnd()

# Función para dibujar una cara de la pirámide
def dibujar_cara(vertices, color):
    glColor3f(*color)
    glBegin(GL_TRIANGLES)
    for v in vertices:
        glVertex3f(*v)
    glEnd()

# Función para dibujar un triángulo
def triangulo(color):
    vertices = [(0, 0, 0), (largo, 0, 0), (0, largo, 0)]
    dibujar_cara(vertices, color)
    glFlush()

# Función para calcular el vector dirección entre dos puntos
def vector_direccion():
    global vertices_hipotenusa
    x1, y1, z1 = vertices_hipotenusa[0]
    x2, y2, z2 = vertices_hipotenusa[1]

    dx = x2 - x1
    dy = y2 - y1
    dz = z2 - z1

    longitud = math.sqrt(dx**2 + dy**2 + dz**2)

    if longitud != 0:
        dx /= longitud
        dy /= longitud
        dz /= longitud

    return (dx, dy, dz)

# Función para dibujar la pirámide
def piramide():
    colores = [
    (1.0, 0.6, 0.2),  # Naranja
    (1.0, 0.4, 0.8),  # Rosa
    (0.7, 0.2, 0.9),  # Violeta
    (0.4, 0.8, 0.4),  # Verde claro
    (0.2, 0.6, 0.2),  # Verde oscuro
    (1.0, 0.8, 0.0),  # Amarillo
    (0.8, 0.4, 0.2),  # Marrón
    # Puedes agregar más colores según tus preferencias
    ]
    angulo = 360 / cant_triangulos

    for i in range(cant_triangulos):
        color = (random.random(), random.random(), random.random())
        glPushMatrix()
        glRotate(angulo * i, 0, 1, 0)
        triangulo(colores[i % 7])
        glPopMatrix()

# Función para dibujar la pirámide rotando
def piramide_rotando():
    componentes = vector_direccion()
    alpha = math.degrees(math.atan2(componentes[1], componentes[0]))

    glPushMatrix()
    glTranslate(movEnX, 0, 0)
    glRotate(anguloy, 0, 1, 0)
    glRotate(alpha * angulo_en_hipotenusa, *componentes)
    piramide()
    glPopMatrix()

    glFlush()

# Función de visualización principal
def display():
    global ojox, ojoy, ojoz
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (width / height), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    gluLookAt(ojox, ojoy, ojoz, 0, 0, 0, 0.0, 1.0, 0.0)

    ejes(2)
    piramide_rotando()

    glutSwapBuffers()

# Función para manejar eventos de teclado
def keypress(key, x, y):
    global ojox, ojoz, cant_triangulos, movEnX, anguloy, angulo_en_hipotenusa
    print(f'key={key}')

    if key == b'x':
        movEnX += 0.25
    elif key == b'z':
        movEnX -= 0.25
    elif key == b'y':
        anguloy += 10
    elif key == b'r':
        angulo_en_hipotenusa += 1
    elif key == b'm':
        cant_triangulos += 1

    glutPostRedisplay()

# Función principal
def main():
    # Se inicializa glut
    glutInit(sys.argv)

    # Se configura la visualización (buffer doble, modo rgb de colores, Habilita el búfer de profundidad (z-buffer))
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)

    glutInitWindowSize(height, width)
    glutCreateWindow(b'Piramide de Triangulos - Parcial1')

    glEnable(GL_DEPTH_TEST)

    glutDisplayFunc(display)
    glutKeyboardFunc(keypress)
    glutMainLoop()

if __name__ == '__main__':
    main()
