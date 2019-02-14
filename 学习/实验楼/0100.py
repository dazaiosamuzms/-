# sys.argv的用法探析
# sys.argv会将cmd中输入的内容保存为列表

import sys

a = sys.argv[:]

for i in a:
    print(i)
