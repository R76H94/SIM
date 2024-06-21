# percolation.py
import numpy as np

class PercolationMaze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = np.zeros((height, width))

    def generate_maze(self):
        # 簡単なパーコレーションモデルの実装
        for y in range(self.height):
            for x in range(self.width):
                self.grid[y, x] = np.random.choice([0, 1], p=[0.7, 0.3])
        return self.grid
