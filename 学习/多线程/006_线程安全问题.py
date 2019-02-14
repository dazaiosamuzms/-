#! \Local\Programs\Python\Python36\python.exe
# -*- coding: utf-8 -*-
__author__ = '98221254@qq.com'
'''
线程安全问题：
 - 如果一个资源/变量,在多线程中不加锁也不会造成问题，则为线程安全
 - 不安全变量类型(list, set, dict)   安全变量类型(queue)
 - 使用队列queue来实现线程安全 
'''
import threading
import time
import queue
# 生成队列对象
q = queue.Queue()


class Producer(threading.Thread):
    def run(self):
        global q
        count = 0
        while True:
            if q.qsize() < 100:
                for i in range(10):
                    count = count + 1
                    msg = str(count)
                    q.put(msg)
                    print('生产产品' + msg)
            time.sleep(0.5)


class Consumer(threading.Thread):
    def run(self):
        global q
        while True:
            if q.qsize() > 10:
                for i in range(3):
                    msg = self.name + '消费' + q.get()
                    print(msg)
            time.sleep(1)


def main():
    global q
    for i in range(5):
        q.put('初始产品' + str(i))
    for i in range(2):
        p = Producer()
        p.start()
    for i in range(5):
        c = Consumer()
        c.start()


if __name__ == "__main__":
    main()
