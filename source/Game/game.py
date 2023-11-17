import math
import random
import sys

import neat.nn
import pygame.font

from Game.cactus import SmallCactus, LargeCactus
from Game.cloud import Cloud
from Game.dinosaur import Dinosaur
from Game.pterodactyl import Pterodactyl
from Game.constants import *

pygame.init()
font = pygame.font.Font("freesansbold.ttf", 20)


class Game:
    def __init__(self, population):
        self.population = population

        self.game_speed = 14
        self.x_position_background = 0
        self.y_position_background = 380
        self.obstacles = []
        self.dinosaurs = []
        self.all_genomes = []
        self.neural_nets = []
        self.points = 0
        self.clock = pygame.time.Clock()

    def remove(self, index):
        self.dinosaurs.pop(index)
        self.all_genomes.pop(index)
        self.neural_nets.pop(index)

    @staticmethod
    def distance(position_a, position_b):
        distance_x = position_a[0] - position_b[0]
        distance_y = position_a[1] - position_b[1]
        return math.sqrt(distance_x ** 2 + distance_y ** 2)

    def prepare_run(self):
        self.game_speed = 14
        self.x_position_background = 0
        self.y_position_background = 380
        self.obstacles = []
        self.dinosaurs = []
        self.all_genomes = []
        self.neural_nets = []
        self.points = 0

    def evaluate_genomes(self, genomes, config_file):
        self.prepare_run()
        cloud = Cloud(self.game_speed)
        run = True

        for genome_id, genome in genomes:
            self.dinosaurs.append(Dinosaur())
            self.all_genomes.append(genome)
            neural_net = neat.nn.FeedForwardNetwork.create(genome, config_file)
            self.neural_nets.append(neural_net)
            genome.fitness = 0

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            SCREEN.fill((255, 255, 255))

            self.background()

            for dinosaur in self.dinosaurs:
                dinosaur.update()
                dinosaur.draw(SCREEN)

            if len(self.dinosaurs) == 0:
                break
            if len(self.obstacles) == 0:
                magic_number = random.randint(0, 3)
                if magic_number == 0:
                    self.obstacles.append(SmallCactus(SMALL_CACTUS, self.game_speed, self.obstacles))
                elif magic_number == 1:
                    self.obstacles.append(LargeCactus(LARGE_CACTUS, self.game_speed, self.obstacles))
                elif magic_number == 2:
                    self.obstacles.append(Pterodactyl(PTERODACTYL, self.game_speed, self.obstacles))
            for obstacle in self.obstacles:
                obstacle.draw(SCREEN)
                obstacle.update()
                for i, dinosaur in enumerate(self.dinosaurs):
                    if dinosaur.dino_rectangle.colliderect(obstacle.rectangle):
                        self.all_genomes[i].fitness -= 10
                        self.remove(i)
                    else:
                        self.all_genomes[i].fitness += 1
            for i, dinosaur in enumerate(self.dinosaurs):
                if self.obstacles:
                    output = self.neural_nets[i].activate(
                        (dinosaur.dino_rectangle.centerx, dinosaur.dino_rectangle.centery,
                         self.obstacles[0].rectangle.centerx, self.obstacles[0].rectangle.centery,
                         abs(dinosaur.dino_rectangle.centerx - self.obstacles[0].rectangle.centerx),
                         abs(dinosaur.dino_rectangle.centery - self.obstacles[0].rectangle.centery),
                         self.obstacles[0].type, self.game_speed))

                    print(output)

                    if output[0] > 0.5:
                        if output[1] > 0.5 and not dinosaur.dino_duck:
                            dinosaur.dino_run = False
                            dinosaur.dino_jump = True
                        elif output[2] > 0.5 and not dinosaur.dino_jump:
                            dinosaur.dino_run = False
                            dinosaur.dino_duck = True
                    else:
                        dinosaur.dino_run = True
                        dinosaur.dino_jump = False
                        dinosaur.dino_duck = False

            cloud.draw(SCREEN)
            cloud.update()
            self.score()
            self.statistics()
            pygame.display.update()
            self.clock.tick(30)

    def score(self):
        self.points += 1
        if self.points % 100 == 0:
            self.game_speed += 1
        text = font.render("Score: " + str(self.points), True, (0, 0, 0))
        text_rectangle = text.get_rect()
        text_rectangle.center = (1000, 40)
        SCREEN.blit(text, text_rectangle)

    def background(self):
        if pygame.display.get_surface() is not None:
            image_width = BACKGROUND.get_width()
            SCREEN.blit(BACKGROUND, (self.x_position_background, 380))
            SCREEN.blit(BACKGROUND, (image_width + self.x_position_background, 380))
            if self.x_position_background <= - image_width:
                SCREEN.blit(BACKGROUND, (image_width + self.x_position_background, 380))
                self.x_position_background = 0
            self.x_position_background -= self.game_speed

    def statistics(self):
        text_1 = font.render(f"Dinosaurs Alive: {str(len(self.dinosaurs))}", True, (0, 0, 0))
        text_2 = font.render(f"Generation: {self.population.generation + 1}", True, (0, 0, 0))
        text_3 = font.render(f"Game Speed: {str(self.game_speed)}", True, (0, 0, 0))
        SCREEN.blit(text_1, (50, 450))
        SCREEN.blit(text_2, (50, 480))
        SCREEN.blit(text_3, (50, 510))
