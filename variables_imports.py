from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *
from heightmap import HeightMap
from terrain import Terrain
from PIL import Image
import sys
from funcs import *

size = 0.01
h = 0.005
zoom = 1
filename = "C:/Users/serka/Desktop/Bilgisayar Grafikleri/final/ornek_harita2.jpg"
terrain_texture_filename =  "C:/Users/serka/Desktop/Bilgisayar Grafikleri/final/texture.png"
WindowHeight = 1200
WindowWidth = 800
terrain_texture_id = 0

