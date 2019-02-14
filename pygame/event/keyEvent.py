import pygame
import sys

# 初始化部分
pygame.init()
screen = pygame.display.set_mode((600, 400))  # 窗口设置
pygame.display.set_caption("Pygame响应事件")  # 窗口标题


# 事件处理部分
while True:  # 一个循环内
    for event in pygame.event.get():  # 处理每一个事件
        if event.type == pygame.QUIT:  # 出现退出事件QUIT时，退出操作
            sys.exit()
        elif event.type == pygame.KEYDOWN:  # 监听按键 释放按键为KEYUP
            if event.unicode == "":  # 有些键没有unicode值
                print("[KEYDOWN]:", "#", event.key, event.mod)
            else:
                print("[KEYDOWN]:",event.unicode, event.key, event.mod)
        elif event.type == pygame.MOUSEMOTION:  # 监听鼠标移动
            # pos为鼠标在窗口的相对位置(像素)，窗口左上角为(0,0)
            # rel表示与相对于上次鼠标移动事件时pos值的运动，缓慢移动时，一般为(0,±1)，或(±1,0)
            # buttons表示鼠标点击状态,(1,0,0)表示点击左键移动,(1,0,1)表示按着左右键移动，(0,1,0)表示按下滚轮移动
            print("[MOUSEBOTTON]:",event.pos, event.rel, event.buttons)
        elif event.type == pygame.MOUSEBUTTONUP:  # 监听鼠标点击事件
            # pos 表示点击位置   button表示鼠标编号 1:左键,2:滑轮,3:右键
            print("[MOUSEBOTTONUP]:", event.pos, event.button)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("[MOUSEBUTTONDOWN]:", event.pos, event.button)

        pygame.display.update()


