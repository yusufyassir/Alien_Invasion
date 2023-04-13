import pygame

class Ship:
    """a class to manage the ship"""

    def __init__(self, ai_game):
        """initiliaze the ship and set satrating position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        #load the ship and its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        #start each ne ship at the bottom corer of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        #store decimal value for the ship horizontal position.
        self.x = float(self.rect.x)
        #movement flag
        self.moving_right = False
        self.moving_left = False

    def bltime(self):
        """"draw ship in its current location."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """update the ships position"""
        #update the shp x value, not rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        #update rect object from self.x
        self.rect.x = self.x

    def center_ship(self):
        """center shipon the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)