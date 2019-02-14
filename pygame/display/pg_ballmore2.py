# 升级版，可以控制的小球

import pygame
import sys

pygame.init()
size = width, height = 600, 400
BLACK = 0, 0, 0
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pygame小球")
# 导入小球的图片
ball = pygame.image.load(r"C:\Users\Administrator\Desktop\PYG02-ball.gif")
ballrect = ball.get_rect()  # 以小球面积生成最小外切长方形，矩形
speed = [1,1]  # 指每帧移动时移动的像素
fps = 300  # 帧数
fclock = pygame.time.Clock()  # 创建一个Clock对象，用于操作时间

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # 监听按键事件，上下左右分别控制y轴速度,x轴速度的加减
        # KEYDOWN是按键事件，K_LEFT,K_RIGHT,K_UP,K_DOWN 表示上下左右
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed[0] = speed[0] if speed[0] == 0 else (abs(speed[0])-1)*int(speed[0]/abs(speed[0]))
            elif event.key == pygame.K_RIGHT:
                speed[0] = speed[0] + 1 if speed[0] > 0 else speed[0] -1
            elif event.key == pygame.K_UP:
                speed[1] = speed[1] + 1 if speed[1] > 0 else speed[1] -1
            elif event.key == pygame.K_DOWN:
                speed[1] = speed[1] if speed[1] == 0 else (abs(speed[1])-1)*int(speed[1]/abs(speed[1]))

    # 给矩形一个运动，参数是x,y轴的速度，其中参数不能小于1
    ballrect = ballrect.move(speed[0], speed[1])
    if ballrect.left < 0 or ballrect.right > width:  # 判断矩形到达边缘的状态
        speed[0] = -speed[0]  # 碰撞后矩形的速度取反
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(BLACK)  # 设置壁纸的背景颜色
    screen.blit(ball, ballrect)  # blit可以将小球的图像绘制在ballrect的矩形上
    pygame.display.update()
    fclock.tick(fps)  # tick用于控制帧速，即窗口刷新速度