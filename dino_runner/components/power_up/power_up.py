
from typing import Any
from pygame.sprite import Sprite
from dino_runner.utils.constants import  SCREEN_WIDTH

class PowerUp(Sprite):
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x =  SCREEN_WIDTH + 50
        self.rect.y = 280

    def update(self, game_speed):
         self.rect.x -= game_speed
         
    def draw(self,screen):
        screen.blit(self.image, self.rect)    

     
