#! \Local\Programs\Python\Python36\python.exe
# -*- coding: utf-8 -*-
__author__ = '98221254@qq.com'
'''
函数预期的结果为开始和结束都为0, 但结果有出入
使用多线程同时执行2个函数时, 由于进行的不是原子操作,
在执行一个函数时, 另一个函数将公共参数改变了

python中常用解决方法为设置--锁
  --设置锁:  lock = threading.Lock()
  --上锁:    lock.acquire()
  --解锁:    lock.release()
  --注意点： 上锁的位置(在调用公共参数的代码前后) 
'''
import threading


sum = 0
loopSum = 1000000


def myAdd():
    global sum, loopSum
    for i in range(1, loopSum):
        sum += 1


def myMinu():
    global sum, loopSum
    for i in range(1, loopSum):
        sum -= 1


# 结果与预期不一致, 是一个(-1000000~1000000)之间的数字
def main():
    print('starting ...{}'.format(sum))
    t1 = threading.Thread(target=myAdd, args=())
    t2 = threading.Thread(target=myMinu, args=())
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('done...{}'.format(sum))


# 建立锁的对象
lock = threading.Lock()


def myAdd2():
    global sum, loopSum
    for i in range(1, loopSum):
        lock.acquire()  # 申请一把锁, 上锁
        sum += 1        # 在操作共享资源的代码进行锁的操作
        lock.release()  # 释放锁


def myMinu2():
    global sum, loopSum
    for i in range(1, loopSum):
        lock.acquire()  # 申请一把锁, 上锁
        sum -= 1
        lock.release()  # 释放锁


#  结果与预期一致, 结束为0
def main2():
    print('starting ...{}'.format(sum))
    t1 = threading.Thread(target=myAdd2, args=())
    t2 = threading.Thread(target=myMinu2, args=())
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('done...{}'.format(sum))


if __name__ == '__main__':
    # main()
    main2()



