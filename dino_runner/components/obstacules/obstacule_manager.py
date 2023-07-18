from dino_runner.components.obstacules.cactus import Cactus


class ObstacleMager ():

    def __init__(self) :
        self.has_obstacle = False
        self.obstacle = None

    def update(self,game):
        if not self.has_obstacle:
            self.create_obstacle()
        if self.obstacle.rect.x > 0:
            self.has_obstacle = True
        else:
            self.has_obstacle = False
        self.obstacle.update(game.game_speed)
    def create_obstacle(self):
        self.obstacle = Cactus()


    def draw(self,screen):
        if self.has_obstacle:
            self.obstacle.draw(screen)