
import pygame
from pygame.sprite import Group

from game_xh.button import Button
from game_xh.game_stats import GameStats
from game_xh.scoreboard import Scoreboard
from game_xh.settings import Setting

from game_xh import game_function as gf
from game_xh.ship import Ship


def run_game():
    pygame.init()
    ai_settings = Setting()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height), depth=200)

    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    pygame.display.set_caption("外星人之战")

    play_button = Button(ai_settings, screen, "play")

    gf.create_fleet(ai_settings, screen, aliens, ship)

    while True:
        gf.update_screen(screen, ai_settings, ship, bullets, aliens, play_button, stats, sb)
        gf.check_events(ai_settings, screen, aliens, ship, bullets, play_button, stats, sb)
        if stats.game_active == True:
            gf.update_bullet(ai_settings, screen, aliens, ship, bullets, stats, sb)
            gf.update_aliens(ai_settings, screen, aliens, ship, bullets, stats, sb)
            ship.update()
run_game()