#! \Local\Programs\Python\Python36\python.exe
# -*- coding: utf-8 -*-
__author__ = '98221254@qq.com'

from myLog_010 import MyLog

if __name__ == '__main__':
    ml = MyLog()
    ml.debug('debug message')
    ml.info('info message')
    ml.warn('warn message')
    ml.error('error message')
    ml.critical('critical message')
