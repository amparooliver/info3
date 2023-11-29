from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Tamaño de la ventana
width, height = 800, 800

# Posición inicial de la cámara
ojox, ojoy, ojoz = 1, 1, 5

# Posición inicial de la fuente de luz
light_position = [1.0, 1.0, 2.0, 0.0]

# Ángulos de rotación para la luz y la estrella
light_rotation_x = 0.0
light_rotation_y = 0.0
star_rotation_angle = 0.0

class Mesh:
    def __init__(self, objPath=None, vertices=[], triangles=[], drawtype=GL_POLYGON): #GL_LINE_LOOP #GL_POLYGON
        self.vertices = vertices
        self.triangles = triangles
        self.drawtype = drawtype

        if objPath is not None:
            self.LoadMesh(objPath)

    def LoadMesh(self, objPath):
        with open(objPath) as objFile:
            lines = objFile.readlines()
            for line in lines:
                if line.startswith("v "):
                    vx, vy, vz = [float(value) for value in line.split()[1:]]
                    self.vertices.append((vx, vy, vz))
                elif line.startswith("f "):
                    face = [int(face.split('/')[0]) - 1 for face in line.split()[1:]]
                    self.triangles.extend(face)

    def Draw(self):
        glBegin(self.drawtype)
        for i in range(0, len(self.triangles), 3):
            for j in range(3):
                glVertex3fv(self.vertices[self.triangles[i + j]])
        glEnd()

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


def draw_star():
    global star_mesh, star_rotation_angle

    # Encuentra la punta de la estrella (por ejemplo, el primer vértice)
    pivot_point = star_mesh.vertices[1]

    # Aplica la rotación alrededor de la punta
    glPushMatrix()
    glTranslatef(pivot_point[0], pivot_point[1], pivot_point[2])
    glRotatef(star_rotation_angle, 0.0, 1.0, 0.0)
    glTranslatef(-pivot_point[0], -pivot_point[1], -pivot_point[2])
    # Configura el color de la estrella (amarillo)
    glColor3f(1.0, 1.0, 0.0)
    star_mesh.Draw()
    glPopMatrix()

def display():
    global ojox, ojoy, ojoz, light_position, light_rotation_x, light_rotation_y

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    gluLookAt(ojox, ojoy, ojoz, 0, 0, 0, 0.0, 1.0, 0.0)

    # Setear luz
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, [0.2, 0.2, 0.2, 1.0])

    # Material
    glEnable(GL_COLOR_MATERIAL)
    glMaterialfv(GL_FRONT, GL_AMBIENT, [0.4, 0.4, 0.4, 1.0])
    glMaterialfv(GL_FRONT, GL_DIFFUSE, [0.8, 0.8, 0.8, 1.0])
    glMaterialfv(GL_FRONT, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])
    glMaterialfv(GL_FRONT, GL_SHININESS, 100.0)
    
    # Dibujar ejes 
    ejes(2)

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

    draw_star()

    glutSwapBuffers()

def keypress(key, x, y):
    global light_position, light_rotation_x, light_rotation_y, star_rotation_angle

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

    # Control de la rotación de la estrella
    elif key == b'u':
        star_rotation_angle += 5.0  # Rota la estrella en sentido antihorario
    elif key == b'j':
        star_rotation_angle -= 5.0  # Rota la estrella en sentido horario

    # Actualiza la escena después de los cambios
    glutPostRedisplay()

def main():
    global star_mesh

    # Inicializar la aplicación GLUT
    glutInit(sys.argv)

    # Configurar el modo de visualización con doble búfer, RGB y profundidad
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)

    # Configurar el tamaño de la ventana
    glutInitWindowSize(height, width)

    # Crear la ventana con el título "Estrella 3D"
    glutCreateWindow(b'Estrella 3D - Amparo')

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

    # Cargar el modelo de estrella desde el archivo "estrellaMODELO.obj"
    star_mesh = Mesh(objPath="estrellaMODELO.obj")

    # Establecer las funciones de visualización y manejo de teclado
    glutDisplayFunc(display)
    glutKeyboardFunc(keypress)

    # Iniciar el bucle principal de GLUT
    glutMainLoop()

if __name__ == '__main__':
    main()

