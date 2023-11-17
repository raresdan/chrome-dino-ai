import random

from Game.constants import *


class Cloud:
    def __init__(self, game_speed):
        self.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = CLOUD
        self.width = self.image.get_width()
        self.game_speed = game_speed

    def update(self):
        self.x -= self.game_speed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self, screen):
        if pygame.display.get_surface() is not None:
            screen.blit(self.image, (self.x, self.y))
