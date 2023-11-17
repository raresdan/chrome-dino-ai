import random

from Game.obstacle import Obstacle


class SmallCactus(Obstacle):
    def __init__(self, image, game_speed, obstacles):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type, game_speed, obstacles)
        self.rectangle.y = 325


class LargeCactus(Obstacle):
    def __init__(self, image, game_speed, obstacles):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type, game_speed, obstacles)
        self.rectangle.y = 300
