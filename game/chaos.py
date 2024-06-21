# chaos.py
import numpy as np

class ChaosMovement:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update_position(self):
        # ロジスティック写像などを使用したカオス的な位置更新
        r = 3.9  # パラメータ
        self.x = r * self.x * (1 - self.x)
        self.y = r * self.y * (1 - self.y)
        return self.x, self.y
