import sys  # helps to hand the app's termination and exit status
import os
import time
import typing
import pygame, sys
from Maze import Maze
from player import Player
from game import Game
from clock import Clock
from PyQt6 import QtCore
from PyQt6.QtWidgets import (
    QApplication, 
    QFormLayout, 
    QLineEdit, 
    QWidget,
    QPushButton,
    QLabel,
    QGridLayout)

class MainAppPage(QWidget):
    def __init__(self, screen):
        super().__init__(parent=None)

        # Initialize Pygame
        pygame.init()
        pygame.font.init()

        # Set up Pygame surface
        self.pygame_surface = pygame.display.set_mode((800, 600))

        
        self.screen = screen
        self.font = pygame.font.SysFont("impact", 30)
        self.message_color = pygame.Color("cyan")
        self.running = True
        self.game_over = False
        self.FPS = pygame.time.Clock()


    def instructions(self):
        instructions1 = self.font.render('Use', True, self.message_color)
        instructions2 = self.font.render('Arrow Keys', True, self.message_color)
        instructions3 = self.font.render('to Move', True, self.message_color)
        self.screen.blit(instructions1,(655,300))
        self.screen.blit(instructions2,(610,331))
        self.screen.blit(instructions3,(630,362))

    # draws all configs; maze, player, instructions, and time
    def _draw(self, maze, tile, player, game, clock):
        # draw maze
        [cell.draw(self.screen, tile) for cell in maze.grid_cells]
        # add a goal point to reach
        game.add_goal_point(self.screen)
        # draw every player movement
        player.draw(self.screen)
        player.update()
        # instructions, clock, winning message
        self.instructions()
        if self.game_over:
            clock.stop_timer()
            self.screen.blit(game.message(),(610,120))
        else:
            clock.update_timer()
        self.screen.blit(clock.display_timer(), (625,200))
        pygame.display.flip()

    # main game loop
    def main(self, frame_size, tile):
        cols, rows = frame_size[0] // tile, frame_size[-1] // tile
        maze = Maze(cols, rows)
        game = Game(maze.grid_cells[-1], tile)
        player = Player(tile // 3, tile // 3)
        clock = Clock()
        maze.generate_maze()
        clock.start_timer()
        while self.running:
            self.screen.fill("gray")
            self.screen.fill( pygame.Color("darkslategray"), (603, 0, 752, 752))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            # if keys were pressed still
            if event.type == pygame.KEYDOWN:
                if not self.game_over:
                    if event.key == pygame.K_LEFT:
                        player.left_pressed = True
                    if event.key == pygame.K_RIGHT:
                        player.right_pressed = True
                    if event.key == pygame.K_UP:
                        player.up_pressed = True
                    if event.key == pygame.K_DOWN:
                        player.down_pressed = True
                    player.check_move(tile, maze.grid_cells, maze.thickness)
            # if pressed key released
            if event.type == pygame.KEYUP:
                if not self.game_over:
                    if event.key == pygame.K_LEFT:
                        player.left_pressed = False
                    if event.key == pygame.K_RIGHT:
                        player.right_pressed = False
                    if event.key == pygame.K_UP:
                        player.up_pressed = False
                    if event.key == pygame.K_DOWN:
                        player.down_pressed = False
                    player.check_move(tile, maze.grid_cells, maze.thickness)
            if game.is_game_over(player):
                self.game_over = True
                player.left_pressed = False
                player.right_pressed = False
                player.up_pressed = False
                player.down_pressed = False
            self._draw(maze, tile, player, game, clock)
            self.FPS.tick(60)