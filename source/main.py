import os.path

from NEAT.neat import NEAT

if __name__ == '__main__':
    local_directory = os.path.dirname(__file__)
    config_path = os.path.join(local_directory, "NEAT/config.txt")
    NEAT = NEAT(config_path)
    NEAT.run()
