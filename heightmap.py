""" Bu class filepathi verilen png, jpg uzantili dosyanin pixellerini
PIL kutuphanesi kullanarak yukler, pixellerin
gri tonlarinin koyuluguna gore
yukseklik vertexlerini tutan arrayi olusturur """
from PIL import Image
import sys
class HeightMap:
    def __init__(self):
        self.heights = []
        self.image = None
        self.height = 0
        self.width = 0
        self.pixels = []    
    
    #Bu fonksiyon resmin pixellerini ve resmin ozelliklerini okur
    def load_image(self, filename):
        self.image = Image.open(filename)
        self.height = self.image.height
        self.width = self.image.width
        self.pixels = self.image.load()

    #Bu fonksiyon yukseklik vertexlerini tutan arrayi olusturur 
    def get_heights(self):
        if(self.image == None):
            print("Could not load the image")
            sys.exit(-1)
        rgb_image = self.image.convert('RGB')
        for i in range(self.width):
            temp = []
            for j in range(self.height):
                r, _, _ = rgb_image.getpixel((i, j))
                temp.append(r)
            self.heights.append(temp)
        return self.heights
