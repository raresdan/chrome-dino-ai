import pygame.font

from cloud import Cloud
from constants import *
from dinosaur import Dinosaur

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
        background()
        cloud.draw(SCREEN)
        cloud.update()
        score()
        clock.tick(30)
        pygame.display.update()


if __name__ == "__main__":
    main()
