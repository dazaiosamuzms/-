# 栈的实现（原理是利用数组）


class Stack():
    def __init__(self, n=100):
        self.stack = []
        self.n = n

    def isEmpty(self):
        return self.stack == []

    def isFull(self):
        return self.size() > self.n

    def push(self, item):
        if self.isFull():
            raise IndexError('栈已满，不可继续压栈')
        return self.stack.append(item)

    def pop(self):
        if self.isEmpty():
            raise IndexError('栈为空，不可移除栈顶')
        return self.stack.pop()

    # 返回栈顶
    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)


def main():
    stack = Stack(100)
    for i in range(10):
        stack.push(i)
    stack.pop()
    print(stack.stack)


if __name__ == '__main__':
    main()

