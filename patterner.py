#!/usr/bin/python3

from tkinter import *
from random import randint, choice

class Patterner:
	def __init__(self, matrix, pixel_size = 1, mode = 'wb'):
		'''matrix - an array or tuple of rows of elements
		mode - "wb" for white/black, "color" for color
		pixel_size - size of pseudopixel 
        In color mode uses cell values from matrix as colors; 
        color could be in any tk-acceptable format
        !!!currently works only with square matrixes'''
		self.p_size = pixel_size
		self.mode = mode
		self.tk = Tk()
		self.set_matrix(matrix)
		self.create_canvas(self.c_size)

	def set_matrix(self, m):
		'''A method to change matrix'''
		self.matrix = m
		self.c_size = len(self.matrix) * self.p_size + 1
		self.rng = range(0, len(self.matrix))

	def set_mode(self, mode):
		'''changes mode'''
		self.mode = mode

	def clean(self):
		'''cleans canvas'''
		self.c.delete('all')
		
	def create_canvas(self, size):
		self.c = Canvas(self.tk, width=size, height=size)
		self.c.pack()

	def draw(self):
		'''draw method'''
		x0, y0, x1, y1 = 0, 0, self.p_size, self.p_size

		for i in self.rng:
			for ii in self.rng:
				if (self.mode == 'color'):
					self.c.create_rectangle(x0, y0, x1, y1, fill = self.matrix[i][ii], width = 0)
				else:
					if (self.matrix[i][ii] >= 1):
						self.c.create_rectangle(x0, y0, x1, y1, fill = 'black', width = 0)

				x0 += self.p_size
				x1 += self.p_size
			x0 = 0
			y0 += self.p_size
			x1 = self.p_size
			y1 += self.p_size
		self.tk.update_idletasks()
		self.tk.update()
		

	def bind(self, key, event):
		self.tk.bind(key, event)

def rnd_matrix(n):
	'''Returns matrix with size n*n filled with 1s or 0s'''
	return [[randint(0,1) for x in range(n)] for xx in range(n)]

def rnd_color():
	'''Pretty original way to create random color in hex.
    Returns color string'''
	ch = ['a','b','c','d','e','f']
	clr = '#'
	for i in range(6):
		x = randint(0,100)
		if(x < 50):
			clr += choice(ch)
		else:
			clr += str(randint(0,9))
	return clr

def rnd_matrix_c(n):
	'''returns matrix with size n*n and filled with random colors'''
	return [[rnd_color() for x in range(n)] for xx in range(n)]

def filled_matrix(n, fill):
	'''returns matrix with size n*n and filled with "fill"'''
	return [[fill for i in range(n)] for j in range(n)] 

def text_draw(m):
	'''An alternate simple way to draw matrix filled with same length elements - just prints it out!'''
	l = len(m)
	s = ''
	for i in range(l):
		for j in range(l):
			s += str(m[i][j]) + ' '
		s += '\n'
	return s

if __name__ == '__main__':
	# Example of usage
	import time
	m = rnd_matrix_c(20)
	p = Patterner(m, 20, 'color')
	print(p)
	p.draw()
	time.sleep(2)
	p.clean()
	p.set_mode('wb')
	p.set_matrix(rnd_matrix(20))
	p.draw()
	
	input()