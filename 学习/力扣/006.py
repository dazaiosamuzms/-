'''
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:

L     D     R
E   O E   I I
E C   I H   N
T     S     G
'''


# 解法：将每一行的索引列出式子。
'''
 n = 4
 i = 0, i++  
0    6      12    (2n-2)*i     
1  5 7   11 13    (2n-2)*i+1 and 2(n-2)*(i+1)-1
2 4  8 10   14    (2n-2)*i+2 and 2(n-2)*(i+1)-2
3    9      15    (2n-2)*i+3

'''


class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        l = len(s)
        n = 2 * numRows - 2
        rst = ''
        lis = [[] for i in range(n)]
        for i in range(numRows):
            for j in range(0, l-i, n):
                rst += s[j + i]
                if i != 0 and i != numRows - 1 and j + n - i < l:
                    rst += s[j + n - i]
        return rst


def main():
    s = 'PAYPALISHIRING'
    solution = Solution()
    rst = solution.convert(s, 4)
    print(rst)


main()