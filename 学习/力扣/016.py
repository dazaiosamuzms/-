#! \Local\Programs\Python\Python36\python.exe
# -*- coding: utf-8 -*-
__author__ = '98221254@qq.com'

'''
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，
使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
'''


class Solution:
    # 复杂度为N**3
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = len(nums)
        nums = sorted(nums)
        mi = nums[0] + nums[1] + nums[-1]
        rst = target
        for i in range(l-1):
            if mi == target:
                return rst
            t = nums[i]
            for j in range(i+1, l-1):
                for k in range(l-1, j, -1):
                    if abs(nums[j] + nums[k] + t - target) < abs(mi - target):
                        mi = nums[j] + nums[k] + t
                    if mi == target:
                        return rst
        return mi

    # 和上个方法思路相似，但解题侧重在找最接近的值，双指针可以简化循环，复杂度为N**2
    def threeSumClosest2(self, nums, target):
        nums.sort()
        res = None
        i = 0
        for i in range(len(nums)):
            if i == 0 or nums[i] > nums[i-1]:
                l = i+1
                r = len(nums)-1
                while l < r:
                    s = nums[i] + nums[l] + nums[r]
                    res = s if res == None or abs(
                        s-target) < abs(res-target) else res
                    if s == target:
                        return s
                    # 因为进行过排序，如果
                    elif s > target:
                        r -= 1
                    else:
                        l += 1
        return res


if __name__ == '__main__':
    s = Solution()
    n = [-1, 2, 1, -4]
    rst = s.threeSumClosest2(n, 2)
    print(rst)
