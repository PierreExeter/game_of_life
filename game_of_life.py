# This Python file uses the following encoding: utf-8
# """
# Game of life

import pygame
from pygame.locals import *
import numpy as np
import copy
from operator import add

size_cell = 5
cells_by_side = 70
nb_fps = 30
side_win = size_cell*cells_by_side

pygame.init()

# import image
brick = pygame.image.load("brick.png")
b_brick = pygame.image.load("black_brick.png")

# scale image
brick = pygame.transform.scale(brick, (size_cell, size_cell))
b_brick = pygame.transform.scale(b_brick, (size_cell, size_cell))

# open windows
window = pygame.display.set_mode((side_win, side_win))

# create initial map
grid = np.zeros((cells_by_side, cells_by_side))

def create_brick(x, y):
		""" place white brick at location (x, y) """
		window.blit(brick, (size_cell*x, size_cell*y))

def delete_brick(x, y):
		""" place black birck at location (x, y) """	
		window.blit(b_brick, (size_cell*x, size_cell*y))

def number_neighbours(x, y, grid):
		""" return number of neighbourghs for the cell (x, y) in grid """
		n = 0
		if grid[x+1, y] == 1:
			n = n+1
		if grid[x+1, y+1] == 1:
			n = n+1
		if grid[x, y+1] == 1:
			n = n+1
		if grid[x-1, y+1] == 1:
			n = n+1
		if grid[x-1, y] == 1:
			n = n+1
		if grid[x-1, y-1] == 1:
			n = n+1
		if grid[x, y-1] == 1:
			n = n+1
		if grid[x+1, y-1] == 1:
			n = n+1    
		return[n]

# initialise the game of life

def glider(x, y):
		""" place a glider at (x, y) """

		if x >= cells_by_side-2 or y >= cells_by_side-2 or x <= 2 or y <= 2:
			raise ValueError('The glider is outside the edge of the window!')

		glider_x = [0, 1, 1, 2, 2]
		glider_y = [0, 1, 2, 2, 1]

		a = [i+x for i in glider_x]
		b = [i+y for i in glider_y]

		for i in range(len(a)):
			grid[a[i], b[i]] = 1
			create_brick(a[i], b[i])

# glider(12,60)

# pulsar

def pulsar(x, y):
		""" place a pulsar at (x, y) """

		if x >= cells_by_side-12 or y >= cells_by_side-12 or x<= 12 or y<= 12:
			raise ValueError('The pulsar is outside the edge of the window!')

		pulsar_x = [2, 3, 4, 8, 9, 10, 0, 5, 7, 12, 0, 5, 7, 12, 0, 5, 7, 12, 2, 3, 4, 8, 9, 10, 2, 3, 4, 8, 9, 10, 0, 5, 7, 12, 0, 5, 7, 12, 0, 5, 7, 12, 2, 3, 4, 8, 9, 10]
		pulsar_y = [0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 12, 12, 12, 12, 12, 12]

		a = [i+x for i in pulsar_x]
		b = [i+y for i in pulsar_y]

		for i in range(len(a)):
			grid[a[i], b[i]] = 1
			create_brick(a[i], b[i])

# pulsar(20, 20)

# glider gun
def glider_gun(x, y):
		""" place a glider gun at (x, y) """
		
		gg_x = [24, 22, 24, 12, 13, 20, 21, 34, 35, 11, 15, 20, 21, 34, 35, 0, 1, 10, 16, 20, 21, 0, 1, 10, 14, 16, 17, 22, 24, 10, 16, 24, 11, 15, 12, 13]
		gg_y = [0, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 7, 7, 8, 8]

		for i in range(len(x)):
    	grid[x[i], y[i]] = 1
    	create_brick(x[i], y[i])

# refresh screen
pygame.display.flip()

# create old_grid
old_grid = copy.deepcopy(grid)

run_game = 1
while run_game:
		# pygame.time.Clock().tick(nb_fps)

		for event in pygame.event.get():
				if event.type == QUIT:
						run_game = 0
				if event.type == KEYDOWN and event.key == K_SPACE:
						run_game = 0

		# for x in range(0, len(grid)-1):
				# for y in range(0, len(grid)-1):

						# if number_neighbours(x, y, old_grid) < [2]:
								# grid[x, y] = 0
						# if number_neighbours(x, y, old_grid) == [3]:
								# grid[x, y] = 1
						# if number_neighbours(x, y, old_grid) > [3]:
								# grid[x, y] = 0

		# for x in range(0, len(grid)-1):
				# for y in range(0, len(grid)-1):
						# if grid[x, y] == [1]:
								# create_brick(x, y)
						# if grid[x, y] == [0]:
								# delete_brick(x, y)

		# old_grid = copy.deepcopy(grid)
		pygame.display.flip()




