#! \Local\Programs\Python\Python36\python.exe
# -*- coding: utf-8 -*-
__author__ = '98221254@qq.com'

'''
罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。
I      1      V      5
X      10     L      50
C      100    D      500
M      1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。
通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。
数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。

给定一个整数，将其转为罗马数字。输入确保在 1 到 3999 的范围内。
输入: 3    输出: "III"
'''

'''
解法1：以各个位数数字为基准
'''


class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        rst = ''
        x3 = num // 1000
        x2 = num // 100 % 10
        x1 = num // 10 % 10
        x0 = num % 10
        k = 3
        tup = (('I','V','X'), ('X','L','C'), ('C','D','M'), ('M','?','?'))
        for i in [x3, x2, x1, x0]:
            st = tup[k]
            index1, index2 = i % 5, i // 5
            if index1 == 4:
                rst += st[0]
                if index2 > 0:
                    rst += st[2]
                else:
                    rst += st[1]
            else:
                if index2 > 0:
                    rst += st[1]
                else:
                    rst += ''
                rst += st[0] * index1
            k -= 1
        return rst

'''
解法2：列出出数字的可能性，直接赋值
'''


class Solution2:
    def intToRoman(self, num):

        m = [
            ['', 'M', 'MM', 'MMM'],
            ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
            ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
            ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        ]

        d = [1000, 100, 10, 1]

        r = ''

        for k, v in enumerate(d):
            r += m[k][int(num/v)]
            num = num % v

        return r


if __name__ == '__main__':
    s = Solution()
    rst = s.intToRoman(1994)
    print(rst)
