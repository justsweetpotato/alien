#!/usr/bin/env python

import sys
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # 初始化并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(screen)

    # 开始游戏的主循环
    while True:
        # 响应按键和鼠标事件
        gf.check_events(ship)

        # 绘制屏幕
        gf.update_screen(ai_settings, screen, ship)


run_game()
