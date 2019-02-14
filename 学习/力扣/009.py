class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        rst = ''
        bo = False
        if x < 0:
            return bo
        else:
            for i in reversed(str(x)):
               rst += i
            if str(x) == rst:
                bo = True
            return bo


if __name__ == '__main__':
    s = Solution()
    rst = s.isPalindrome(121)
    print(rst)
