#! \Local\Programs\Python\Python36\python.exe
# -*- coding: utf-8 -*-
__author__ = '98221254@qq.com'
'''
继承Thread的类实现多线程
    -- 作用为简化多次调用，模块化执行
    -- 注意点
        1. 必须继承自threading.Thread,且重写__init__()方法
        2. 必须用一个run的方法, 等同于Thread()中的target参数
'''
import threading
import time


class MyThread(threading.Thread):
    def __init__(self, arg):
        super(MyThread, self).__init__()
        self.arg = arg

    def run(self):
        time.sleep(2)
        print('the args for this class is {}'.format(self.arg))


for i in range(5):
    t = MyThread(i)
    t.start()
    t.join()

print("main thread is done")
