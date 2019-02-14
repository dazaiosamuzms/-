'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''


class Solution:
    # 暴力破解
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lis = []
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                count = nums[i] + nums[j]
                if count == target:
                    lis.append(i)
                    lis.append(j)
                    return lis

    # 先排序， 前后两两相加找值
    def twoSum_b(self, nums, target):
        nums.sort()
        # sorted_id = sorted(range(len(nums)), key=lambda k: nums[k])  # [0, 1, 2, 3]
        sorted_id = [i for i in range(len(nums))]  # [0, 1, 2, 3]
        head = 0
        tail = len(nums) - 1
        sum_result = nums[sorted_id[head]] + nums[sorted_id[tail]]
        while sum_result != target:
            sum_result = nums[sorted_id[head]] + nums[sorted_id[tail]]
            if sum_result > target:
                tail -= 1
            elif sum_result < target:
                head += 1
        return [sorted_id[head], sorted_id[tail]]

    # 用哈希（字典）,值做键，排序做值
    def twoSum_c(self, nums, target):
        hashmap = {}
        for index, num in enumerate(nums):
            # >> > seasons = ['Spring', 'Summer', 'Fall', 'Winter']
            # >> > list(enumerate(seasons, start=1))  # 下标从 1 开始
            # [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
            another_num = target - num
            if another_num in hashmap:
                return [hashmap[another_num], index]
            hashmap[num] = index
        return None


def main():
    nums = [2, 7, 11, 15]
    solution = Solution()
    rst = solution.twoSum_c(nums, 18)
    print(rst)


main()

