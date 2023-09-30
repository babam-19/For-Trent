# adapted from https://thepythoncode.com/article/build-a-maze-game-in-python

import pygame
from cell import Cell

class Maze:
    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        self.thickness = 4
        self.grid_cells = [Cell(col, row, self.thickness) for row in range(self.rows) for col in range(self.cols)]

    # carve grid cell walls
    def remove_walls(self, current, next):
        dx = current.x - next.x
        if dx == 1: # means next cell is to the left of the current cell
            current.walls['left'] = False
            next.walls['right'] = False
        elif dx == -1: # means next cell is to the right of the current cell
            current.walls['right'] = False
            next.walls['left'] = False
        dy = current.y - next.y
        if dy == 1: # means next cell is below current cell
            current.walls['top'] = False
            next.walls['bottom'] = False
        elif dy == -1: # means next cell is above the current cell
            current.walls['bottom'] = False
            next.walls['top'] = False

    # generates maze 
    def generate_maze(self):
        '''
        Generates maze through recursive back tracking algorithm        
        '''
        current_cell = self.grid_cells[0]
        array = []
        break_count = 1
        while break_count != len(self.grid_cells):
            current_cell.visited = True
            next_cell = current_cell.check_neighbors(self.cols, self.rows, self.grid_cells)
            if next_cell:
                next_cell.visited = True
                break_count += 1
                array.append(current_cell)
                self.remove_walls(current_cell, next_cell)
                current_cell = next_cell
            elif array:
                current_cell = array.pop()
        return self.grid_cells
    
