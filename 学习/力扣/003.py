'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
'''


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lis = []
        for i in s:
            lis.append(i)
        lis = list(set(lis))
        return len(lis)

    def lengthOfLongestSubstring_b(self, s):
        test = ''
        num = 0
        for i in s:
            if i not in test:
                test += i
                num += 1
        return num


def main():
    s = 'pwwkew'
    solution = Solution()
    rst = solution.lengthOfLongestSubstring_b(s)
    print(rst)


main()