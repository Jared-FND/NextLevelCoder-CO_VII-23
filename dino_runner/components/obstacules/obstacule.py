from typing import Any
from pygame.sprite import Sprite
from dino_runner.utils.constants import  SCREEN_WIDTH

class Obstacle(Sprite):
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x =  SCREEN_WIDTH

    def update(self, game_speed):
         self.rect.x -= 20
         print(self.rect.x)
    def draw(self,screen):
        screen.blit(self.image, self.rect)    

     
