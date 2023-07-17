import pygame 
import random
from dino_runner.utils.constants import CLOUDS

class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  # Llamar al constructor de la clase base Sprite
        self.image = CLOUDS
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x -= 1
        if self.rect.x < -344:
            self.rect.x = 1110
            self.rect.y = random.randrange(50)