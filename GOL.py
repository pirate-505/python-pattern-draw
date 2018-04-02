import patterner as pt
from random import randint
import time

#create randomized 50*50 matrix
field = pt.rnd_matrix(50)

'''
#create planer for classic GOL rule
field = pt.filled_matrix(50, 0)
field[9][8] = 1
field[9][9] = 1
field[9][10] = 1
field[8][10] = 1
field[7][7] = 1
'''
p = pt.Patterner(field, 10)
l = len(field)

#'pseudolife' ruleset
ALIVE = [2, 3, 8]
BORN = [3, 5, 7]

#'maze' ruleset
#alive = [1, 2, 3, 4, 5]
#born = [3]

print("%s x %s field generated" % (len(field), len(field[0])))

def tor(c):
	#toroidal closed surface
	if (c < 0):
		return c+l
	else:
		return c%l

def gol(y, near):
	#cell birth condition
	if (y == 0 and near in BORN):
		return 1
	#cell survives condition
	if (y == 1 and near in ALIVE):
		return 1
	#else die
	return 0

def sum_near(m, i, j):
	#calculate the sum of all neighbour cells
	s = 0
	for ii in range(-1,2):
		for jj in range(-1,2):
			s += m[tor(i+ii)][tor(j+jj)]
	s -= m[i][j]
	return s

def iterate(m):
	#new state matrix
	f2 = [row[:] for row in m]
	for i in range(l):
		for j in range(l):
			near = sum_near(m, i, j)
			#some debug stuff
			#if(m[i][j] != 0):
			#	print('i = %d, j = %d; cell = %d, nearsum = %d' % (i,j, m[tor(i)][tor(j)], near))
			f2[tor(i)][tor(j)] = gol(m[tor(i)][tor(j)], near)
	return f2

iteration = 0

while (True):
	p.clean()
	p.set_matrix(field)
	p.draw()
	#print(pt.text_draw(field))
	time.sleep(0.1)
	field = iterate(field)
	iteration += 1
	print('Iteration %d' % iteration)
	#if(field == iterate(field)):
	#	print('*** Stable state! ***')

input()