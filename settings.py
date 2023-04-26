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
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (230, 60, 60)
        self.bullets_allowed = 3
        #alien settingd
        self.fleet_drop_speed = 10

        #how quickly the game speeds up
        self.sppedup_scale = 1.1

        #how quickly the aliens point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """initialize settings that change troughout the game."""
        self.ship_speed = 2
        self.bullet_speed = 2
        self.alien_speed = .5

        #fleet direction of 1 is right, -1 is left
        self.fleet_direction = 1

        #scoring
        self.alien_points = 50
    
    def increase_speed(self):
        """increase  speed settings"""
        self.ship_speed *= self.sppedup_scale
        self.bullet_speed *= self.sppedup_scale
        self.alien_speed *= self.sppedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        
