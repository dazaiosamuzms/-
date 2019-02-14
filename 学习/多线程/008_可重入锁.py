#! \Local\Programs\Python\Python36\python.exe
# -*- coding: utf-8 -*-
__author__ = '98221254@qq.com'
'''
可重入锁
 - 作用：为了解决递归调用函数或函数多次调用时, 重复申请锁会出现自己产生死锁。
        可重入锁则允许该函数在释放前,多次申请锁。 
 - 方法：threading.RLock()
'''
import threading
import time

num = 0
# lock = threading.Lock()  # 普通锁： 造成死锁
lock = threading.RLock()   # 可重入锁： 可以运行


class MyThread(threading.Thread):
    def run(self):
        global num
        time.sleep(1)
        if lock.acquire(timeout=1):
            num += 1
            msg = self.name + ' set num to ' + str(num)
            print(msg)
            lock.acquire()
            lock.release()
            lock.release()


def main():
    for i in range(5):
        t = MyThread()
        t.start()


if __name__ == '__main__':
    main()
