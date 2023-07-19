from dino_runner.components.obstacules.obstacule import Obstacle
from dino_runner.utils.constants import ENEMY_ROBOT
import random

class EnemyRobot (Obstacle):
    def __init__(self):
        self.image = ENEMY_ROBOT[0]
        super().__init__(self.image)
        self.rect.y = 300
        self.counter = 0
        
    def update(self, game_speed):
        self.rect.x -= game_speed
        self.counter += 1
        self.image = ENEMY_ROBOT[0] if self.counter % 2 == 0 else ENEMY_ROBOT[1] 