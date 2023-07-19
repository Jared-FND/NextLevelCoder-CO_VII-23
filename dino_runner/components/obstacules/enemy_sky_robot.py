from dino_runner.components.obstacules.obstacule import Obstacle
from dino_runner.utils.constants import ENEMY_SKY_ROBOT
import random

class EnemySkyRobot (Obstacle):
    def __init__(self):
        self.image = ENEMY_SKY_ROBOT
        super().__init__(self.image)
        self.rect.y = 200
        self.counter = 0
        
    def update(self, game_speed):
        self.rect.x -= game_speed
        self.counter += 1
        