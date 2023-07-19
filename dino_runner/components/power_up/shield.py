from dino_runner.components.power_up.power_up import PowerUp
from dino_runner.utils.constants import SHIELD
class Shield(PowerUp):

    def __init__(self) :
        self.image= SHIELD
        super().__init__(self.image)
       