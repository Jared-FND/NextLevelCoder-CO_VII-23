import pygame
from dino_runner.components.obstacules.obstacule import Obstacle
from dino_runner.components.obstacules.bulet import Bullet
from dino_runner.utils.constants import ENEMY_ROBOT
import pygame

class EnemyRobot(Obstacle):
    def __init__(self):
        self.image = ENEMY_ROBOT[0]
        super().__init__(self.image)
        self.rect.y = 305
        self.counter = 0
        self.timer_interval = 5000  
        self.timer_active = True
        self.start_time = pygame.time.get_ticks()
        self.shots_list = pygame.sprite.Group()

    def update(self, game):
        self.rect.x = 1000
        self.counter += 1
        for shot in self.shots_list:
            shot.update(game)
        if self.counter % 20 == 0:
            
            self.image = ENEMY_ROBOT[1]

            game.music.list_sound[2].play()
            shot = Bullet()
            self.shots_list.add(shot)
            
        else:
            self.image = ENEMY_ROBOT[0]
           

        if self.timer_active:
            current_time = pygame.time.get_ticks()
            if current_time - self.start_time >= self.timer_interval:
                self.timer_active = False
                self.rect.x = -100  

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.shots_list.draw(screen)
