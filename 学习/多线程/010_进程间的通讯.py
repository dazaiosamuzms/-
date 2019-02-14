#! \Local\Programs\Python\Python36\python.exe
# -*- coding: utf-8 -*-
__author__ = '98221254@qq.com'
'''

'''
import time
import multiprocessing


def consumer(input_q):
    print('into consumer: ', time.ctime())
    while True:
        item = input_q.get()
        print('pull ', item, ' out of q')
        input_q.task_done()


def producer(sequence, output_q):
    print('into procuder: ', time.ctime())
    for item in sequence:
        output_q.put(item)
        print('put ', item, ' into q')
    print('produce success!')


def main():
    # JoinableQueue 类似于queue的队列对象, 并且可以返回数据
    q = multiprocessing.JoinableQueue()
    cons_p = multiprocessing.Process(target=consumer, args=(q, ))
    cons_p.daemon = True
    cons_p.start()
    sequence = [1, 2, 3, 4]
    producer(sequence, q)
    q.join()


if __name__ == "__main__":
    main()
