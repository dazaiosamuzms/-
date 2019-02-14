#! \Local\Programs\Python\Python36\python.exe
# -*- coding: utf-8 -*-
__author__ = '98221254@qq.com'
'''
threading.Thread是新的多线程工具
调用的方法类似_thread.start_new_thread()，但是需要start()来启动
Thread(target=fun, args=(xxx, ..))
Timer(sec, fun, args=None, kwargs=None)

守护线程指生命周期依赖于主线程, 主线程结束, 守护线程也同时结束
  -- 一般用于不重要的线程或者不允许独立运行的方法
  __ 设置方法：在start()之前,设置setDaemon(True)
'''

import time
import threading


def loop1(in1, in2):
    print('start loop1')
    time.sleep(1)
    print('values: ', in1, ' + ', in2)
    print('End loop1')


def loop2():
    print('start loop2')
    time.sleep(1)
    print('end loop2')


def loop3():
    print('start loop3')
    time.sleep(5)
    print('end loop3')


def main():
    print('starting at:', time.ctime())
    t1 = threading.Thread(target=loop1, args=('li', 'liu'))
    t1.start()
    t1.join()  # 新的功能, 等待子进程完成后才继续执行

    t2 = threading.Thread(target=loop2, args=())
    t2.setDaemon(True)  # 设置为守护线程
    t2.start()
    print('all done at:', time.ctime())


# 测试threading的常用方法
def main2():
    print('starting at:', time.ctime())
    t1 = threading.Thread(target=loop1, args=('li', 'liu'))
    t1.setName('THR_1')  # 设置进程名称
    t1.start()
    t2 = threading.Timer(3, loop2)  # 设置为3秒后开启新的子进程
    t2.setName('THR_2')
    t2.start()
    t3 = threading.Thread(target=loop3, args=())
    t3.setName('THR_3')
    t3.start()

    time.sleep(3)
    for thr in threading.enumerate():
        print('正在运行的进程为：{}'.format(thr.getName()))

    print('正在运行的进程数量为：{}'.format(threading.activeCount()))
    print('all done at:', time.ctime())


if __name__ == '__main__':
    # main()
    main2()

