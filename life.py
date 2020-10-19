# life.py

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anm

def create(shape):
	'''
	Creates matrix
	'''
	return np.random.choice([1,0], shape, p=[0.5,0.5])

def iterate(matrix):
	'''
	Changes the matrix according to the game rules
	'''
	shifts = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]
	shifted_matrices = [ np.roll(matrix, shift, axis=(0,1)) for shift in shifts ]

	neighbours = sum(shifted_matrices)

	survivors = np.logical_and((matrix==1), np.logical_or(neighbours==2, neighbours==3)) 
	born = np.logical_and(matrix==0, neighbours==3)

	matrix[:] = 0
	matrix += np.where(born == True, 1, 0)
	matrix += np.where(survivors == True, 1, 0)

	return matrix

matrix = create((10,10))

def update(t):
	mat.set_array(iterate(matrix))

fig, ax = plt.subplots()
mat = ax.matshow(matrix)
plt.colorbar(mat)

ani = anm.FuncAnimation(fig, update, frames=100, interval=500)
plt.show()