'''
给定一个字符串 (s) 和一个字符模式 (p)。实现支持 '.' 和 '*' 的正则表达式匹配。
'.' 匹配任意单个字符。   '*' 匹配零个或多个前面的元素。
匹配应该覆盖整个字符串 (s) ，而不是部分字符串。
'''
# 太难了放弃，直接用re模块


class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        import re
        value = re.match(p, s)
        if value == None or value.group(0) != s:
            return False
        else:
            return True





# class Solution:
#     def isMatch(self, s, p):
#         """
#         :type s: str
#         :type p: str
#         :rtype: bool
#         """
#         rst = 'false'
#         check = False
#         team = False
#         index = 0
#         symbol = []
#
#         if s == '' or p == '':
#             if s == '':
#                 rst = 'true'
#             else:
#                 rst = 'false'
#
#         elif p[0] == '*':
#             rst = 'false'
#
#         else:
#             for i in p:
#                 if i in '.*':
#                     if i == '.':
#                         symbol.append(-index)
#                         team = True
#                     else:
#                         symbol.append(index)
#                     check = True
#                 index += 1
#
#             index = 0
#             for i in p:
#                 if not check:
#                     if s == p:
#                         rst = 'true'
#                         break
#                 if check and team:
#                     for k, j in enumerate(symbol):
#                         if j < 0 and p[symbol[k+1]] == -j + 1:
#                             if p[:j]  # a*bb.*cc -> a*bb
#
#
#
#                 index += 1
#     # 判断有*且没有.时的匹配
#     def isMatch_b(self, s, p, symbol=None):
#         if symbol:
#             for i, j in enumerate(symbol):
#                 if i == 0:
#                     if p[:j] != s[:j]:
#                         rst = False
#                 else:
#                     if






