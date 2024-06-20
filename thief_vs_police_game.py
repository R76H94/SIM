import pygame
import random
import numpy as np
from stable_baselines3 import PPO
from stable_baselines3.common.envs import DummyVecEnv
from stable_baselines3.common.evaluation import evaluate_policy
from gym import spaces
import gym

# ゲーム環境の定義
class ThiefPoliceEnv(gym.Env):
    def __init__(self):
        super(ThiefPoliceEnv, self).__init__()
        self.width = 800
        self.height = 600
        self.player_size = 50
        self.police_size = 50
        self.player_pos = [self.width // 2, self.height // 2]
        self.police_pos = [random.randint(0, self.width-self.police_size), random.randint(0, self.height-self.police_size)]
        self.action_space = spaces.Discrete(5) # 上下左右静止
        self.observation_space = spaces.Box(low=0, high=max(self.width, self.height), shape=(4,), dtype=np.float32)

    def reset(self):
        self.player_pos = [self.width // 2, self.height // 2]
        self.police_pos = [random.randint(0, self.width-self.police_size), random.randint(0, self.height-self.police_size)]
        return np.array(self.player_pos + self.police_pos, dtype=np.float32)

    def step(self, action):
        if action == 0:
            self.player_pos[1] -= 5  # 上
        elif action == 1:
            self.player_pos[1] += 5  # 下
        elif action == 2:
            self.player_pos[0] -= 5  # 左
        elif action == 3:
            self.player_pos[0] += 5  # 右
        # else: 静止

        self.player_pos[0] = np.clip(self.player_pos[0], 0, self.width - self.player_size)
        self.player_pos[1] = np.clip(self.player_pos[1], 0, self.height - self.player_size)

        reward = -np.linalg.norm(np.array(self.player_pos) - np.array(self.police_pos))

        if self.player_pos == self.police_pos:
            done = True
            reward -= 100
        else:
            done = False

        return np.array(self.player_pos + self.police_pos, dtype=np.float32), reward, done, {}

    def render(self, mode='human'):
        if mode == 'human':
            screen.fill((0, 0, 0))
            pygame.draw.rect(screen, (0, 0, 255), (self.player_pos[0], self.player_pos[1], self.player_size, self.player_size))
            pygame.draw.rect(screen, (255, 0, 0), (self.police_pos[0], self.police_pos[1], self.police_size, self.police_size))
            pygame.display.flip()

# 環境の初期化
env = ThiefPoliceEnv()
env = DummyVecEnv([lambda: env])

# モデルの訓練
model = PPO('MlpPolicy', env, verbose=1)
model.learn(total_timesteps=10000)

# 訓練済みモデルの評価
mean_reward, std_reward = evaluate_policy(model, env, n_eval_episodes=10)
print(f"Mean reward: {mean_reward} +/- {std_reward}")

# Pygameの初期化
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Thief and Police")

# ゲームループ
done = False
obs = env.reset()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    action, _states = model.predict(obs)
    obs, rewards, dones, info = env.step(action)
    env.render()

    if dones:
        obs = env.reset()

    pygame.time.delay(100)

pygame.quit()
