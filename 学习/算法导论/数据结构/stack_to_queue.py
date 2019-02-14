'''
两个栈实现列表
'''


class Queue:
    def __init__(self):
        self.stockA = []
        self.stockB = []

    def push(self, node):
        self.stockA.append(node)

    def pop(self):
        if not self.stockB:
            if not self.stockA:
                return None
            else:
                for i in range(len(self.stockA)):
                    self.stockB.append(self.stockA.pop())
        rst = self.stockB.pop()
        return rst


def main():
    queue = Queue()
    for i in range(10):
        queue.push(i)
    print(queue.stockA)
    queue.pop()
    print(queue.stockB)

main()
