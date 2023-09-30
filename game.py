# adapted from https://thepythoncode.com/article/build-a-maze-game-in-python

import pygame

pygame.font.init()

class Game:
    def __init__(self, goal_cell, tile):
        self.font = pygame.font.SysFont("impact", 9)
        self.message_color = pygame.Color("purple")
        self.goal_cell = goal_cell
        self.tile = tile

    # add goal point for player to reach
    def add_goal_point(self, screen):
        # adding gate for the goal point
        img_path = 'Photos/briannaDrawing.png'
        img = pygame.image.load(img_path)
        img = pygame.transform.scale(img, (self.tile, self.tile))
        screen.blit(img, (self.goal_cell.x * self.tile, self.goal_cell.y * self.tile))

    # winning message
    def message(self):
        msg = self.font.render('Trent, Happy 6 months.\nYou Won!', True, self.message_color)
        return msg

    # checks if player reached the goal point
    def is_game_over(self, player):
        goal_cell_abs_x, goal_cell_abs_y = self.goal_cell.x * self.tile, self.goal_cell.y * self.tile
        if player.x >= goal_cell_abs_x and player.y >= goal_cell_abs_y:
            return True
        else:
            return False