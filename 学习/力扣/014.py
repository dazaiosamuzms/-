#! \Local\Programs\Python\Python36\python.exe
# -*- coding: utf-8 -*-
__author__ = '98221254@qq.com'
'''
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。

示例
输入: ["flower","flow","flight"]
输出: "fl"
'''


class Solution:
    # 水平扫描法
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        l = len(strs)
        if l == 0:
            return ''
        elif l == 1:
            return strs[0]
        rst = len(strs[0])
        for i in range(l-1):
            word = 0
            st1, st2 = strs[i], strs[i+1]
            for i in range(min(len(st1), len(st2))):
                if st1[i] == st2[i]:
                    word += 1
                else:
                    break
            if word < rst:
                rst = word
        return strs[0][:rst]

    # 分治法 （未完成）
    def longestCommonPrefix2(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        def fun1(strs, l, r):
            if not strs:
                return ''
            if l == r:
                return strs[l]
            else:
                mid = (l+r)//2
                left = fun1(strs, l, mid)
                right = fun1(strs, mid+1, r)
                return fun2(left, right)

        def fun2(left, right):
            len_min = min(len(left), len(right))
            for i in range(len_min):
                if left[i] != right[i]:
                    return left[:i]
            return left[0:min]
        for st in strs:
            fun1(st, 1, 2)


if __name__ == '__main__':
    s = Solution()
    lis = ['abc','abcd','abcde']
    rst = s.longestCommonPrefix2(lis)
    print(rst)
