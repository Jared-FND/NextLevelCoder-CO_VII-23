import pygame
import os
pygame.mixer.init() 

# Global Constants
TITLE = "Next Level Coder CO"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Robot/robot_walk1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Robot/robot_walk2.png")),
]


RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Robot/bufed_walk1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Robot/bufed_walk2.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Robot/robot_jump.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Robot/bufed_jump.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Robot/robot_dunk1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Robot/robot_dunk2.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Robot/robot_dunk1_bufed.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Robot/robot_dunk2_bufed.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]

ENEMY_ROBOT =[ 
            pygame.image.load(os.path.join(IMG_DIR, 'Robot/robot_enemy2.png')),
            pygame.image.load(os.path.join(IMG_DIR, 'Robot/robot_enemy3.png'))
]

FAROS = [
       pygame.image.load(os.path.join(IMG_DIR, 'Other/faro1.png')),
       pygame.image.load(os.path.join(IMG_DIR,'Other/faro2.png' )),
]
ROBOT_SHOT = [
       pygame.image.load(os.path.join(IMG_DIR,'Robot/robot_shot1.png' )),
       pygame.image.load(os.path.join(IMG_DIR,'Robot/robot_shot2.png' )),
]


CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

TRAKLINE1 = pygame.image.load(os.path.join(IMG_DIR, 'Other/trackline_1.png'))

TRAKLINE2 = pygame.image.load(os.path.join(IMG_DIR, 'Other/trackline_2.png'))

CLOUDS= pygame.image.load(os.path.join(IMG_DIR, 'Other/clouds_1.png'))

PINES = pygame.image.load(os.path.join(IMG_DIR, 'Other/3.png'))

SKY = pygame.image.load(os.path.join(IMG_DIR, 'Other/sky.png'))

ENEMY_SKY_ROBOT =  pygame.image.load(os.path.join(IMG_DIR, 'Robot/sky_enemy_robot.png'))

SHOT =  pygame.image.load(os.path.join(IMG_DIR, 'Other/shot.png'))

CLOCK =  pygame.image.load(os.path.join(IMG_DIR, 'Other/clock.png'))

LASER = pygame.image.load(os.path.join(IMG_DIR, 'Other/laser.png'))

LASER_SOUD = pygame.mixer.Sound(os.path.join(IMG_DIR, 'song/laser.ogg'))

JUMP_SOUND = pygame.mixer.Sound(os.path.join(IMG_DIR, 'song/jump.mp3'))

DUNK_SOUND = pygame.mixer.Sound(os.path.join(IMG_DIR, 'song/dunk.mp3'))

DEFAULT_SONG = pygame.mixer.music.load(os.path.join(IMG_DIR, 'song/TheLigth.mp3'))


DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
