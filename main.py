import random

import pygame.font

from cactus import SmallCactus, LargeCactus
from cloud import Cloud
from constants import *
from dinosaur import Dinosaur
from pterodactyl import Pterodactyl

pygame.init()


def main():
    game_speed = 14
    run = True
    clock = pygame.time.Clock()
    player = Dinosaur()
    cloud = Cloud(game_speed)
    x_position_background = 0
    points = 0
    font = pygame.font.Font("freesansbold.ttf", 20)
    obstacles = []
    death_count = 0

    def score():
        nonlocal points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1
        text = font.render("Score: " + str(points), True, (0, 0, 0))
        text_rectangle = text.get_rect()
        text_rectangle.center = (1000, 40)
        SCREEN.blit(text, text_rectangle)

    def background():
        nonlocal x_position_background
        if pygame.display.get_surface() is not None:
            image_width = BACKGROUND.get_width()
            SCREEN.blit(BACKGROUND, (x_position_background, 380))
            SCREEN.blit(BACKGROUND, (image_width + x_position_background, 380))
            if x_position_background <= - image_width:
                SCREEN.blit(BACKGROUND, (image_width + x_position_background, 380))
                x_position_background = 0
            x_position_background -= game_speed

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        SCREEN.fill((255, 255, 255))
        user_input = pygame.key.get_pressed()
        player.draw(SCREEN)
        player.update(user_input)
        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(SmallCactus(SMALL_CACTUS, game_speed, obstacles))
            elif random.randint(0, 2) == 1:
                obstacles.append(LargeCactus(LARGE_CACTUS, game_speed, obstacles))
            elif random.randint(0, 2) == 1:
                obstacles.append(Pterodactyl(PTERODACTYL, game_speed, obstacles))
        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update()
            if player.dino_rectangle.colliderect(obstacle.rectangle):
                pygame.time.delay(2000)
                death_count += 1
                menu(death_count, points)
        background()
        cloud.draw(SCREEN)
        cloud.update()
        score()
        clock.tick(30)
        pygame.display.update()


def menu(death_count, points):
    text = None
    run = True
    while run:
        SCREEN.fill((255, 255, 255))
        font = pygame.font.Font("freesansbold.ttf", 30)
        if death_count == 0:
            text = font.render("Press any Key to Start", True, (0, 0, 0))
        elif death_count > 0:
            text = font.render("Press any Key to Start", True, (0, 0, 0))
            score = font.render("Score: " + str(points), True, (0, 0, 0))
            score_rectangle = score.get_rect()
            score_rectangle.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
            SCREEN.blit(score, score_rectangle)
        text_rectangle = text.get_rect()
        text_rectangle.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        SCREEN.blit(text, text_rectangle)
        SCREEN.blit(RUNNING[0], (SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2 - 140))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                main()


if __name__ == "__main__":
    menu(death_count=0, points=0)
