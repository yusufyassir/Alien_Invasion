import sys
import pygame

from settings import Settings
from ship import Ship

class AlienIvasion:
    """overall class to manage game assets and behaviour"""
    def __init__(self):
        """initialize the game, and create game resources"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_hight))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        
    def run_game(self):
        """start the game main loop"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_sceen()
         

    def _check_events(self):
        """responds to key presse and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            #for moving right
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events

    def _check_keydown_events(self, event):
        """responds to key presses"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """responds to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_sceen(self):
        """update images on screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.bltime()
        #make most recet screen drawn
        pygame.display.flip()


if __name__ == '__main__':
    #make game instance and run ngame
    ai = AlienIvasion()
    ai.run_game()