import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienIvasion:
    """overall class to manage game assets and behaviour"""
    def __init__(self):
        """initialize the game, and create game resources"""
        pygame.init()
        self.settings = Settings()
        #to adjust to full screen mode if wanted
        #self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        #self.settings.screen_width = self.screen.get_rect().width
        #self.settings.screen_height = self.screen.get_rect().height
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()
        
    def run_game(self):
        """start the game main loop"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
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
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """responds to key presses"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):

        """responds to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _create_fleet(self):
        """create fleet of aliens"""
        #make alian and find number of aliena in a row
        #space between each alien is equal t 1 alien wdth
        alien = Alien(self)
        alien_width = alien.rect.width
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // ( 2 * alien_width)

        # create the first row of aliens
        for alien_number in range(number_aliens_x):
           self._create_alien(alien_number)

    def _create_alien(self, alien_number):
        """create an alien and place it in row"""
        alien = Alien(self)
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        self.aliens.add(alien)

    def _update_sceen(self):
        """update images on screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.bltime()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        #make most recet screen drawn
        pygame.display.flip()

    def _fire_bullet(self):
        """create new bullet and add it to bullet group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        """update position of bullets and ge rid of old"""
        #update bullet positions.
        self.bullets.update()
        #get rid of disapperd bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

if __name__ == '__main__':
    #make game instance and run ngame
    ai = AlienIvasion()
    ai.run_game()