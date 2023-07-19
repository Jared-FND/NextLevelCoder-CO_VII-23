from dino_runner.components.power_up.shield import Shield
from dino_runner.components.power_up.shot import Shot
import random
import pygame

class PowerUpManager:

    def __init__(self):
        self.has_powerup = False
        self.powerup = None
        self.next_powerup_show = random.randrange(30)

    def update(self, game):
        print(game.score, self.next_powerup_show)
        if not self.has_powerup and game.score == self.next_powerup_show:
            self.create_powerup()
        if self.powerup and self.powerup.rect.x > 0:  
            self.has_powerup = True
        else:
            self.has_powerup = False

        if self.has_powerup:
            self.powerup.update(game.game_speed)
            if game.player.rect.colliderect(self.powerup.rect):
                self.has_powerup = False
                self.powerup = None
            if game.score > self.next_powerup_show:
                 self.next_powerup_show = self.new_powerup_show()

    def new_powerup_show(self):
        last_power_up = self.next_powerup_show 
        return last_power_up + 100 

    def create_powerup(self):
        powerup_list = [Shield(), Shot()]
        self.powerup = random.choice(powerup_list)

    def draw(self, screen):
        if self.has_powerup:
            self.powerup.draw(screen)
