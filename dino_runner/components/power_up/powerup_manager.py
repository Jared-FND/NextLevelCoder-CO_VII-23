import pygame
from dino_runner.components.power_up.shield import Shield
from dino_runner.components.power_up.shot import Shot
from dino_runner.components.power_up.clock import Clock
import random

class PowerUpManager:

    def __init__(self):
        self.has_powerup = False
        self.powerup = None
        self.next_powerup_show = random.randrange(30)
        self.clock_powerup_start_time = 0  
        self.clock_powerup_duration = 5000  

    def update(self, game):
        if not self.has_powerup and game.score == self.next_powerup_show:
            self.create_powerup()
        if self.powerup and self.powerup.rect.x > 0:
            self.has_powerup = True
        else:
            self.has_powerup = False

        if self.has_powerup:
            self.powerup.update(game)
            if game.player.rect.colliderect(self.powerup.rect):
                self.has_powerup = False
                game.player.type = self.powerup.type
                if isinstance(self.powerup, Shot):
                    game.bulet_shots += 1
                self.powerup = None
                if isinstance(self.powerup, Clock):
                    
                    self.clock_powerup_start_time = pygame.time.get_ticks()
                    game.increase_score(10)  
            if game.score > self.next_powerup_show:
                self.next_powerup_show = self.new_powerup_show()

            if self.clock_powerup_start_time > 0 and pygame.time.get_ticks() - self.clock_powerup_start_time >= self.clock_powerup_duration:
              
                game.game_speed -= 5
                self.clock_powerup_start_time = 0 

    def new_powerup_show(self):
        return self.next_powerup_show + 100

    def create_powerup(self):
        powerup_list = [Shield(), Shot(), Clock()]  # Agregar el power-up de reloj a la lista
        self.powerup = random.choice(powerup_list)

    def draw(self, screen):
        if self.has_powerup:
            self.powerup.draw(screen)
