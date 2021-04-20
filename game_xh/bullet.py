import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, ai_setting, screen, ship):
        super().__init__()
        self.screen = screen

        self.screen_rect = self.screen.get_rect()

        #子弹位置、属性
        self.rect = pygame.Rect(0, 0, ai_setting.bullet_width, ai_setting.bullet_height)
        self.rect.top = ship.rect.top
        self.rect.centerx = ship.center
        self.color = ai_setting.bullet_color

        self.y = float(self.rect.y)
        # 发射速度
        self.speed_factor = ai_setting.bullet_speed_factor

    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y

    # 绘制子弹
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
