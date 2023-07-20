import pygame
from pygame.sprite import Sprite
from dino_runner.components.robot_shot import BulletPlayer
from dino_runner.utils.constants import RUNNING, DUCKING, JUMPING, DEFAULT_TYPE, SHIELD_TYPE, DUCKING_SHIELD, JUMPING_SHIELD, RUNNING_SHIELD, ROBOT_SHOT

class Dinosaur(Sprite):
    POS_X = 80
    POS_Y = 300
    DUK_POS_Y = 340
    JUMP_SPEED = 8.5

    def __init__(self, game):
        super().__init__()  # Llamar al constructor de la clase base Sprite
        self.running_img = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD}
        self.jumping_img = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD}
        self.dunking_img = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD}
        self.shoting_img = {DEFAULT_TYPE: ROBOT_SHOT, SHIELD_TYPE: ROBOT_SHOT}
        self.type = DEFAULT_TYPE
        self.image = self.running_img[self.type][0]
        self.game = game
        self.rect = self.image.get_rect()
        self.rect.x = self.POS_X
        self.rect.y = self.POS_Y
        self.step_index = 0
        self.running = True
        self.jumping = False
        self.dunking = False
        self.shoting = False
        self.jumping_velocity = self.JUMP_SPEED
        self.setup_states()
        self.shot_list = pygame.sprite.Group()
        self.jump_sound_played = False
        self.dunk_sound_played = False
        self.shot_sound_played = False

    def setup_states(self):
        self.has_powerup = False
        self.has_shield = False

    def update(self, user_input):
        if self.running:
            self.run()
        if self.dunking:
            self.dunk()
        if self.jumping:
            self.jump()
        if self.shoting:
            self.shot()

        if user_input[pygame.K_DOWN] or user_input[pygame.K_s] and not self.jumping:
            self.jumping = False
            self.running = False
            self.dunking = True
            self.shoting = False
            if not self.dunk_sound_played:
                self.game.music.list_sound[1].play()
                self.dunk_sound_played = True
                self.jump_sound_played = False
                self.shot_sound_played = False
        elif user_input[pygame.K_SPACE] and not self.jumping and not self.dunking and self.game.bulet_shots > 0:
            self.jumping = False
            self.running = False
            self.dunking = False
            self.shoting = True
            if not self.shot_sound_played:
                self.game.music.list_sound[2].play()
                self.shot_sound_played = True
                self.jump_sound_played = False
                self.dunk_sound_played = False
        elif user_input[pygame.K_UP]:
            self.jumping = True
            self.running = False
            self.dunking = False
            self.shoting = False
            if not self.jump_sound_played:
                self.game.music.list_sound[0].play()
                self.jump_sound_played = True
                self.dunk_sound_played = False
                self.shot_sound_played = False
        elif not self.jumping:
            self.jumping = False
            self.running = True
            self.dunking = False
            self.shoting = False
            self.jump_sound_played = False
            self.dunk_sound_played = False
            self.shot_sound_played = False

        for shot in self.shot_list:
            shot.update(self.game)
        if not self.jumping and not self.dunking and not self.shoting:
            self.running = True

        if self.step_index > 10:
            self.step_index = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.shot_list.draw(screen)

    def run(self):
        self.image = self.running_img[self.type][0 if self.step_index % 5 == 0 else 1]
        self.rect = self.image.get_rect()
        self.rect.x = self.POS_X
        self.rect.y = self.POS_Y
        self.step_index += 1

    def jump(self):
        self.image = self.jumping_img[self.type]
        self.rect.y -= self.jumping_velocity * 4
        self.jumping_velocity -= 0.8

        if self.rect.y >= self.POS_Y:
            self.rect.y = self.POS_Y
            self.jumping = False
            self.jumping_velocity = self.JUMP_SPEED

    def dunk(self):
        self.image = self.dunking_img[self.type][0 if self.step_index % 5 == 0 else 1]
        self.rect = self.image.get_rect()
        self.rect.x = self.POS_X
        self.rect.y = self.DUK_POS_Y
        self.step_index += 1

    def shot(self):
        self.image = self.shoting_img[self.type][0]
        if not self.shot_sound_played:
            self.game.music.list_sound[2].play()
            self.shot_sound_played = True
            self.jump_sound_played = False
            self.dunk_sound_played = False

        shot = BulletPlayer()
        self.shot_list.add(shot)
        self.game.bulet_shots -= 1
        self.rect = self.image.get_rect()
        self.rect.x = self.POS_X
        self.rect.y = self.POS_Y
        self.step_index += 1
