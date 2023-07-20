import pygame
from dino_runner.utils.constants import LASER,SHIELD_TYPE,DEFAULT_TYPE

class BulletPlayer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = LASER
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 340

    def update(self,game):
        self.rect.x += 30
        if self.rect.colliderect(game.obstacle_manajer.obstacle.rect):
            game.obstacle_manajer.has_obstacle = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)