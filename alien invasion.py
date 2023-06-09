import sys
from time import sleep
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from music import Music

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

        #create an instance to score game statistics, 
        #   and create a scoreboard.
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        #make play button
        self.play_button = Button(self, "play")

        #make music
        self.music = Music(self)


        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()
        
    def run_game(self):
        """start the game main loop"""
        while True:
            self._check_events()
            
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()

         
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

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
        elif event.key == pygame.K_p:
            self._start_game()

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
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // ( 2 * alien_width)

        #etermine the number of rows of aliena that fit on screen
        ship_hight = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                                    (3 * alien_height) - ship_hight)
        number_rows = available_space_y // (2 * alien_height)

        # create the first row of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """create an alien and place it in row"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """respond appropriatly if any aliens have reached an edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
        
    def _change_fleet_direction(self):
        """drop the entire fleet and change direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        """update images on screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.bltime()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        #draw the score information
        self.sb.show_score()

        #draw the play button if the game is inactive
        if not self.stats.game_active:
            self.play_button.draw_button()
            #pause music
            self.music.pause_bg()
        #make most recet screen drawn
        pygame.display.flip()

    def _fire_bullet(self):
        """create new bullet and add it to bullet group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            self.music.play_bl()
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
        
        self._check_bullet_alien_collisions()
       
    def _check_bullet_alien_collisions(self):
        """respond to bullet alien collision"""
        #remove bullets and alien s that have collided
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.aliens, True, True)
        
        if collisions:
            self.music.play_ex()
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
        if not self.aliens:
            #destroy remaining bullets and crete new fleet
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            #increase level.
            self.stats.level += 1
            self.sb.prep_level()

    def _ship_hit(self):
        """respond to the ship being ht by an alien"""
        if self.stats.ships_left > 0:
            #decrement ships left and update scoreboard
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            #get rid of any remaining bullets and aliens
            self.aliens.empty()
            self.bullets.empty()

            #create ne fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            #pause 
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_play_button(self, mouse_pos):
        """start new game when the player clicks play"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self._start_game()

    def _start_game(self):
        self.music.play_bg()
        """resets the game"""
        #reset g ame statistics
        self.settings.initialize_dynamic_settings()
        self.stats.reset_stats()
        self.stats.game_active = True
        self.sb.prep_score()
        self.sb.prep_level()
        self.sb.prep_ships()
                    
        #git rid of remainig aliens and bulets.
        self.aliens.empty()
        self.aliens.empty()

        #creat a new fleet aand center the ship
        self._create_fleet()
        self.ship.center_ship()

        #hide the mouse cursor.
        pygame.mouse.set_visible(False)

    def _check_aliens_bottom(self):
        """check if any alien sreached bottom of the screen"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                #treat the same as if ship is hi
                self._ship_hit()
                break
                
    def _update_aliens(self):
        """check if the fleet is at an edge 
            then ipdate the position of all aliens in the fleet"""
        self._check_fleet_edges()
        self.aliens.update()

        #look for alien ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        
        #look for alien hitting the bottom of the screen
        self._check_aliens_bottom()

if __name__ == '__main__':
    #make game instance and run ngame
    ai = AlienIvasion()
    ai.run_game()