from constants import *


class Obstacle:
    def __init__(self, image, type, game_speed, obstacles):
        self.game_speed = game_speed
        self.image = image
        self.type = type
        self.obstacles = obstacles
        self.rectangle = self.image[self.type].get_rect()
        self.rectangle.x = SCREEN_WIDTH

    def update(self):
        self.rectangle.x -= self.game_speed
        if self.rectangle.x < - self.rectangle.width:
            self.obstacles.pop()

    def draw(self, screen):
        screen.blit(self.image[self.type], self.rectangle)
