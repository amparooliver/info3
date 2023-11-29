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
    def __init__(self, objPath=None, vertices=[], triangles=[], drawtype=GL_POLYGON): #GL_LINE_LOOP
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

    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, [0.2, 0.2, 0.2, 1.0])

    ejes(2)

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)

    glPushMatrix()
    glRotatef(light_rotation_x, 1.0, 0.0, 0.0)
    glRotatef(light_rotation_y, 0.0, 1.0, 0.0)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glPopMatrix()

    draw_star()

    glutSwapBuffers()

def keypress(key, x, y):
    global light_position, light_rotation_x, light_rotation_y, star_rotation_angle

    if key == b'a':
        light_position[0] -= 0.1
    elif key == b'd':
        light_position[0] += 0.1
    elif key == b's':
        light_position[1] -= 0.1
    elif key == b'w':
        light_position[1] += 0.1
    elif key == b'u':
        star_rotation_angle += 5.0
    elif key == b'j':
        star_rotation_angle -= 5.0

    glutPostRedisplay()

def main():
    global star_mesh
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(height, width)
    glutCreateWindow(b'Estrella 3D')

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (width / height), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

    glLightfv(GL_LIGHT0, GL_POSITION, light_position)

    # Load the star mesh
    star_mesh = Mesh(objPath="estrellaMODELO.obj")

    glutDisplayFunc(display)
    glutKeyboardFunc(keypress)
    glutMainLoop()

if __name__ == '__main__':
    main()
