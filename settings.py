class Settings:
    """a class to store all settings for alian invasion"""

    def __init__(self):
        """initialize the games settings"""
        #screen settings
        self.screen_width = 1200
        self.screen_hight = 620
        self.bg_color = (230, 230, 230)
        #ship settings
        self.ship_speed = 1.5