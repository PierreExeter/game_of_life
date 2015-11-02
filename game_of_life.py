# This Python file uses the following encoding: utf-8
# """
# Game of life

import pygame
from pygame.locals import *
import numpy as np
import copy
from operator import add

pygame.init()

size_cell = 5
cells_by_side = 70
side_win = size_cell*cells_by_side

def create_brick(x, y):
    window.blit(brick, (size_cell*x, size_cell*y))

def delete_brick(x, y):
    window.blit(b_brick, (size_cell*x, size_cell*y))

def number_neighbours(x, y, grid):
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

# glider
x = [1, 2, 2, 3, 3]
y = [1, 2, 3, 1, 2]

for i in range(len(x)):
    grid[x[i], y[i]] = 1
    create_brick(x[i], y[i])

# pulsar
x = [12,13,14,18,19,20,10,15,17,22,10,15,17,22,10,15,17,22,12,13,14,18,19,20,12,13,14,18,19,20,10,15,17,22,10,15,17,22,10,15,17,22,12,13,14,18,19,20]
y = [10,10,10,10,10,10,12,12,12,12,13,13,13,13,14,14,14,14,15,15,15,15,15,15,17,17,17,17,17,17,18,18,18,18,19,19,19,19,20,20,20,20,22,22,22,22,22,22]

for i in range(len(x)):
    grid[x[i], y[i]] = 1
    create_brick(x[i], y[i])

# glider gun
x = [25,23,25,13,14,21,22,35,36,12,16,21,22,35,36,1,2,11,17,21,22,1,2,11,15,17,18,23,25,11,17,25,12,16,13,14]
old_y = [31,32,32,33,33,33,33,33,33,34,34,34,34,34,34,35,35,35,35,35,35,36,36,36,36,36,36,36,36,37,37,37,38,38,39,39]

translate = []
for i in range(len(old_y)):
    translate.append(10)

y = map(add, old_y, translate)

for i in range(len(x)):
    grid[x[i], y[i]] = 1
    create_brick(x[i], y[i])

# refresh screen
pygame.display.flip()

# create old_grid
old_grid = copy.deepcopy(grid)

run_game = 1
while run_game:
    # 30 frames per seconds
    pygame.time.Clock().tick(30)

    for event in pygame.event.get():
        if event.type == QUIT:
            run_game = 0

    for x in range(0, len(grid)-1):
        for y in range(0, len(grid)-1):

            if number_neighbours(x, y, old_grid) < [2]:
                grid[x, y] = 0
            if number_neighbours(x, y, old_grid) == [3]:
                grid[x, y] = 1
            if number_neighbours(x, y, old_grid) > [3]:
                grid[x, y] = 0

    for x in range(0, len(grid)-1):
        for y in range(0, len(grid)-1):
            if grid[x, y] == [1]:
                create_brick(x, y)
            if grid[x, y] == [0]:
                delete_brick(x, y)

    old_grid = copy.deepcopy(grid)
    pygame.display.flip()
