#! python3

import pygame

class Ship():
    """A class intended for the management of a spacecraft"""

    def __init__(self, ai_game):
        """Spaceship initialization and its initial position."""

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #Load a spaceship image and retrieve its rectangle.
        self.image = pygame.image.load('images/ship2.bmp')
        self.rect = self.image.get_rect()

        #Each new ship appears in the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Displaying a spaceship in its current position."""
        self.screen.blit(self.image, self.rect)