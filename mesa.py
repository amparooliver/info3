from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Tamaño de la ventana
width, height = 800, 800

# Posición inicial de la cámara
ojox, ojoy, ojoz = 1, 1, 5

# Posición inicial de la fuente de luz
light_position = [1.0, -10.0, 2.0, 0.0]

# Ángulos de rotación para la luz
light_rotation_x = 0.0
light_rotation_y = 0.0

def ejes(largo):

    glDisable(GL_LIGHTING)  # Desactivar iluminación para los ejes

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

    glEnable(GL_LIGHTING)  # Volver a activar la iluminación

def draw_table():
    # Configuración de propiedades materiales para la mesa
    mesa_ambient = [0.5, 0.35, 0.05, 1.0]
    mesa_diffuse = [0.5, 0.35, 0.05, 1.0]
    mesa_specular = [0.5, 0.5, 0.5, 1.0]
    mesa_shininess = 32.0

    glMaterialfv(GL_FRONT, GL_AMBIENT, mesa_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mesa_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mesa_specular)
    glMaterialf(GL_FRONT, GL_SHININESS, mesa_shininess)

    # Dibujar la parte superior de la mesa
    glColor3f(0.5, 0.35, 0.05)  # Color marrón
    glPushMatrix()
    glScalef(1.5, 0.1, 1.0)
    glutSolidCube(1.0)
    glPopMatrix()

    # Dibujar las patas de la mesa
    glColor3f(0.5, 0.35, 0.05)  # Color marrón
    glPushMatrix()
    glTranslatef(0.6, -0.4, 0.4)
    glScalef(0.1, 0.8, 0.1)
    glutSolidCube(1.0)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.6, -0.4, -0.4)
    glScalef(0.1, 0.8, 0.1)
    glutSolidCube(1.0)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-0.6, -0.4, 0.4)
    glScalef(0.1, 0.8, 0.1)
    glutSolidCube(1.0)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-0.6, -0.4, -0.4)
    glScalef(0.1, 0.8, 0.1)
    glutSolidCube(1.0)
    glPopMatrix()


def display():
    global ojox, ojoy, ojoz, light_position, light_rotation_x, light_rotation_y

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    gluLookAt(ojox, ojoy, ojoz, 0, 0, 0, 0.0, 1.0, 0.0)

    # Configuración del color ambiente
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, [0.2, 0.2, 0.2, 1.0])

    ejes(2)

    # Configuración de la luz
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)

    # Rotación de la luz
    glPushMatrix()
    glRotatef(light_rotation_x, 1.0, 0.0, 0.0)
    glRotatef(light_rotation_y, 0.0, 1.0, 0.0)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glPopMatrix()

    # Dibujar la mesa
    draw_table()

    glutSwapBuffers()

def keypress(key, x, y):
    global light_position, light_rotation_x, light_rotation_y

    # Mover la fuente de luz
    if key == b'a':
        light_position[0] -= 0.1
    elif key == b'd':
        light_position[0] += 0.1
    elif key == b's':
        light_position[1] -= 0.1
    elif key == b'w':
        light_position[1] += 0.1

    glutPostRedisplay()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(height, width)
    glutCreateWindow(b'Mesa 3D')

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (width / height), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

    # Posicionar la fuente de luz inicialmente
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)

    glutDisplayFunc(display)
    glutKeyboardFunc(keypress)
    glutMainLoop()

if __name__ == '__main__':
    main()
