#! python3

import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """A class intended for the management of a spacecraft"""

    def __init__(self, ai_game):
        """Spaceship initialization and its initial position."""
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #Load a spaceship image and retrieve its rectangle.
        self.image = pygame.image.load('images/ship2.bmp')
        self.rect = self.image.get_rect()

        #Each new ship appears in the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        #The ship's horizontal position is stored as a floating point number.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        #Options that indicate the movement of the ship
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship's position based on the option that indicates its movement."""

        #Updating the X coordinate of the ship, not its rectangle
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        #Updating rect based on self.x
        self.rect.x = self.x
        self.rect.y = self.y

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def blitme(self):
        """Displaying a spaceship in its current position."""
        self.screen.blit(self.image, self.rect)