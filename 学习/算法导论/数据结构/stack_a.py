'''
栈的先进后出特点，可以处理对称问题
例如：1. 检查程序中成对的符号
     2. 最长回文子串
     3. 十进制转换二进制
'''

# from .stack import Stack


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


# 检查程序中成对的符号
def checkSimple(s):
    def match(i, j):
        start = '([{'
        end = ')]}'
        return end.index(i) == start.index(j)

    def checker(string):
        stack = Stack()
        balance = True
        for i in string:
            if i in '([{':
                stack.push(i)
            elif i in ')]}':
                if stack.isEmpty():
                    balance = False
                    return balance
                else:
                    j = stack.pop()  # 取出最后压栈的开始括号
                    if not match(i, j):
                        balance = False
                        return balance
        return balance
    return checker(s)


# 十进制转换二进制：把十进制转成二进制一直分解至商数为0。从最底左边数字开始读，之后读右边的数字，从下读到上。
def decimal_to_bin(dec):
    stack = Stack()
    cur = dec
    while cur > 0:
        a = cur % 2
        cur = cur // 2
        stack.push(a)
    binstr = ''
    while not stack.isEmpty():
        binstr += str(stack.pop())
    return binstr


def main():
    # s = '{123()21[123]}'
    # rst = checkSimple(s)
    rst = decimal_to_bin(1245)
    print(rst)

main()