#! \Local\Programs\Python\Python36\python.exe
# -*- coding: utf-8 -*-
__author__ = '98221254@qq.com'

'''
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
2:abc; 3:def; 4:ghi; 5:jkl; 6:mno; 7:pqrs; 8:tuv; 9:wxyz; 
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
输入："23"    
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
'''


class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        lis = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        lis_2 = []

        for digit in digits:
            index = int(digit) - 2
            lis_2.append(lis[index])
        print(lis)
        print(lis_2)
        rst = []
        l = 0
        for i in range(len(lis_2)):
            for j in range(len(lis_2[i])):
                rst.append(lis_2[i][j])
                # rst[l] += [i]
                l += 1

    def c

        print(rst)


if __name__ == '__main__':
    s = Solution()
    d = '23'
    s.letterCombinations(d)