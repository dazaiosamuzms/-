# 自定义事件

import pygame, sys

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Pygame事件处理")
fps = 1
fclock = pygame.time.Clock()
num = 1

while True:
    # 建立事件对象
    uevent = pygame.event.Event(pygame.KEYDOWN,{"unicode":123,"key":pygame.K_SPACE,"mod":pygame.KMOD_ALT})
    pygame.event.post(uevent)  # 提交事件
    num = num + 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.unicode == "":
                print("[KEYDOWN {}]:".format(num), "#", event.key, event.mod)
            else:
                print("[KEYDOWN {}]:".format(num), event.unicode, event.key, event.mod)