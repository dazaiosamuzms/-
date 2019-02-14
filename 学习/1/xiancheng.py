# 由于windows没有fork()，只能用multiprocessing模块代替
# import os
#
# print('Process (%s) start...' % os.getpid())
# pid = os.fork()
# if pid==0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))


'''
multiprocessing模块就是跨平台版本的多进程模块。
'''


from multiprocessing import Process
import os


# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     # 创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动
#     p = Process(target=run_proc, args=('test',))
#     print('Process will start.')
#     p.start()
#     # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
#     p.join()
#     print('Process end.')


'''
如果要启动大量的子进程，可以用进程池的方式批量创建子进程：
'''

from multiprocessing import Pool
import os, time, random


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool()
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
