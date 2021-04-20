import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, ai_setting, screen):
        super(Ship, self).__init__()
        self.screen = screen

        # 在suface.draw方法中 image为特定属性
        self.image = pygame.image.load('./images/ship.bmp')
        self.ai_settings = ai_setting

        self.screen_rect = self.screen.get_rect()
        self.rect = self.image.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        # 左右运动状态
        self.left_moving = False
        self.right_moving = False

    def update(self):
        # ship移动
        if self.left_moving == True and self.rect.left > self.screen_rect.left :
            self.center -= self.ai_settings.ship_speed_factor

        if self.right_moving == True and self.rect.right < self.screen_rect.right :
            self.center += self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx