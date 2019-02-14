#! \Local\Programs\Python\Python36\python.exe
# -*- coding: utf-8 -*-
__author__ = '98221254@qq.com'


class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        I = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900,
        }
        rst = 0

        for i, j in I.items():
            if i in s:
                rst += int(j)
                # 注意：replace()函数不是原地赋值，不改变原来的字符串
                s = s.replace(i, '')
        for st in s:
            if st in roman.keys():
                rst += roman[st]
        return rst


if __name__ == '__main__':
    s = Solution()
    st = 'IX'
    rst = s.romanToInt(st)
    print(rst)

