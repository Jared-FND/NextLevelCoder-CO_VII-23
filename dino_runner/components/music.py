from dino_runner.utils.constants import DEFAULT_SONG, JUMP_SOUND, DUNK_SOUND, LASER_SOUD
import pygame 

class Music():
    def __init__(self):
        self.song =  DEFAULT_SONG
        self.list_sound = [JUMP_SOUND,DUNK_SOUND,LASER_SOUD]
   
    def play_background_music():
        pygame.mixer.music.play(-1)





    