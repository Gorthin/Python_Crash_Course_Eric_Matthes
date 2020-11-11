#! python3

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class representing the single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialization alien and definition his starting position"""
        super().__init__()
        self.screen = ai_game.screen

        #Reading the image and defining its rect attribute.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #Putting new alien near the top left corner.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Storing the exact horizontal foreign position
        self.x = float(self.rect.x)