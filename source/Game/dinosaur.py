import random

from Game.constants import *


class Dinosaur:
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VELOCITY = 8.5

    def __init__(self):
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING
        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False
        self.step_index = 0
        self.jump_vel = self.JUMP_VELOCITY
        self.image = self.run_img[0]
        self.dino_rectangle = self.image.get_rect()
        self.dino_rectangle.x = self.X_POS
        self.dino_rectangle.y = self.Y_POS
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def update(self):
        if self.step_index >= 10:
            self.step_index = 0
        if self.dino_duck:
            self.duck()
        elif self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()

    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        self.dino_rectangle = self.image.get_rect()
        self.dino_rectangle.x = self.X_POS
        self.dino_rectangle.y = self.Y_POS_DUCK
        self.step_index += 1

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.dino_rectangle = self.image.get_rect()
        self.dino_rectangle.x = self.X_POS
        self.dino_rectangle.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
        if self.dino_jump:
            self.dino_rectangle.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < - self.JUMP_VELOCITY:
            self.dino_rectangle.y = self.Y_POS
            self.dino_jump = False
            self.dino_run = True
            self.jump_vel = self.JUMP_VELOCITY

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rectangle.x, self.dino_rectangle.y))
        pygame.draw.rect(SCREEN, self.color, (
            self.dino_rectangle.x, self.dino_rectangle.y, self.dino_rectangle.width, self.dino_rectangle.height), 2)
