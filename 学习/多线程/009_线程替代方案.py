#! \Local\Programs\Python\Python36\python.exe
# -*- coding: utf-8 -*-
__author__ = '98221254@qq.com'
'''
线程代替方案 - 进程(相互独立执行)
    - subprocess: 跳过线程, 使用进程; 支持python2.4以后版本
    - multiprocessing: 使用threading接口派生子进程, 允许多核或多CPU派生进程; Python2.6后版本
    - concurrent.futures: 异步执行模块, 任务级别操作; python3.2后版本

使用进程的优势
    - 每个进程互相独立不影响主程序的稳定性,通过增加CPU就可以容易扩充性能;可以尽量减少线程加锁/解锁的影响,极大提高性能,
      虽然就算是线程运行的模块算法效率低, 每个子进程都有2GB地址空间和相关资源，总体能够达到的性能上限非常大。
    
最严重的问题: 进程间通讯 
    - 原因: 进程之间独立无共享状态; 
'''
import time
import multiprocessing
import os


# 直接使用multiprocessing的方法
def clock(interval):
    while True:
        print('the time is {}'.format(time.ctime()))
        time.sleep(interval)


def main():
    print('start main()')
    # multiprocessing 与threading用法非常接近
    p = multiprocessing.Process(target=clock, args=(5,))
    p.start()
    print('end main()')


# 使用派生类实现multiprocessing的方法
class ClockProcess(multiprocessing.Process):
    def __init__(self, interval):
        super().__init__()
        self.interval = interval

    def run(self):
        print('the time is {}'.format(time.ctime()), end='\n\n')
        time.sleep(self.interval)
        process_info()  # 主进程为'__mp_main__'


def main2():
    print('start main()')
    p = ClockProcess(3)
    p.start()
    print('end main()')


def process_info():  # 不同函数下的主子进程不同
    print('module name', __name__)
    print('parent process id:', os.getppid())  # 获取主进程id
    print('self process id:', os.getpid())     # 获取子进程id


if __name__ == "__main__":
    # main()
    main2()
    process_info()  # 主进程为'__main__'

