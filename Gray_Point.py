from PIL import Image
from tkinter.filedialog import askopenfilenames
from tkinter import Tk
import time
import os
import numpy


class normal:
    def __init__(self, path) -> None:
        print('this is a normal image')
        self.__path = path
        self.__name = os.path.basename(self.__path).split('.')[0]
        self.__ext = os.path.splitext(self.__path)[1]
        self.__img = Image.open(self.__path)
        if self.__ext == '.png':
            self.__img = self.__img.convert('RGB')
        self.__pixels = numpy.array(self.__img)
        self.gray()

    def gray(self):
        blank = Image.new(
            'L', (self.__img.size[0], self.__img.size[1]*3), (0))
        temp = []
        for x in range(len(self.__pixels)):
            for y in range(len(self.__pixels[x])):
                for z in range(0, 3):
                    temp.append(int(self.__pixels[x][y][z]))
        pix_map = blank.load()
        temp = iter(temp)
        for i in range(blank.size[0]):
            for j in range(blank.size[1]):
                pix_map[j, i] = next(temp)
        blank.save('source/%s.jpg' % self.__name)


class gray:
    def __init__(self, path) -> None:
        print('this is a gray image')
        self.__path = path
        self.__name = os.path.basename(self.__path).split('.')[0]
        self.__img = Image.open(self.__path)
        self.__pixels_map = self.__img.load()
        self.__width = self.__img.size[0]
        self.__height = int(self.__img.size[1] / 3)
        self.__data = self.read_data()
        self.create_img()

    def read_data(self):
        fin = []
        temp = []
        for x in range(self.__img.size[0]):
            for y in range(self.__img.size[1]):
                temp.append(self.__pixels_map[x, y])
                if len(temp) == 3:
                    fin.append(tuple(temp))
                    temp = []
        return iter(fin)

    def create_img(self):
        img = Image.new('RGB', (self.__width, self.__height), (0, 0, 0))
        array = numpy.array(img)

        for x in range(self.__width):
            for y in range(self.__height):
                array[y][x] = next(self.__data)
        img = Image.fromarray(array)
        img.save('%s.jpg' % self.__name)


def main():
    Tk().withdraw()
    files = askopenfilenames()
    for x in files:
        Img = Image.open(x)
        if type((Img.load()[0, 0])) == int:
            gray(x)
        else:
            normal(x)


main()
# pyinstaller --onefile --hidden-import='pillow'--collect-all='pillow' Gray_Point.py
