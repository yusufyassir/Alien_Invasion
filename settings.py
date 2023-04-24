class Settings:
    """a class to store all settings for alian invasion"""

    def __init__(self):
        """initialize the games settings"""
        #screen settings
        self.screen_width = 1200
        self.screen_height = 620
        self.bg_color = (230, 230, 230)
        #ship settings
        self.ship_limit = 3
        #bullet settings
        self.bullet_width = 20
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        #alien settingd
        self.fleet_drop_speed = 6

        #how quickly the game speeds up
        self.sppedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """initialize settings that change troughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 1.5
        self.alien_speed = .5

        #fleet direction of 1 is right, -1 is left
        self.fleet_direction = 1

        
