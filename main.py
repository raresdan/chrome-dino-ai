import pygame
import os

pygame.init()

# constants
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

RUNNING = [pygame.image.load(os.path.join("Assets/Dino", "DinoRun1.png")),
           pygame.image.load(os.path.join("Assets/Dino", "DinoRun2.png"))]
JUMPING = [pygame.image.load(os.path.join("Assets/Dino", "DinoJump.png"))]
DUCKING = [pygame.image.load(os.path.join("Assets/Dino", "DinoDuck1.png")),
           pygame.image.load(os.path.join("Assets/Dino", "DinoDuck2.png"))]
SMALL_CACTUS = [pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus1.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus3.png"))]
LARGE_CACTUS = [pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus1.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus3.png"))]
PTERODACTYL = [pygame.image.load(os.path.join("Assets/Bird", "Bird1.png")),
               pygame.image.load(os.path.join("Assets/Bird", "Bird2.png"))]
CLOUD = [pygame.image.load(os.path.join("Assets/Other", "Cloud.png"))]
BACKGROUND = [pygame.image.load(os.path.join("Assets/Other", "Track.png"))]


class Dinosaur:
    X_POS = 80
    Y_POS = 310

    def __init__(self):
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING
        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False
        self.step_index = 0
        self.image = self.run_img[0]
        self.dino_rectangle = self.image.get_rect()
        self.dino_rectangle.x = self.X_POS
        self.dino_rectangle.y = self.Y_POS

    def update(self, user_input):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()
        if self.step_index >= 10:
            self.step_index = 0

        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_jump = True
            self.dino_duck = False
            self.dino_run = False
        elif user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_jump = False
            self.dino_duck = True
            self.dino_run = False
        elif not (self.dino_jump or user_input[pygame.K_DOWN]):
            self.dino_jump = False
            self.dino_duck = False
            self.dino_run = True

    def duck(self):
        pass

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.dino_rectangle = self.image.get_rect()
        self.dino_rectangle.x = self.X_POS
        self.dino_rectangle.y = self.Y_POS
        self.step_index += 1

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rectangle.x, self.dino_rectangle.y))

    def jump(self):
        pass


def main():
    run = True
    clock = pygame.time.Clock()
    player = Dinosaur()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        SCREEN.fill((255, 255, 255))
        user_input = pygame.key.get_pressed()
        player.draw(SCREEN)
        player.update(user_input)
        clock.tick(30)
        pygame.display.update()


main()
