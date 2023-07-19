from dino_runner.components.obstacules.obstacule import Obstacle
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS
import random

class Cactus (Obstacle):
    def __init__(self):

        images = SMALL_CACTUS + LARGE_CACTUS
        self.image = random.choice(images)
        super().__init__(self.image)
        self.rect.y = 400 - self.image.get_height()
       