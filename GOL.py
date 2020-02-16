import patterner as pt
from random import random
import time

pause = False
# create randomized 60*60 matrix
field = pt.rnd_matrix(60)

'''
# create planer for classic GOL rule
field = pt.filled_matrix(50, 0)
field[9][8] = 1
field[9][9] = 1
field[9][10] = 1
field[8][10] = 1
field[7][7] = 1
'''
p = pt.Patterner(field, 10)
l = len(field)

# 'maze' ruleset
# Format is "number of cells: probability".
# The "probability" thing adds some random
# Not really a finite-state machine now, just added this for fun.
# To make it behave as normal Game of Life, make all the "probabilities" equal to 1
alive_conditions = {'1': 0.95, '2': 0.95, '3': 0.95, '4': 0.95, '5': 0.95}
born_conditions = {'3': 0.3}

#'maze' ruleset
# alive = [1, 2, 3, 4, 5]
# born = [3]

print("%s x %s field generated" % (len(field), len(field[0])))


def tor(c):
    '''Toroidal closed surface'''
    return c + l if c < 0 else c % l


def gol_step(y, near):
    # cell birth condition
    if (y == 0 and str(near) in born_conditions):
        return 1 if born_conditions[str(near)] > random() else 0
    # cell survives condition
    if (y == 1 and str(near) in alive_conditions):
        return 1 if alive_conditions[str(near)] > random() else 0
    # else die
    return 0


def sum_near(m, i, j):
    '''Calculate the sum of all neighbour cells'''
    s = 0
    for ii in range(-1, 2):
        for jj in range(-1, 2):
            s += m[tor(i + ii)][tor(j + jj)]
    s -= m[i][j]
    return s


def iterate(m):
    # New state matrix
    f2 = [row[:] for row in m]
    for i in range(l):
        for j in range(l):
            near = sum_near(m, i, j)
            f2[tor(i)][tor(j)] = gol_step(m[tor(i)][tor(j)], near)
    return f2


def key1_callback(event):
    global pause
    pause = not pause
    print("pause: ", pause)


def key3_callback(event):
    print("Saved as ", p.save_image())


p.bind("<Button-1>", key1_callback)  # press LMB to pause/resume
p.bind("<Button-3>", key3_callback)  # press RMB to save current state as png image

iteration = 0
time_counter = time.time()

# basic main loop
while (True):
    p.tk_update()
    if pause:
        time.sleep(0.05)
        continue
    if time.time() - time_counter >= 0.1:
        time_counter = time.time()
        p.clean()
        p.set_matrix(field)
        p.draw()
        field = iterate(field)
        iteration += 1
        print('Iteration %d' % iteration)
        time.sleep(0.05)

input()
