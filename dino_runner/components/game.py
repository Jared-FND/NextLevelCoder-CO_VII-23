import pygame
import random
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.cloud import Cloud
from dino_runner.components.faros import Faros
from dino_runner.components.obstacules.obstacule_manager import ObstacleMager
from dino_runner.utils.constants import (
    BG,
    ICON,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    TITLE,
    FPS, TRAKLINE1,SKY
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
        self.y_pos_bg =-450
        self.player = Dinosaur()
        self.sky_list = pygame.sprite.Group()
        self.faro_list = pygame.sprite.Group()
        self.obstacle_manajer = ObstacleMager()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        for i in range(5):
           cloud = Cloud()
           cloud.rect.x = random.randrange(0, 1100, 180)
           cloud.rect.y = random.randrange(20)
           self.sky_list.add(cloud)
        

        for i in range(40):
           faros = Faros()
           faros.rect.x = random.randrange(0, 1100, 180)
           faros.rect.y = 305
           self.faro_list.add(faros)
            
        while self.playing:
          
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
        self.obstacle_manajer.update(self)
        for sky in self.sky_list:
                sky.update()
        for faro in self.faro_list:
                faro.update()
            
        
       

    def draw(self):
        self.clock.tick(FPS)
       
        self.screen.fill((255, 255, 255))
        
        self.draw_background()
        self.faro_list.draw(self.screen)
        self.sky_list.draw(self.screen)
        self.player.draw(self.screen)
        self.obstacle_manajer.draw(self.screen)
        
        pygame.display.update()
        pygame.display.flip()
       

    def draw_background(self):
        image_width = TRAKLINE1.get_width()
        self.screen.blit(SKY, (0,0))
        
        self.screen.blit(TRAKLINE1, (self.x_pos_bg, self.y_pos_bg))
        
        self.screen.blit(TRAKLINE1 ,(image_width + self.x_pos_bg, self.y_pos_bg))

        if self.x_pos_bg <= -image_width:
           
            self.screen.blit(TRAKLINE1, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed