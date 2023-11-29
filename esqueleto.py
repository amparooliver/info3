from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Tamaño de la ventana
width, height = 800, 800

# Posición inicial de la cámara
ojox, ojoy, ojoz = 4, 10, 10

# Posición inicial de la fuente de luz
light_position = [10.0, 10.0, 15.0, 1.0]

# Ángulos de rotación para la luz y la estrella
light_rotation_x = 0.0
light_rotation_y = 0.0

def ejes(largo):
    glDisable(GL_LIGHTING)
    glBegin(GL_LINES)
    glColor3f(1, 0, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(largo, 0, 0)

    glColor3f(0, 1, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(0, largo, 0)

    glColor3f(0, 0, 1)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 0, largo)
    glEnd()
    glEnable(GL_LIGHTING)

def display():
    global ojox, ojoy, ojoz, light_position, light_rotation_x, light_rotation_y

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    gluLookAt(ojox, ojoy, ojoz, 0, 0, 0, 0.0, 1.0, 0.0)

    # Setear luz
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, [0.2, 0.2, 0.2, 1.0])

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

    glutSwapBuffers()

def keypress(key, x, y):
    global light_position, light_rotation_x, light_rotation_y

    if key == b'a':
        light_position[0] -= 0.1
    elif key == b'd':
        light_position[0] += 0.1
    elif key == b's':
        light_position[1] -= 0.1
    elif key == b'w':
        light_position[1] += 0.1
    elif key == b'u':
        light_rotation_x += 5.0
    elif key == b'j':
        light_rotation_x -= 5.0

    glutPostRedisplay()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(height, width)
    glutCreateWindow(b'Ejes')

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (width / height), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

    glLightfv(GL_LIGHT0, GL_POSITION, light_position)

    glutDisplayFunc(display)
    glutKeyboardFunc(keypress)
    glutMainLoop()

if __name__ == '__main__':
    main()
