#! \Local\Programs\Python\Python36\python.exe
# -*- coding: utf-8 -*-
__author__ = '98221254@qq.com'

import logging
import getpass
import sys
import os


# 用于自定义log消息设置
class MyLog:
    def __init__(self):
        user = getpass.getuser()
        self.logger = logging.getLogger(user)
        self.logger.setLevel(logging.DEBUG)
        logFile = './' + os.path.split(sys.argv[0])[-1][0:-3] + '.log'  # 在当前目录下以执行该方法的文件名+.log 创建文件
        # %(name)-10s: 表示显示用户名，-表示左对齐，10s表示长度为10字节
        formatter = logging.Formatter('%(asctime)-12s %(levelname)-8s %(name)-10s %(message)-12s')

        logHand = logging.FileHandler(logFile)
        logHand.setFormatter(formatter)  # 设置保存/显示位置
        logHand.setLevel(logging.ERROR)

        logHandSt = logging.StreamHandler()
        logHandSt.setFormatter(formatter)

        self.logger.addHandler(logHand)    # 保存到文件中
        self.logger.addHandler(logHandSt)  # 打印到shell

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warn(self, msg):
        self.logger.warn(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)


if __name__ == '__main__':
    mylog = MyLog()
    mylog.debug('debug')
    mylog.info('info')
    mylog.warn('warn')
    mylog.error('error')
    mylog.critical('critical')

