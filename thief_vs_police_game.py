import numpy as np
import pygame
import pygame.locals
import random


def generate_percolation_field(size, p):
    return np.random.rand(size, size) < p

size = 50  # フィールドのサイズ
p = 0.65  # パーコレーションの確率
field = generate_percolation_field(size, p)


pygame.init()

# 画面の設定
screen_size = 800
screen = pygame.display.set_mode((screen_size, screen_size))
pygame.display.set_caption("Thief vs Police")
clock = pygame.time.Clock()

# 色の設定
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# セルのサイズ
cell_size = screen_size // size


class Agent:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def move(self, dx, dy):
        self.x = max(0, min(size - 1, self.x + dx))
        self.y = max(0, min(size - 1, self.y + dy))

thief = Agent(size // 2, size // 2, BLUE)
cops = [Agent(random.randint(0, size - 1), random.randint(0, size - 1), RED) for _ in range(3)]


def draw_field(screen, field):
    for x in range(size):
        for y in range(size):
            color = WHITE if field[x, y] else BLACK
            pygame.draw.rect(screen, color, (x * cell_size, y * cell_size, cell_size, cell_size))

def draw_agent(screen, agent):
    pygame.draw.rect(screen, agent.color, (agent.x * cell_size, agent.y * cell_size, cell_size, cell_size))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.locals.KEYDOWN:
            # keys = pygame.key.get_pressed()
            if event.key == pygame.K_LEFT:
                thief.move(-1, 0)
            if event.key == pygame.K_RIGHT:
                thief.move(1, 0)
            if event.key == pygame.K_UP:
                thief.move(0, -1)
            if event.key == pygame.K_DOWN:
                thief.move(0, 1)

    for cop in cops:
        if cop.x < thief.x:
            cop.move(1, 0)
        elif cop.x > thief.x:
            cop.move(-1, 0)
        if cop.y < thief.y:
            cop.move(0, 1)
        elif cop.y > thief.y:
            cop.move(0, -1)

    screen.fill(BLACK)
    draw_field(screen, field)
    draw_agent(screen, thief)
    for cop in cops:
        draw_agent(screen, cop)
    
    pygame.display.flip()
    clock.tick(1)

pygame.quit()
