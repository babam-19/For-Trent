# adapted from https://thepythoncode.com/article/build-a-maze-game-in-python

import pygame
from random import choice

class Cell:
    def __init__(self, x, y, thickness):
        # parameters x,y, and thickness define the position and thickness of the wall per cell in the maze
        self.x, self.y = x, y
        self.thickness = thickness
        self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}
        self.visited = False

    
    # draw grid cell walls
    def draw(self, sc, tile):
        '''
        Calculates the screen coordinates based on x, y, and tile size and makes walls for 
        each cell in the maze      
        '''
        x, y = self.x * tile, self.y * tile
        if self.walls['top']:
            pygame.draw.line(sc, pygame.Color('#934AB3'), (x, y), (x + tile, y), self.thickness)
        if self.walls['right']:
            pygame.draw.line(sc, pygame.Color('#934AB3'), (x + tile, y), (x + tile, y + tile), self.thickness)
        if self.walls['bottom']:
            pygame.draw.line(sc, pygame.Color('#934AB3'), (x + tile, y + tile), (x , y + tile), self.thickness)
        if self.walls['left']:
            pygame.draw.line(sc, pygame.Color('#934AB3'), (x, y + tile), (x, y), self.thickness)


    # checks if cell does exist and returns it if it does
    def check_cell(self, x, y, cols, rows, grid_cells):
        '''
        Check if a cell at a given x, y coordinate exists. If the cell does not exists, the
        function returns false. If the cel does exist, the function returns the cell itself (at the coordinates)
        '''
        find_index = lambda x, y: x + y * cols
        if x < 0 or x > cols - 1 or y < 0 or y > rows - 1:
            return False
        return grid_cells[find_index(x, y)]

    # checking cell neighbors of current cell if visited (carved) or not
    def check_neighbors(self, cols, rows, grid_cells):
        '''
        Looks for neighboring cells that have not been visited. If the neighbor exists and has not
        been visited, the function adds the cell to the neighbors list. The function returns a random
        cell from neighbors if it exists (otherwise it returns false)
        '''
        neighbors = []
        top = self.check_cell(self.x, self.y - 1, cols, rows, grid_cells)
        right = self.check_cell(self.x + 1, self.y, cols, rows, grid_cells)
        bottom = self.check_cell(self.x, self.y + 1, cols, rows, grid_cells)
        left = self.check_cell(self.x - 1, self.y, cols, rows, grid_cells)
        if top and not top.visited:
            neighbors.append(top)
        if right and not right.visited:
            neighbors.append(right)
        if bottom and not bottom.visited:
            neighbors.append(bottom)
        if left and not left.visited:
            neighbors.append(left)
        return choice(neighbors) if neighbors else False