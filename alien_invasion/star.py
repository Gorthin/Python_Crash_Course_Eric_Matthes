#! python3

import pygame
from pygame.sprite import Sprite
from random import randint

class Star(Sprite):
    """A class representing the single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialization alien and definition his starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #Reading the image and defining its rect attribute.
        self.image = pygame.image.load('images/star.bmp')
        self.rect = self.image.get_rect()

        #Putting new alien near the top left corner.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Storing the exact horizontal foreign position
        self.x = float(self.rect.x)

    def update(self):
        """Move the alien to the right"""
        #self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        #self.rect.x = self.x

