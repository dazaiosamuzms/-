#! \Local\Programs\Python\Python36\python.exe
# -*- coding: utf-8 -*-
__author__ = '98221254@qq.com'

import time
from loggings.myLog_010 import MyLog


class TestTime:
    def __init__(self):
        self.log = MyLog()
        self.testTime()
        self.testLocaltime()

    def testTime(self):
        self.log.info('开始测试time()函数')

    def testLocaltime(self):
        self.log.info('测试localtime()函数')
        print('当前本地时间为', time.localtime())
        print('返回一个struct_time结构元组')


if __name__ == '__main__':
    tt = TestTime()

