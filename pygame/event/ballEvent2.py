# 升级版3，减速效果，按照点击鼠标后移动速度来

import pygame
import sys


pygame.init()
# 导入图标
icon = pygame.image.load(r"C:\Users\Administrator\Desktop\dota.png")
pygame.display.set_icon(icon)
display_info = pygame.display.Info()  # 因为还没有生成游戏窗口，监听到的为系统的屏幕尺寸
size = width, height = int(display_info.current_w/2), int(display_info.current_h/2)
BLACK = 0, 0, 0
# set_mode有2个参数(r=(0,0),flags=0),r是游戏屏幕分辨率，flags是显示类型,可以用|来组合多类型
# flags可选参数：pygame.RESIZABLE(窗口可调),pygame.NOFRAME(无边界),pygame.FULLSCREEN(全屏)
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
pygame.display.set_caption("Pygame小球")
# 导入小球的图片
ball = pygame.image.load(r"C:\Users\Administrator\Desktop\PYG02-ball.gif")
ballrect = ball.get_rect()  # 以小球面积生成最小外切长方形，矩形
speed = [1,1]  # 指每帧移动时移动的像素,第一项为x坐标，第二项为y坐标
fps = 300  # 帧数
fclock = pygame.time.Clock()  # 创建一个Clock对象，用于操作时间
still = False  # 设置停止
slow = 0.999

while True:  # 每一帧移动一次
    for event in pygame.event.get():  # event.get() 可以获得event队列
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
            elif event.key == pygame.K_ESCAPE:  # 添加ECS退出操作
                sys.exit()

        elif event.type == pygame.VIDEORESIZE:  # 当监听到屏幕尺寸改变时，会接受为VIDEORESIZE事件
            # 并且返回event.size元组参数，（新屏幕宽度，新屏幕高度）
            size = width, height = event.size[0], event.size[1]  # 重新赋值，下次while循环改变
            screen = pygame.display.set_mode(size, pygame.RESIZABLE)  # 重绘窗口


        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                still = True

        elif event.type == pygame.MOUSEBUTTONUP:
            still = False
            if event.button == 1:
                # 将小球移动到鼠标位置,就是在小球原来位置移动(鼠标-小球)坐标的距离
                ballrect = ballrect.move(event.pos[0] - ballrect.left, event.pos[1] - ballrect.top)

        elif event.type == pygame.MOUSEMOTION:  # 即点击左键移动时
            if event.buttons[0] == 1:
                speed[0] = event.rel[0] / (abs(speed[0]) + 1) * 1.5
                speed[1] = event.rel[1] / (abs(speed[1]) + 1) * 1.5
                ballrect = ballrect.move(event.pos[0] - ballrect.left, event.pos[1] - ballrect.top)

    # 窗体在活跃时运动，最小化时不运动; 且在参数still为False时移动;
    if pygame.display.get_active() and not still:
        # 给矩形一个运动，参数是x,y轴的移动的像素，其中参数不能小于1
        ballrect = ballrect.move(speed[0], speed[1])

    if ballrect.left < 0 or ballrect.right > width:  # 判断矩形到达边缘的状态
        speed[0] = -speed[0]  # 碰撞后矩形的速度取反
        if ballrect.right > width and speed[0] > 0:
            speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
        if ballrect.bottom > height and speed[1] > 0:
            speed[1] = - speed[1]
    # 防止小球在窗口外部无线循环，禁止小球停止运动
    if abs(speed[0]) < 1 and abs(speed[1]) < 1:
        speed = [1, 1]
    if abs(speed[0]) < 1 and ballrect.right > width + 1:
        if speed[0] == 0:
            speed[0] = 1
        else:
            speed[0] = speed[0]/abs(speed[0])
    if abs(speed[1]) < 1 and ballrect.bottom > height + 1:
        if speed[1] == 0:
            speed[1] = 1
        else:
            speed[1] = speed[1]/abs(speed[1])
    # 减速
    if abs(speed[0]) > 1/slow:
        speed[0] = abs(speed[0]) * slow * speed[0]/abs(speed[0])
    if abs(speed[1]) > 1/slow:
        speed[1] = abs(speed[1]) * slow * speed[1]/abs(speed[1])

    screen.fill(BLACK)  # 设置壁纸的背景颜色
    screen.blit(ball, ballrect)  # blit可以将小球的图像绘制在ballrect的矩形上
    pygame.display.update()
    fclock.tick(fps)  # tick用于控制帧速，即窗口刷新速度
