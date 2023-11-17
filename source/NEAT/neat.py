import neat

from Game.game import Game


class NEAT:
    def __init__(self, config_path):
        self.config_path = config_path
        self.population = 0

    def run(self):
        config = neat.config.Config(
            neat.DefaultGenome,
            neat.DefaultReproduction,
            neat.DefaultSpeciesSet,
            neat.DefaultStagnation,
            self.config_path
        )
        self.population = neat.Population(config)
        new_game = Game(self.population)
        self.population.run(new_game.evaluate_genomes, 50)
