import pygame
import os

pygame.init()

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

RUNNING = [pygame.image.load(os.path.join("../chrome-dino/Assets/Dino", "DinoRun1.png")),
           pygame.image.load(os.path.join("../chrome-dino/Assets/Dino", "DinoRun2.png"))]
JUMPING = pygame.image.load(os.path.join("../chrome-dino/Assets/Dino", "DinoJump.png"))
DUCKING = [pygame.image.load(os.path.join("../chrome-dino/Assets/Dino", "DinoDuck1.png")),
           pygame.image.load(os.path.join("../chrome-dino/Assets/Dino", "DinoDuck2.png"))]

SMALL_CACTUS = [pygame.image.load(os.path.join("../chrome-dino/Assets/Cactus", "SmallCactus1.png")),
                pygame.image.load(os.path.join("../chrome-dino/Assets/Cactus", "SmallCactus2.png")),
                pygame.image.load(os.path.join("../chrome-dino/Assets/Cactus", "SmallCactus3.png"))]
LARGE_CACTUS = [pygame.image.load(os.path.join("../chrome-dino/Assets/Cactus", "LargeCactus1.png")),
                pygame.image.load(os.path.join("../chrome-dino/Assets/Cactus", "LargeCactus2.png")),
                pygame.image.load(os.path.join("../chrome-dino/Assets/Cactus", "LargeCactus3.png"))]

PTERODACTYL = [pygame.image.load(os.path.join("../chrome-dino/Assets/Bird", "Bird1.png")),
               pygame.image.load(os.path.join("../chrome-dino/Assets/Bird", "Bird2.png"))]

CLOUD = pygame.image.load(os.path.join("../chrome-dino/Assets/Other", "Cloud.png"))
BACKGROUND = pygame.image.load(os.path.join("../chrome-dino/Assets/Other", "Track.png"))
