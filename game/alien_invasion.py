import sys
import pygame

from game.button import Button
from game.scoreboard import Scoreboard
from game.settings import Settings
from game.ship import Ship
import game.game_function as gf
from pygame.sprite import Group
from game.game_stats import GameStats



def run_name() :
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption("xu xu")
    ship = Ship(ai_setting, screen)
    bullets = Group()
    aliens = Group()
    stats = GameStats(ai_setting)
    sb = Scoreboard(ai_setting, screen, stats)
    play_button = Button(ai_setting, screen, "play")

    gf.create_fleet(ai_setting, screen, ship, aliens)

    while True:
        gf.check_events(ai_setting, ship, aliens, screen, bullets, stats, sb, play_button)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_setting, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_setting, stats, sb, screen, ship, aliens, bullets)

        gf.update_screen(ai_setting, screen, ship, bullets, aliens, stats, sb, play_button)

run_name()