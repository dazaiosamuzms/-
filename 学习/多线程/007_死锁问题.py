#! \Local\Programs\Python\Python36\python.exe
# -*- coding: utf-8 -*-
__author__ = '98221254@qq.com'
'''
死锁问题：即在多个线程同时使用一把锁时, 互相等待释放锁, 造成阻塞
  - 解决方案(1)：设置等待时间(一定时间内无法获得锁)  timeout参数
  - 解决方案(2)：限制一个资源允许的几个线程同时使用  
'''
import threading
import time

lock1 = threading.Lock()
lock2 = threading.Lock()


def fun1():
    print('fun1 start......')
    lock1.acquire()
    print('fun1 申请 lock1')
    time.sleep(2)
    print('fun1 等待 lock2')
    lock2.acquire()
    print('fun1 申请 lock2')
    lock2.release()
    print('fun1 释放 lock2')
    lock1.release()
    print('fun1 释放 lock1')
    print('fun1 done......')


def fun2():
    print('fun2 start......')
    lock2.acquire()
    print('fun2 申请 lock2')
    time.sleep(4)
    print('fun2 等待 lock1')
    lock1.acquire()
    print('fun2 申请 lock1')
    lock1.release()
    print('fun2 释放 lock1')
    lock2.release()
    print('fun2 释放 lock2')
    print('fun2 done......')


def main():
    print('main() start......')
    t1 = threading.Thread(target=fun1, args=())
    t2 = threading.Thread(target=fun2, args=())
    t1.start()
    t2.start()
    t1.join()
    t2.join()


# 解决死锁问题的改善方案(1)
def fun1_2():
    print('fun1 start......')
    lock1.acquire(timeout=4)  # 可以设置超时时间
    print('fun1 申请 lock1')
    time.sleep(2)
    print('fun1 等待 lock2')
    rst = lock2.acquire(timeout=2)
    if rst:  # 若获取锁2超时, 则释放锁1
        print('fun1 申请 lock2')
        lock2.release()
        print('fun1 释放 lock2')
    else:
        print('fun1 无法申请 lock2')
    lock1.release()
    print('fun1 释放 lock1')
    print('fun1 done......')


def main_2():
    print('main() start......')
    t1 = threading.Thread(target=fun1_2, args=())
    t2 = threading.Thread(target=fun2, args=())
    t1.start()
    t2.start()
    t1.join()
    t2.join()


semaphore = threading.Semaphore(3)  # 设置可以同时调同一公共资源的进程数


def func():
    if semaphore.acquire():
        for i in range(2):
            print(threading.current_thread().getName() + ' get semaphore')
        time.sleep(10)
        semaphore.release()
        print(threading.current_thread().getName() + ' release semaphore')


def main_3():
    for i in range(8):
        t1 = threading.Thread(target=func)
        t1.start()


if __name__ == "__main__":
    # main()
    # main_2()
    main_3()  # 得到的结果可以得到, 限制同时调用同一资源的进程数为3,
