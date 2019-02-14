#! \Local\Programs\Python\Python36\python.exe
# -*- coding: utf-8 -*-
__author__ = '98221254@qq.com'
'''
实际工作中调用多线程的常用写法
'''
import threading
from time import sleep, ctime


class ThreadFunc:

    def __init__(self, name):
        self.name = name

    def loop(self, nloop, sec):
        '''
        :param nloop: loop函数的名称
        :param sec: 系统休眠时间
        :return:
        '''
        print('start loop', nloop, 'at ', ctime())
        sleep(sec)
        print('done loop', nloop, 'at ', ctime())


def main():
    print('start main at ', ctime())
    # 公司一般习惯这种写法
    t1 = threading.Thread(target=ThreadFunc('loop').loop, args=('LOOP1', 2))
    t1.start()
    t1.join()
    print('all done at: ', ctime())


if __name__ == '__main__':
    main()
