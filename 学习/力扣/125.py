#! \Local\Programs\Python\Python36\python.exe
# -*- coding: utf-8 -*-
__author__ = '98221254@qq.com'


class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = 'zxcvbnmasdfghjklqwertyuiopZXCVB' \
             'NMASDFGHJKLQWERTYUIOP1234567890'
        rst = ''
        if s == '':
            return True
        for i in s:
            if i in st:
                rst += i
        rst = rst.lower()
        for i in range(len(rst)//2):
            if rst[i] != rst[len(rst)-i-1]:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    st = '/123b, b32-1'
    rst = s.isPalindrome(st)
    print(rst)