from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image
"""Bu fonksiyon [oldmin, oldmax] rangeindeki bir degeri [newmin, newmax] araligina
tasir, ornegin [0, 100] araliginda 50 degerini, [0, 200] araliginda 100 degeri yapar
"""
def map(OldValue, OldMin, OldMax, NewMin, NewMax):
    OldRange = (OldMax - OldMin)  
    NewRange = (NewMax - NewMin)  
    NewValue = (((OldValue - OldMin) * NewRange) / OldRange) + NewMin
    return NewValue

"""Bu fonksiyon filepathi verilen resmi texture olarak yukler, resmin buyuklugunu ve texture
id'sini dondurur"""
def loadTexture(filename):
        im = Image.open(filename)
        xSize = im.size[0]
        ySize = im.size[1]
        rawReference = im.tobytes("raw", "RGB")
        id = glGenTextures(1)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_MIRRORED_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, 3, xSize, ySize, 0, GL_RGB, GL_UNSIGNED_BYTE, rawReference)
        glEnable(GL_TEXTURE_2D)
        info = [id, xSize, ySize]
        return info