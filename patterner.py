#!/usr/bin/python3

from tkinter import *
from random import randint, choice
from datetime import datetime
from PIL import Image
import io


class Patterner:
    def __init__(self, matrix, pixel_size=1, mode="wb"):
        '''matrix - an array or tuple of rows of elements
        mode - "wb" for white/black, "color" for color, default - "wb"
        pixel_size - size of pseudopixel
        In color mode it uses cell values from matrix as colors;
        Color could be in any tk-acceptable format'''
        self.pixel_size = pixel_size
        self.mode = mode
        self.tk = Tk()
        self.set_matrix(matrix)
        self.canvas = Canvas(self.tk, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()

    def set_matrix(self, matrix):
        self.matrix = matrix
        self.matrix_width = len(self.matrix[0])
        self.matrix_height = len(self.matrix)

        self.canvas_width = self.matrix_width * self.pixel_size + 1
        self.canvas_height = self.matrix_height * self.pixel_size + 1

    def set_mode(self, mode):
        '''mode - "wb" for white/black, "color" for color'''
        self.mode = mode

    def clean(self):
        self.canvas.delete("all")

    def draw(self):
        x0, y0, x1, y1 = 0, 0, self.pixel_size, self.pixel_size

        for i in range(0, self.matrix_height):
            for ii in range(0, self.matrix_width):
                if (self.mode == 'color'):
                    self.canvas.create_rectangle(
                        x0, y0, x1, y1, fill=self.matrix[i][ii], width=0)
                else:
                    if (self.matrix[i][ii] >= 1):
                        self.canvas.create_rectangle(
                            x0, y0, x1, y1, fill="black", width=0)

                x0 += self.pixel_size
                x1 += self.pixel_size
            x0 = 0
            y0 += self.pixel_size
            x1 = self.pixel_size
            y1 += self.pixel_size
        self.tk_update()

    def bind(self, key, event):
        self.tk.bind(key, event)

    def tk_update(self):
        self.tk.update_idletasks()
        self.tk.update()

    def _generate_filename(self):
        return datetime.strftime(datetime.today(), "%d%m%y_%H%M%S")

    def save_image(self, filename=None):
        fn = filename if filename else self._generate_filename()
        ps = self.canvas.postscript(colormode="color")
        img = Image.open(io.BytesIO(ps.encode("utf-8")))
        img.save(fn + ".png", "png")
        return fn + ".png"


def rnd_matrix(n):
    '''Returns n*n matrix filled with 1s or 0s'''
    return [[randint(0, 1) for x in range(n)] for xx in range(n)]


def rnd_color():
    '''Pretty original way to create random color in hex.
    Returns color string'''
    ch = ['a', 'b', 'c', 'd', 'e', 'f']
    clr = '#'
    for i in range(6):
        x = randint(0, 100)
        if(x < 50):
            clr += choice(ch)
        else:
            clr += str(randint(0, 9))
    return clr


def rnd_matrix_c(n):
    '''returns n*n-sized matrix filled with random colors'''
    return [[rnd_color() for x in range(n)] for xx in range(n)]


def filled_matrix(n, fill):
    '''returns n*n-sized matrix filled with "fill"'''
    return [[fill for i in range(n)] for j in range(n)]


if __name__ == "__main__":
    # Example of usage
    import time
    m = rnd_matrix_c(20)
    p = Patterner(m, 30, "color")
    p.draw()
    time.sleep(2)
    p.clean()
    p.set_mode("wb")
    p.set_matrix(rnd_matrix(20))
    p.draw()

    input()
