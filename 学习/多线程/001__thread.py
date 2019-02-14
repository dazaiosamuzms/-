#! \Local\Programs\Python\Python36\python.exe
# -*- coding: utf-8 -*-
__author__ = '98221254@qq.com'
'''
_thread.start_new_thread是即将被遗弃的多线程调用方法
其中main为主线程,loop1和loop2为2个子线程
3个线程是独立进行的
'''

from _thread import start_new_thread
import time


def loop1():
    print('start loop1 at:', time.ctime())
    time.sleep(2)
    print('End loop1 at:', time.ctime())


def loop2(in1,in2):
    print('start loop2 at:', time.ctime())
    time.sleep(2)
    print('values: ', in1, ' + ', in2)
    print('End loop2 at:', time.ctime())


def main():
    print('starting at:', time.ctime())
    start_new_thread(loop1, ())
    start_new_thread(loop2, ('li', 'liu'))

    print('all done at:', time.ctime())


if __name__ == '__main__':
    main()
    # 一直等待
    while True:
        time.sleep(1)
