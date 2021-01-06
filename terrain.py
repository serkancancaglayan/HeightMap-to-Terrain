from PIL import Image
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from heightmap import HeightMap
from funcs import *

"""Bu class HeightMap classini kullanarak olusturulan yukseklik vertexlerinden,
 terrain olusturur ve terraini ekrana cizer"""
class Terrain:
    def __init__(self):
        self.heights = []
        self.h_map = None
    
    #Bu fonksiyon filepath, terrain buyuklugu ve max yukseklik parametreleri alir ve
    #cizilecek terraini init eder
    def initTerrain(self, filename, size, h,texture_filename):
        self.h_map = HeightMap()
        self.h_map.load_image(filename)
        self.heights = self.h_map.get_heights()
        self.size = size
        self.h = h
        self.texture_id = loadTexture(texture_filename)[0]
    
    #Bu fonksiyon initlenen terraini ekrana cizdirir
    def renderTerrain(self):
        glPushMatrix()
        glBindTexture(GL_TEXTURE_2D, self.texture_id)
        for i in range(len(self.h_map.heights) - 1):
            for j in range(len(self.h_map.heights[0]) - 1):
                range_ = self.h_map.width
                """ i ve j [0,resim boyutu] araliginda oldugu icin terraini ekranin sag 
                ust tarafina dayali ciziyordu, bu yuzden i ve j'yi [-resim boyutu, resim boyutu] araligina
                map ettik"""
                x = map(i, 0, range_, -range_, range_)
                y = map(j, 0, range_, -range_, range_)
                x_ = map(i + 1, 0, range_, -range_, range_)
                y_ = map(j + 1, 0, range_, -range_ , range_ )
                glBegin(GL_TRIANGLE_STRIP)
                if(self.heights[i][j] < 64):
                    r = 126 / 256
                    g = 200 / 256
                    b = 80 / 256
                    glColor3f(r * self.heights[i][j] / 256, g * self.heights[i][j] / 256, b * self.heights[i][j] / 256)
                elif(self.heights[i][j] > 64 and self.heights[i][j] < 192):
                    r = 128 / 256
                    g = 132 / 256
                    b = 135 / 256
                    glColor3f(r * self.heights[i][j] / 256, g * self.heights[i][j] / 256, b * self.heights[i][j] / 256)
                elif(self.heights[i][j] > 192 and self.heights[i][j] < 255):
                    r = 1
                    g = 1
                    b = 1
                    glColor3f(r * self.heights[i][j] / 256, g * self.heights[i][j] / 256, b * self.heights[i][j] / 256)
                glTexCoord2f(1, 0)
                glVertex3f(x*self.size, self.heights[i][j]*self.h, y*self.size)
                glTexCoord2f(1, 1)
                glVertex3f(x_*self.size, self.heights[i+1][j]*self.h, y*self.size)
                glTexCoord2f(0, 1)
                glVertex3f(x*self.size, self.heights[i][j+1]*self.h, y_*self.size)
                glTexCoord2f(0, 0)
                glVertex3f(x_*self.size, self.heights[i+1][j+1]*self.h, y_*self.size)
                glEnd()
        glPopMatrix()