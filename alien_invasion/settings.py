#! python3

class Settings:
    """The class is designed to store all game settings."""

    def __init__(self):
        """Initializing the game settings."""
        #Setting of screen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (135, 206, 250)
        self.ship_speed = 1.5