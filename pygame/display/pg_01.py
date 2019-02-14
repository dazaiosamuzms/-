# 这就是pygame最小的游戏格式

import pygame
import sys

# 初始化部分
pygame.init()
screen = pygame.display.set_mode((600, 400))  # 窗口设置
pygame.display.set_caption("Pygame游戏之旅")  # 窗口标题


# 事件处理部分
while True:  # 一个循环内
    for event in pygame.event.get():  # 处理每一个事件
        if event.type == pygame.QUIT:  # 出现退出事件QUIT时，退出操作
            sys.exit()
        pygame.display.update()
