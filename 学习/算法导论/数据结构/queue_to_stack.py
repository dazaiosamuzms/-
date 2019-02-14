'''
两个队列实现一个栈
'''


class Stock:
    def __init__(self):
        self.queueA = []
        self.queueB = []

    def push(self, node):
        self.queueA.append(node)

    def pop(self):
        if len(self.queueA) == 0:
            return None
        while len(self.queueA) != 1:
            self.queueB.append(self.queueA.pop(0))
        self.queueA, self.queueB = self.queueB, self.queueA  # 交换是为了下一次的pop
        return self.queueB.pop()
