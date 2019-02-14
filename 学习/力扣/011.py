#! \Local\Programs\Python\Python36\python.exe
# -*- coding: utf-8 -*-
__author__ = '98221254@qq.com'

'''
给定n个非负整数a1，a2，...，an，每个数代表坐标中的一个点(i, ai) 。在坐标内画n条垂直线，垂直线
i的两个端点分别为(i, ai)和(i, 0)。找出其中的两条线，使得它们与x轴共同构成的容器可以容纳最多的水。
说明：你不能倾斜容器，且n的值至少为2。

垂直线代表输入数组[1, 8, 6, 2, 5, 4, 8, 3, 7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为
49。

输入: [1, 8, 6, 2, 5, 4, 8, 3, 7]
输出: 49
'''

'''
题目分析，即找出2个点(x,ix),(y,iy)，他们之间的(y-x)*min(ix,iy)的值最大
解题思路1：
暴力解法，遍历所有可能
'''


class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        rst = 0
        lis = list(enumerate(height))
        for x in lis:
            for y in lis[x[0]:]:
                k = y[0]-x[0]
                area = k * min(x[1], y[1])
                #print(k, area)
                if area > rst:
                    rst = area
        return rst


if __name__ == '__main__':
    s = Solution()
    rst = s.maxArea([1,8,6,2,5,4,8,3,7])
    print(rst)
