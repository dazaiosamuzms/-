#! \Local\Programs\Python\Python36\python.exe
# -*- coding: utf-8 -*-
__author__ = '98221254@qq.com'

'''
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？
找出所有满足条件且不重复的三元组。注意：答案中不可以包含重复的三元组
例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]
满足要求的三元组集合为：[ [-1, 0, 1], [-1, -1, 2] ]
'''


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        lis = [[]]
        nums = sorted(nums)
        l = len(nums)
        for i in range(l):
            for j in range(i+1, l):
                for k in range(j+1, l):
                    if nums[i] + nums[j] + nums[k] == 0:
                        li = [nums[i], nums[j], nums[k]]
                        if l not in lis:
                            lis.append(li)
        lis = lis[1:]
        tup = (tuple(i) for i in lis)
        lis = list(set(tup))
        return lis

if __name__ == '__main__':
    s = Solution()
    n = [-1, 0, 1, 2, -1, -4]
    rst = s.threeSum2(n)
    print(rst)
