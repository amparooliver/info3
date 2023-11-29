from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Tamaño de la ventana
width, height = 800, 800

# Posición inicial de la cámara
ojox, ojoy, ojoz = 4.0, 4.0, 5.0

# Posición inicial de la fuente de luz
light_position = [10.0, 10.5, 1.0, 1.0]

# Ángulos de rotación para la luz y el cubo
light_rotation_x = 0.0
light_rotation_y = 0.0
cube_rotation_angle = 0.0

class RubikCube:
    def __init__(self, size=3):
        self.size = size
        self.colors = [
            (1, 0, 0),  # Rojo
            (0, 1, 0),  # Verde
            (0, 0, 1),  # Azul
            (1, 1, 0),  # Amarillo
            (1, 0.5, 0),  # Naranja
            (1, 1, 1)  # Blanco
        ]

    def draw_small_cube(self, x, y, z, size, color_index):
        half_size = size / 2

        # Asegurarse de que el índice esté en el rango correcto
        color_index = color_index % len(self.colors)
        color = self.colors[color_index]

        glColor3f(*color)

        glBegin(GL_QUADS)
        # Cara frontal
        glNormal3f(0, 0, 1)
        glVertex3f(x - half_size, y - half_size, z + half_size)
        glVertex3f(x + half_size, y - half_size, z + half_size)
        glVertex3f(x + half_size, y + half_size, z + half_size)
        glVertex3f(x - half_size, y + half_size, z + half_size)

        # Cara posterior
        glNormal3f(0, 0, -1)
        glVertex3f(x - half_size, y - half_size, z - half_size)
        glVertex3f(x + half_size, y - half_size, z - half_size)
        glVertex3f(x + half_size, y + half_size, z - half_size)
        glVertex3f(x - half_size, y + half_size, z - half_size)

        # Cara izquierda
        glNormal3f(-1, 0, 0)
        glVertex3f(x - half_size, y - half_size, z - half_size)
        glVertex3f(x - half_size, y - half_size, z + half_size)
        glVertex3f(x - half_size, y + half_size, z + half_size)
        glVertex3f(x - half_size, y + half_size, z - half_size)

        # Cara derecha
        glNormal3f(1, 0, 0)
        glVertex3f(x + half_size, y - half_size, z - half_size)
        glVertex3f(x + half_size, y - half_size, z + half_size)
        glVertex3f(x + half_size, y + half_size, z + half_size)
        glVertex3f(x + half_size, y + half_size, z - half_size)

        # Cara superior
        glNormal3f(0, 1, 0)
        glVertex3f(x - half_size, y + half_size, z - half_size)
        glVertex3f(x + half_size, y + half_size, z - half_size)
        glVertex3f(x + half_size, y + half_size, z + half_size)
        glVertex3f(x - half_size, y + half_size, z + half_size)

        # Cara inferior
        glNormal3f(0, -1, 0)
        glVertex3f(x - half_size, y - half_size, z - half_size)
        glVertex3f(x + half_size, y - half_size, z - half_size)
        glVertex3f(x + half_size, y - half_size, z + half_size)
        glVertex3f(x - half_size, y - half_size, z + half_size)

        glEnd()

    def draw_cube(self):
        cube_size = 1.0
        half_cube_size = cube_size / 2

        for i in range(self.size):
            for j in range(self.size):
                for k in range(self.size):
                    color_index = (i * self.size + j) * self.size + k

                    x = (j - self.size / 2) * cube_size
                    y = (i - self.size / 2) * cube_size
                    z = (k - self.size / 2) * cube_size

                    self.draw_small_cube(x, y, z, cube_size, color_index)

    def rotate_internal_cubes(self, angle, axis):
        # Rotar el conjunto interno del cubo
        glTranslatef(0.5, 0.5, 0.5)  # Trasladar al centro del cubo
        glRotatef(angle, *axis)
        glTranslatef(-0.5, -0.5, -0.5)  # Trasladar de vuelta al lugar original

    def rotate_cube(self, angle, axis):
        glRotatef(angle, *axis)

rubik_cube = RubikCube()

def ejes(largo):
    # Desactiva la iluminación para dibujar los ejes
    glDisable(GL_LIGHTING)

    # Inicia el dibujo de líneas
    glBegin(GL_LINES)

    # Eje X (rojo)
    glColor3f(1, 0, 0)
    glVertex3f(0, 0, 0)     # Punto de inicio del eje X
    glVertex3f(largo, 0, 0)  # Punto final del eje X
    # Eje Y (verde)
    glColor3f(0, 1, 0)
    glVertex3f(0, 0, 0)     # Punto de inicio del eje Y
    glVertex3f(0, largo, 0)  # Punto final del eje Y
    # Eje Z (azul)
    glColor3f(0, 0, 1)
    glVertex3f(0, 0, 0)     # Punto de inicio del eje Z
    glVertex3f(0, 0, largo)  # Punto final del eje Z

    # Finaliza el dibujo de líneas
    glEnd()

    # Vuelve a activar la iluminación
    glEnable(GL_LIGHTING)


def display():
    global ojox, ojoy, ojoz, light_position, light_rotation_x, light_rotation_y, cube_rotation_angle

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    gluLookAt(ojox, ojoy, ojoz, 0, 0, 0, 0.0, 1.0, 0.0)

    # Setear luz
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, [0.2, 0.2, 0.2, 1.0])

    # Material
    glEnable(GL_COLOR_MATERIAL)

    # Este define qué partes afectan la iluminación
    # GL_FRONT solo a las caras frontales
    # Color ambiental y color difuso afectarán el color del material
    glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)

    # Dibujar ejes
    ejes(10)

    # Habilitar luces y fuente de luz
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)

    # Rotar luz
    glPushMatrix()
    glRotatef(light_rotation_x, 1.0, 0.0, 0.0)
    glRotatef(light_rotation_y, 0.0, 1.0, 0.0)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glPopMatrix()

    # Rotar cubo
    glPushMatrix()
    rubik_cube.rotate_internal_cubes(cube_rotation_angle, (0, 1, 0))
    rubik_cube.draw_cube()
    glPopMatrix()

    glutSwapBuffers()

def keypress(key, x, y):
    global light_position, light_rotation_x, light_rotation_y, cube_rotation_angle

    # Control de la posición de la luz en el eje X
    if key == b'a':
        light_position[0] -= 0.1  # Mueve la luz hacia la izquierda
    elif key == b'd':
        light_position[0] += 0.1  # Mueve la luz hacia la derecha

    # Control de la posición de la luz en el eje Y
    elif key == b's':
        light_position[1] -= 0.1  # Mueve la luz hacia abajo
    elif key == b'w':
        light_position[1] += 0.1  # Mueve la luz hacia arriba

    # Control de la rotación del cubo interno
    elif key == b'u':
        cube_rotation_angle += 5.0  # Rota el conjunto interno en sentido antihorario
    elif key == b'j':
        cube_rotation_angle -= 5.0  # Rota el conjunto interno en sentido horario

    # Actualiza la escena después de los cambios
    glutPostRedisplay()

def main():
    # Inicializar la aplicación GLUT
    glutInit(sys.argv)

    # Configurar el modo de visualización con doble búfer, RGB y profundidad
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)

    # Configurar el tamaño de la ventana
    glutInitWindowSize(height, width)

    # Crear la ventana con el título "Cubo de Rubik 3D"
    glutCreateWindow(b'Cubo de Rubik 3D - Amparo')

    # Habilitar la prueba de profundidad y la iluminación
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

    # Configurar la perspectiva de la cámara
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (width / height), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

    # Configurar la posición de la fuente de luz
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)

    # Establecer las funciones de visualización y manejo de teclado
    glutDisplayFunc(display)
    glutKeyboardFunc(keypress)

    # Iniciar el bucle principal de GLUT
    glutMainLoop()

if __name__ == '__main__':
    main()
