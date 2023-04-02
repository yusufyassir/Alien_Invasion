import pygame

class Ship:
    """a class to manage the ship"""

    def __init__(self, ai_game):
        """initiliaze the ship and set satrating position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #load the ship and its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #start each ne ship at the bottom corer of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def bltime(self):
        """"draw ship in its current location."""
        self.screen.blit(self.image, self.rect)