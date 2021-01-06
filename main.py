
from variables_imports import *
t = Terrain()

def init():
    t.initTerrain(filename, size, h, terrain_texture_filename)
    glClearColor(0,0,0,1)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    gluOrtho2D(0, WindowHeight, 0, WindowWidth)


def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glScale(zoom, zoom, zoom)
    glOrtho(-3.0, 3.0, -3.0, 3.0, 1.0, 50.0)
    gluLookAt(12.3, 12.6, 12.3, 0, 0, 0, -12.5, 0, -12.5)
    t.renderTerrain()
    glutSwapBuffers()

def MouseWheel(*args):
    global zoom
    if args[1]==-1:
        zoom-=0.05
    elif args[1]==1:
        zoom +=0.05
    else:
        pass
    glutPostRedisplay()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
    glutInitWindowSize(WindowHeight, WindowWidth)
    glutInitWindowPosition(0, 0)    
    glutCreateWindow(b"Terrain")
    glutMouseWheelFunc(MouseWheel)
    init()
    glutDisplayFunc(draw)
    glutMainLoop()

main()
