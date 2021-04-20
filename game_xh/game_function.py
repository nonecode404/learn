import sys
from time import sleep
import pygame

from game_xh.alien import Alien
from game_xh.bullet import Bullet


def update_screen(screen, ai_settings, ship, bullets, aliens, play_button, stats, sb):
    screen.fill(ai_settings.bg_color)

    # 分数显示
    sb.show_score()
    ship.blitme()
    aliens.draw(screen)

    # 绘制子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # 绘制play按钮
    if stats.game_active == False:
        play_button.draw_button()

    pygame.display.flip()


# 更新子弹
def update_bullet(ai_settings, screen, aliens, ship, bullets, stats, sb):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, screen, aliens, ship, bullets, stats, sb)

# 发射子弹
def fire_bullet(bullets, ai_settings, screen, ship):
    if len(bullets) < 3:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

# 检测子弹外星人碰撞
def check_bullet_alien_collisions(ai_settings, screen, aliens, ship, bullets, stats, sb):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True) # 外星人和子弹写反 出现效果不一样

    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points
            sb.prep_score()
        check_high_score(stats, sb)

    if len(aliens) == 0:
        bullets.empty()
        ai_settings.increase_speed()
        stats.level += 1
        sb.prep_level()
        create_fleet(ai_settings, screen, aliens, ship)


def check_high_score(stats, sb):
    '''检测最高分'''
    if stats.score >= stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

# 创建一个外星人
def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    # 宽间隔为一个外星人
    alien_width = alien.rect.width

    #alien.rect.x = alien.rect.width + alien_number * 2 * alien_width
    #使用上一语句，未考虑alien.x变化，会导致外星人移动出错
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x

    # 竖间隔为一个外星人
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


# 创建多行外星人
def create_fleet(ai_settings, screen, aliens, ship):
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height,
                                  alien.rect.height)
    # number_rows =  1
    # number_aliens_x = 1
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number,
                         row_number)


# 一行外星人数目
def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_alens_x = int(available_space_x / (2 * alien_width))
    return number_alens_x


# 容纳几行外星人
def get_number_rows(ai_settings, ship_height, alien_height):
    availabale_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(availabale_space_y / (2 * alien_height))
    return number_rows


# 检测外星人是否碰到边缘
def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break

# 改变外星人方向并下移
def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():

        alien.rect.y += ai_settings.alien_drop_speed_factor
    ai_settings.fleet_direction *= -1


# 更新外星人
def check_ailen_bottom(ai_settings,aliens, screen, ship, bullets, stats, sb):
    for alien in aliens:
        if alien.rect.bottom >= screen.get_rect().bottom:
            ship_hit(ai_settings, screen, aliens, ship, bullets, stats, sb)


def update_aliens(ai_settings, screen, aliens, ship, bullets, stats, sb):

    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # for alien in aliens.sprites():
    #     alien.rect.x -= 1
    #     alien.rect.y += 1

    # 检测外星人与飞船撞击
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, aliens, ship, bullets, stats, sb)

    # 检测是否遗漏外星人
    check_ailen_bottom(ai_settings, aliens, screen, ship, bullets, stats, sb)




# 飞船毁灭
def ship_hit(ai_settings, screen, aliens, ship, bullets, stats, sb):

    stats.ships_left -= 1
    # 判断是否有剩余飞船
    if stats.ships_left > 0:
        sb.prep_ships()
        aliens.empty()
        bullets.empty()
        ship.center_ship()

        create_fleet(ai_settings, screen, aliens, ship)
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

# 监听按键
def check_events(ai_settings, screen, aliens, ship, bullets, play_button, stats, sb):
    for event in pygame.event.get():
        # 点x退出游戏
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, ship, bullets, screen)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, ship, aliens, bullets, play_button, mouse_x, mouse_y, stats, sb)


def check_keydown_events(event, ai_settings, ship, bullets, screen):
    '''监听按下按键'''
    if event.key == pygame.K_RIGHT:
        ship.right_moving = True

    if event.key == pygame.K_LEFT:
        ship.left_moving = True

    if event.key == pygame.K_SPACE:
        fire_bullet(bullets, ai_settings, screen, ship)


def check_keyup_events(event, ship):
    '''监听抬起按键'''

    if event.key == pygame.K_RIGHT:
        ship.right_moving = False

    if event.key == pygame.K_LEFT:
        ship.left_moving = False


# 检测playButtong
def check_play_button(ai_settings, screen, ship, aliens, bullets, play_button, mouse_x, mouse_y, stats, sb):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active :

        ai_settings.initialize_dynamic_settings()
        stats.reset_stats()

        sb.prep_level()
        sb.prep_score()
        sb.prep_ships()
        sb.prep_high_score()

        aliens.empty()
        bullets.empty()

        create_fleet(ai_settings, screen, aliens, ship)
        ship.center_ship()

        pygame.mouse.set_visible(False)
        stats.game_active = True