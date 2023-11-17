from Game.obstacle import Obstacle


class Pterodactyl(Obstacle):
    def __init__(self, image, game_speed, obstacles):
        self.type = 3
        super().__init__(image, 0, game_speed, obstacles)
        self.rectangle.y = 250
        self.index = 0

    def draw(self, screen):
        if self.index >= 9:
            self.index = 0
        screen.blit(self.image[self.index // 5], self.rectangle)
        self.index += 1