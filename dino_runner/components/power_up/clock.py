from dino_runner.components.power_up.power_up import PowerUp
from dino_runner.utils.constants import CLOCK,SCREEN_HEIGHT
class Clock(PowerUp):

    def __init__(self) :
        self.image= CLOCK
        super().__init__(self.image)
        self.rect.x = SCREEN_HEIGHT - self.image.get_height()
       