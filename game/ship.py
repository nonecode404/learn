import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, ai_setting, screen):
        super(Ship, self).__init__()
        self.screen = screen

        self.image = pygame.image.load('../game_xh/images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moveing_right = False
        self.moveing_left = False

        self.ai_setting = ai_setting
        self.center = float(self.rect.centerx)

    def update(self):
        if self.moveing_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_setting.ship_speed_factor

        if self.moveing_left and self.rect.left > self.screen_rect.left:
            self.center -= self.ai_setting.ship_speed_factor

        self.rect.centerx = self.center

    def bltime(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx