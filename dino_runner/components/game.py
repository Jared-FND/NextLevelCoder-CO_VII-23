import pygame
import random
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.cloud import Cloud

from dino_runner.utils.constants import (
    BG,
    ICON,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    TITLE,
    FPS, BACKGROUND,PINES,SKY
)

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = -575
        self.player = Dinosaur()
        self.sky_list = pygame.sprite.Group()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        for i in range(5):
           cloud = Cloud()
           cloud.rect.x = random.randrange(1100)
           cloud.rect.y = random.randrange(50)
           self.sky_list.add(cloud)
    
        while self.playing:
            for sky in self.sky_list:
                sky.update()
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        self.player.update(pygame.key.get_pressed())
        
       

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)  
        self.sky_list.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()
       
    def draw_background(self):
        image_width = BACKGROUND.get_width()
        self.screen.blit(SKY, (0,0))
        self.screen.blit(PINES,  (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(PINES, (image_width + self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BACKGROUND, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BACKGROUND, (image_width + self.x_pos_bg, self.y_pos_bg))
        
        
        
        if self.x_pos_bg <= -image_width:
            self.screen.blit(PINES, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.screen.blit(BACKGROUND, (image_width + self.x_pos_bg, self.y_pos_bg))
            
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
