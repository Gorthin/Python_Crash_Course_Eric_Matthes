#! python3

class Settings:
    """The class is designed to store all game settings."""

    def __init__(self):
        """Initializing the game settings."""
        #Setting of screen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (135, 206, 250)

        #Ship
        self.ship_limit = 3

        #Bullet
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 4

        #Alien
        self.fleet_drop_speed = 10

        #Speed game
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initalization settings which change during in game"""
        self.ship_speed = 1.5
        self.bullet_speed = 1.5
        self.alien_speed = 1.0

        self.fleet_direction = 1

        self.alien_points = 50

    def increase_speed(self):
        """Change speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)