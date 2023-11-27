from OpenGL.GL import *
from OpenGL.GLU import gluOrtho2D
from OpenGL.GLUT import *
from math import *

rotation_angle = 0.0  # Variable para el ángulo de rotación
angle_offset = 0  # Ángulo de separación entre las dos columnas

def draw_rounded_rectangle(x, y, width, height, radius, num_segments=100):
    glBegin(GL_QUADS)

    # Dibuja el cuerpo del rectángulo
    glColor3f(0.0, 0.5, 0.0)  # Verde oscuro
    glVertex2f(x + radius, y)
    glVertex2f(x + width - radius, y)
    glVertex2f(x + width - radius, y + height)
    glVertex2f(x + radius, y + height)

    # Dibuja los bordes ovalados
    for i in range(num_segments):
        theta = 2.0 * 3.1415926 * i / num_segments
        dx = radius * cos(theta)
        dy = radius * sin(theta)

        # Arco superior izquierdo
        glVertex2f(x + radius + dx, y + height - radius + dy)
        # Arco superior derecho
        glVertex2f(x + width - radius + dx, y + height - radius + dy)

        # Arco inferior derecho
        glVertex2f(x + width - radius + dx, y + radius + dy)
        # Arco inferior izquierdo
        glVertex2f(x + radius + dx, y + radius + dy)

    glEnd()

def rotate_rectangle():
    glTranslatef(0.2, 0, 0)  # Traslada el rectángulo
    glRotatef(rotation_angle, 0, 0, 1)  # Rota el rectángulo alrededor del eje Z

def display():
    global rotation_angle, angle_offset
    glClear(GL_COLOR_BUFFER_BIT)


    for i in range(4):
        # Dibuja la primera columna de rectángulos
        glPushMatrix()
        glTranslatef(0.2, 0, 0)
        glRotatef(rotation_angle - angle_offset, 0, 0, 1)  # Rota con el ángulo interno
        draw_rounded_rectangle(0, i * 0.16, 0.05, 0.15, 0.01)
        glPopMatrix()

        # Dibuja la segunda columna de rectángulos invertida
        glPushMatrix()
        #rotate_rectangle()
        glTranslatef(0.3, 0, 0)  # Ajusta la posición
        glRotatef(rotation_angle + angle_offset, 0, 0, 1)  # Rota con el ángulo interno
        draw_rounded_rectangle(0, i * 0.16, 0.05, 0.15, 0.01)
        glPopMatrix()

    # Muestra el ángulo en la ventana
    glColor3f(0.0, 0.0, 0.0)
    glWindowPos2f(10, 370)
    glutBitmapString(GLUT_BITMAP_HELVETICA_18, bytes(f"Angulo: {angle_offset*2}", 'utf-8'))


    glutSwapBuffers()

def special_keys(key, x, y):
    global rotation_angle, angle_offset
    if key == GLUT_KEY_LEFT:
        angle_offset += 5.0  # Disminuye el ángulo de separación al presionar la tecla izquierda
    elif key == GLUT_KEY_RIGHT:
        angle_offset -= 5.0  # Aumenta el ángulo de separación al presionar la tecla derecha
    glutPostRedisplay()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(400, 400)
    glutCreateWindow(b'Rectangulo ')

    glClearColor(1.0, 1.0, 1.0, 1.0)  # Fondo blanco
    gluOrtho2D(0.0, 1.0, 0.0, 1.0)  # Establece la matriz de proyección

    glutDisplayFunc(display)
    glutSpecialFunc(special_keys)  # Registra la función de teclas especiales
    glutMainLoop()

main()
