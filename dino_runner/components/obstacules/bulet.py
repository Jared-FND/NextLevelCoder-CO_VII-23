import pygame
from dino_runner.utils.constants import LASER,SHIELD_TYPE,DEFAULT_TYPE

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = LASER
        self.rect = self.image.get_rect()
        self.rect.x = 995
        self.rect.y = 320 

    def update(self,game):
        self.rect.x -= 30
        if self.rect.colliderect(game.player.rect):

            if game.player.type == SHIELD_TYPE:
                    game.player.type = DEFAULT_TYPE
                    self.rect.x = -10000
            else:
                pygame.time.delay(300)
                game.playing = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)