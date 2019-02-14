'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
'''


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = {}
        switch = 0

        if len(s) == 0 or len(s) == 1:
            return s

        for i in range(0, len(s)):
            if s[i:i+1] == s[i+1:i+2] or s[i:i+1] == s[i+2:i+3]:
                count = 1
                if s[i:i+1] == s[i+2:i+3] or s[i:i+1] == s[i+1:i+2] and s[i:i+1] == s[i+2:i+3]:
                    i += 1
                    l, r = i - 1, i + 1

                else:
                    l, r = i - 1, i + 2
                while s[l:l + 1] == s[r:r + 1]:
                    l -= 1
                    r += 1
                    count += 1
                dic[count] = i
                i += 1

        max_d = dic and max(dic.keys()) or -1
        if max_d == -1:
            return s[:1]
        index = dic[max_d]
        left = index - max_d + 1
        if left < 0:
            left = 0
        right = index + max_d + 1

        # # 判断是完全对称还是除了中间完全对称
        # if len(s) > 3:
        #     l, r = 0, 0
        #     l_i, r_i = index, index
        #     print(index)
        #     for j in range(max_d - 2):
        #         if s[index] == s[l_i + 1]:
        #             l += 1
        #             l_i += 1
        #         if s[index] == s[r_i - 1]:
        #             r += 1
        #             r_i += 1
        #     if l == r:
        #          switch = 1

        if switch:
           right -= 1
        print(dic, max_d, switch)

        if s[:1] == s[1:2]:
            s1, s1_l = s[:1], 0
            for j in s:
                if s1 == j:
                    s1_l += 1
                else:
                    break
            if s1_l/2 >= max_d:
                print(s1_l)
                return s[:s1_l]
        return s[left:right]


def main():
    s = "baba   ddtattarrattatdd"
    solution = Solution()
    rst = solution.longestPalindrome(s)
    print(rst)


main()