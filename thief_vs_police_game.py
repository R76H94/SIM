import numpy as np
import pygame
import random


def generate_percolation_field(size, p):
    return np.random.rand(size, size) < p

size = 50  # フィールドのサイズ
p = 0.65  # パーコレーションの確率
field = generate_percolation_field(size, p)

# Pygameの初期化
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

# エージェントクラスの定義
class Agent:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def move(self, dx, dy):
        self.x = max(0, min(size - 1, self.x + dx))
        self.y = max(0, min(size - 1, self.y + dy))

# 泥棒エージェントと警察エージェントの初期設定
thief = Agent(size // 2, size // 2, BLUE)
cops = [Agent(random.randint(0, size - 1), random.randint(0, size - 1), RED) for _ in range(3)]

# フィールドを描画する関数
def draw_field(screen, field):
    for x in range(size):
        for y in range(size):
            color = WHITE if field[x, y] else BLACK
            pygame.draw.rect(screen, color, (x * cell_size, y * cell_size, cell_size, cell_size))

# エージェントを描画する関数
def draw_agent(screen, agent):
    pygame.draw.rect(screen, agent.color, (agent.x * cell_size, agent.y * cell_size, cell_size, cell_size))

# ゲームのメインループ
running = True
while running:
    # イベント処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # キー入力の処理
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        thief.move(-1, 0)
    if keys[pygame.K_RIGHT]:
        thief.move(1, 0)
    if keys[pygame.K_UP]:
        thief.move(0, -1)
    if keys[pygame.K_DOWN]:
        thief.move(0, 1)

    # 警察エージェントの移動処理
    for cop in cops:
        if cop.x < thief.x:
            cop.move(1, 0)
        elif cop.x > thief.x:
            cop.move(-1, 0)
        if cop.y < thief.y:
            cop.move(0, 1)
        elif cop.y > thief.y:
            cop.move(0, -1)

    # 画面の描画処理
    screen.fill(BLACK)
    draw_field(screen, field)
    draw_agent(screen, thief)
    for cop in cops:
        draw_agent(screen, cop)
    
    # 画面の更新
    pygame.display.flip()
    
    # フレームレートの調整
    clock.tick(30)  # フレームレートを30に設定

# Pygameの終了
pygame.quit()
