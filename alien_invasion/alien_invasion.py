#! python3

import sys

import pygame

from settings import Settings

class AlienInvasion:
    """A class dedicated to managing the resources and the way the game works."""

    def __init__(self):
        """Initializing the game and creating its resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien invasion")

    def run_game(self):
        """Starting the main loop of the program."""
        while True:
            #Waiting for a key or mouse button to be pressed.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #Refresh the screen during each iteration of the loop
            self.screen.fill(self.settings.bg_color)

            #Waiting for a key or mouse button to be pressed.
            pygame.display.flip()

if __name__ == '__main__':
    #Creation of a copy of the game and its launch.
    ai = AlienInvasion()
    ai.run_game()
