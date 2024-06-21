# character.py
import pygame

class Character:
    def __init__(self, x, y, chaos_movement):
        self.x = x
        self.y = y
        self.chaos_movement = chaos_movement

    def update(self):
        self.x, self.y = self.chaos_movement.update_position()

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (int(self.x * 800), int(self.y * 600)), 5)
