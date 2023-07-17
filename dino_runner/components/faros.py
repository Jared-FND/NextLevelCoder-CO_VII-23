import pygame 
import random
from dino_runner.utils.constants import FAROS

class Faros(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  # Llamar al constructor de la clase base Sprite
        self.image = FAROS[0]
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.faros_range  = 500
        self.faros_count = 0
        

    def update(self):
        

        
        self.rect.x -= 5
        if self.rect.x < 0:
            self.faros_count += 1
            self.rect.x = 1110
            self.rect.y = 305
            
            self.image = FAROS[0] if self.faros_count % 2 == 0 else FAROS[1]