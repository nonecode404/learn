class Setting():
    def __init__(self):
        self.screen_height = 800
        self.screen_width = 1200
        self.bg_color = (230, 230, 230)

        #子弹
        self.bullet_height = 15
        self.bullet_width = 3
        self.bullet_color = 60, 60, 60

        # 外星人设置


        # 飞船设置
        self.ship_limit = 3

        # 速度权重
        self.speedip_scale = 1.1

        # 分数权重
        self.score_scale = 1.5

    def increase_speed(self):
        self.alien_drop_speed_factor *= self.speedip_scale
        self.bullet_speed_factor *= self.speedip_scale
        self.ship_speed_factor *= self.speedip_scale
        self.alien_points = int(self.alien_points * self.score_scale)

    def initialize_dynamic_settings(self):
        self.alien_drop_speed_factor = 15
        self.ship_speed_factor = 1.5
        self.alien_speed_factor = 1
        self.bullet_speed_factor = 3
        self.fleet_direction = 1
        self.alien_points = 50