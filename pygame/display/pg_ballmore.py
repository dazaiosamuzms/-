# 碰撞后反弹的运动的小球

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
speed = [1,1]
fps = 300  # 帧数
fclock = pygame.time.Clock()  # 创建一个Clock对象，用于操作时间

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
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
