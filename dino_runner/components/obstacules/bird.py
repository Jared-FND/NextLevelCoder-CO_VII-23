from dino_runner.components.obstacules.obstacule import Obstacle
from dino_runner.utils.constants import BIRD
import random

class Bird (Obstacle):
    def __init__(self):
        self.image = BIRD[0]
        super().__init__(self.image)
        self.rect.y = 250
        self.counter = 0
        
    def update(self, game):
        self.rect.x -= game.game_speed
        self.counter += 1
        self.image = BIRD[0] if self.counter % 4 else BIRD[1]