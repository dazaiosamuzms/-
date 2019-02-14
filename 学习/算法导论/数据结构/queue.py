'''
关于队列，collection模块已经提供了高效的deque对象
from collections import deque
'''


# 自定义队列
class Queue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return self.queue == []

    def enqueue(self, x):
        self.queue.append(x)

    def dequeue(self):
        if self.queue:
            a = self.queue[0]
            self.queue.remove(a)
            return a
        else:
            raise IndexError("队列为空，无法继续出队")

    def size(self):
        return len(self.queue)


# collections模块
from collections import deque
queue = deque(['a', 'b', 'c'])