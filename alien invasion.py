import sys
import pygame

from settings import Settings

class AlienIvasion:
    """overall class to manage game assets and behaviour"""
    def __init__(self):
        """initialize the game, and create game resources"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_hight))
        pygame.display.set_caption("Alien Invasion")

        #set background color
        self.bg_color = (230,230,230)
    def run_game(self):
        """start the game main loop"""
        while True:
            #watch for keboard and muse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            #redraw screen through each pass of looop
            self.screen.fill(self.settings.bg_color)
            #make most recet screen drawn
            pygame.display.flip()

if __name__ == '__main__':
    #make game instance and run ngame
    ai = AlienIvasion()
    ai.run_game()