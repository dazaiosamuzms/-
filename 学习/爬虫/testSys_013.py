#! \Local\Programs\Python\Python36\python.exe
# -*- coding: utf-8 -*-
__author__ = '98221254@qq.com'

import sys


# 用于展示sys
class ShowSysNodule:
    def __init__(self):
        print('sys模块获取程序参数')
        self.getArg()
        print('其次是获取当前系统平台')
        self.getOs()

    def getArg(self):
        print('开始获取参数个数')
        print('当前参数有{}个'.format(len(sys.argv)))
        print('这些参数分别为{}'.format(sys.argv))

    def getOs(self):
        print('sys.platform 返回值对应的平台')
        print('当前的系统为:', sys.platform)


if __name__ == '__main__':
    sm = ShowSysNodule()
