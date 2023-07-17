import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import RUNNING, DUCKING, JUMPING

class Dinosaur(Sprite):
    POS_X = 80
    POS_Y = 300
    DUK_POS_Y = 340
    JUMP_SPEED = 8.5

    def __init__(self):
        super().__init__()  # Llamar al constructor de la clase base Sprite
        self.image = RUNNING[0]
        self.rect = self.image.get_rect()
        self.rect.x = self.POS_X
        self.rect.y = self.POS_Y
        self.step_index = 0
        self.running = True
        self.jumping = False
        self.dunking = False
        self.jumping_velocity = self.JUMP_SPEED

    def update(self, user_input):
        if self.running:
            self.run()
        if self.dunking:
            self.dunk()
        if self.jumping:
            self.jump()

        if user_input[pygame.K_DOWN] or user_input[pygame.K_s] and not self.jumping:
            self.jumping = False
            self.running = False
            self.dunking = True
        elif user_input[pygame.K_UP]:
            self.jumping = True
            self.running = False
            self.dunking = False
        elif not self.jumping :
            self.jumping = False
            self.running = True
            self.dunking = False


        if not self.jumping and not self.dunking:
            self.running = True

        if self.step_index > 10:
            self.step_index = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def run(self):
        self.image = RUNNING[0] if self.step_index > 5 else RUNNING[1]
        self.rect = self.image.get_rect()
        self.rect.x = self.POS_X
        self.rect.y = self.POS_Y
        self.step_index += 1

    def jump(self):
        self.image = JUMPING
        self.rect.y -= self.jumping_velocity * 4
        self.jumping_velocity -= 0.8

        if self.rect.y >= self.POS_Y:
            self.rect.y = self.POS_Y
            self.jumping = False
            self.jumping_velocity = self.JUMP_SPEED

    def dunk(self):
        self.image = DUCKING[0] if self.step_index > 5 else DUCKING[1]
        self.rect = self.image.get_rect()
        self.rect.x = self.POS_X
        self.rect.y = self.DUK_POS_Y
        self.step_index += 1
