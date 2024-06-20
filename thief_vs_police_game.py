import pygame
import random
import numpy as np
import gym
from gym import spaces

class ThiefPoliceEnv(gym.Env):
    def __init__(self):
        super(ThiefPoliceEnv, self).__init__()
        self.width = 800
        self.height = 600
        self.grid_size = 50
        self.player_size = 50
        self.police_size = 50
        self.player_pos = [self.width // 2, self.height // 2]
        self.police_pos = [random.randint(0, self.width - self.police_size), random.randint(0, self.height - self.police_size)]
        self.action_space = spaces.Discrete(5)  # 上下左右静止
        self.observation_space = spaces.Box(low=0, high=max(self.width, self.height), shape=(4,), dtype=np.float32)

    def reset(self):
        self.player_pos = [self.width // 2, self.height // 2]
        self.police_pos = [random.randint(0, self.width - self.police_size), random.randint(0, self.height - self.police_size)]
        return self._get_discrete_state()

    def step(self, action):
        if action == 0:
            self.player_pos[1] -= self.grid_size  # 上
        elif action == 1:
            self.player_pos[1] += self.grid_size  # 下
        elif action == 2:
            self.player_pos[0] -= self.grid_size  # 左
        elif action == 3:
            self.player_pos[0] += self.grid_size  # 右
        # else: 静止

        self.player_pos[0] = np.clip(self.player_pos[0], 0, self.width - self.player_size)
        self.player_pos[1] = np.clip(self.player_pos[1], 0, self.height - self.player_size)

        reward = -np.linalg.norm(np.array(self.player_pos) - np.array(self.police_pos))

        done = False
        if self.player_pos == self.police_pos:
            done = True
            reward -= 100

        return self._get_discrete_state(), reward, done, {}

    def _get_discrete_state(self):
        discrete_state = (
            self.player_pos[0] // self.grid_size,
            self.player_pos[1] // self.grid_size,
            self.police_pos[0] // self.grid_size,
            self.police_pos[1] // self.grid_size
        )
        return tuple(discrete_state)

    def render(self, mode='human'):
        if mode == 'human':
            screen.fill((0, 0, 0))
            pygame.draw.rect(screen, (0, 0, 255), (self.player_pos[0], self.player_pos[1], self.player_size, self.player_size))
            pygame.draw.rect(screen, (255, 0, 0), (self.police_pos[0], self.police_pos[1], self.police_size, self.police_size))
            pygame.display.flip()

import numpy as np

class QLearningAgent:
    def __init__(self, action_space, state_space, learning_rate=0.1, discount_factor=0.99, exploration_rate=1.0, exploration_decay=0.995):
        self.action_space = action_space
        self.state_space = state_space
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate
        self.exploration_decay = exploration_decay

        # 状態空間を離散化したものに基づいてQテーブルを初期化
        self.q_table = np.zeros(state_space + (action_space,))
        
        # 新しい乱数生成器の初期化
        self.rng = np.random.default_rng(seed=123)

    def choose_action(self, state):
        if self.rng.random() < self.exploration_rate:
            return self.rng.integers(self.action_space)
        return np.argmax(self.q_table[state])

    def learn(self, state, action, reward, next_state):
        predict = self.q_table[state][action]
        target = reward + self.discount_factor * np.max(self.q_table[next_state])
        self.q_table[state][action] += self.learning_rate * (target - predict)
        self.exploration_rate *= self.exploration_decay

# 環境の初期化
env = ThiefPoliceEnv()

# エージェントの初期化
state_space = (
    env.width // env.grid_size,
    env.height // env.grid_size,
    env.width // env.grid_size,
    env.height // env.grid_size
)
agent = QLearningAgent(env.action_space.n, state_space)

# 学習の実行
episodes = 1
# 1000

for episode in range(episodes):
    state = env.reset()

    done = False
    while not done:
        action = agent.choose_action(state)
        next_state, reward, done, _ = env.step(action)
        agent.learn(state, action, reward, next_state)
        state = next_state

    if episode % 100 == 0:
        print(f"Episode {episode}, Exploration Rate: {agent.exploration_rate}")

# Pygameの初期化
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Thief and Police")

# ゲームループ
done = False
state = env.reset()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    action = agent.choose_action(state)
    next_state, reward, done, _ = env.step(action)
    state = next_state

    env.render()
    pygame.time.delay(100)

pygame.quit()
