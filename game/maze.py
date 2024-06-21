# maze.py
import pygame

class Maze:
    def __init__(self, grid):
        self.grid = grid

    def draw(self, screen):
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                color = (255, 255, 255) if cell == 1 else (0, 0, 0)
                pygame.draw.rect(screen, color, (x * 10, y * 10, 10, 10))
