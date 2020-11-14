#! python3

class GameStats:
    """In-game statistics monitoring in 'Aliens invasion'"""

    def __init__(self, ai_game):
        """Initialization in-game statistic"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        """Initialization in-game statistic, wich can change during game"""
        self.ship_left = self.settings.ship_limit