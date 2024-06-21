# game_manager.py
import pygame
from .settings import *
from .chaos import ChaosMovement
from .percolation import PercolationMaze
from .character import Character
from .maze import Maze

class GameManager:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.init_game()

    def init_game(self):
        chaos_movement = ChaosMovement(0.5, 0.5)
        self.character = Character(0.5, 0.5, chaos_movement)
        percolation_maze = PercolationMaze(WINDOW_WIDTH // 10, WINDOW_HEIGHT // 10)
        grid = percolation_maze.generate_maze()
        self.maze = Maze(grid)

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.character.update()

    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)
        self.maze.draw(self.screen)
        self.character.draw(self.screen)
        pygame.display.flip()
