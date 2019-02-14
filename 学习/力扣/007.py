'''
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
'''


class Solution:
    # python内置函数利用
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        fuhao = 1
        if x < 0:
            fuhao = -1
            x = -x

        rst = ''
        lis = list((reversed(str(x))))
        for i in lis:
            rst += i
        if int(rst) >= 2 ** 31:
            return 0
        return int(rst) * fuhao

    # 计算方法
    def reverse_b(self, x):
        fuhao = 1
        if x < 0:
            fuhao = -1
            x = -x
        digit = 0
        l = x
        while l//10 != 0:
            l /= 10
            digit += 1
        rst = 0
        for i in range(digit, -1, -1):
            j = digit - i
            rst += x // (10 ** i) * 10 ** j
            x = x % 10 ** i

        return rst * fuhao


def main():
    s = 123465734234563
    solution = Solution()
    rst = solution.reverse_b(s)
    print(rst)


main()