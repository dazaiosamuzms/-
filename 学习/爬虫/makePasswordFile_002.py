'''
函数式编程方式

生成密码字典的文件
'''

import os
import platform
import itertools
import time


def main():
    global rawList         # 原始列表
    global denyList        # 非法字符列表
    global pwList          # 密码列表
    global minLen          # 密码长度最小值
    global maxLen          # 密码长度最大值
    global timeout         # 等待时间
    global flag            # 创建文件状态
    rawList = []
    denyList = [' ', '', '@']
    pwList = []
    minLen, maxLen  = 6, 16
    timeout = 3
    flag = 0
    run = {
        '0': exit,                   # 退出
        '1': getRawList,             # 创建原始列表
        '2': addDenyList,            # 添加不可能出现的列表
        '3': clearRawList,           # 清除列表
        '4': setRawList,             # 原始列表排序
        '5': modifyPasswordLen,      # 修改最终的密码长度
        '6': createPasswordList,     # 创建最终的字典列表
        '7': showPassword,           # 显示密码
        '8': createPasswordFile,     # 创建密码文件

    }
    # 依靠while True循环mainMenu()的内容
    # 执行完函数后，break回到循环，实现主页面的跳回
    while True:
        mainMenu()
        op = input('输入选项:')
        # list[map(str, range(len(run)))] = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
        if op in map(str, range(len(run))):
            run.get(op)()
        else:
            tipMainMenuInputError()
            continue


def mainMenu():
    # global rawList
    # global denyList
    # global pwList
    # global flag
    clear()
    print('||')
    print('=' * 40)
    print('||')
    print('|| 0: 退出程序')
    print('|| 1: 输入原始字符串')
    print('|| 2: 添加非法字符到列表')
    print('|| 3: 清空原始密码列表')
    print('|| 4: 原始列表排序')
    print('|| 5: 修改最终的密码长度')
    print('|| 6: 创建最终的字典列表')
    print('|| 7: 显示密码')
    print('|| 8: 创建密码文件')
    print('||')
    print('=' * 40)
    print('||')
    print('当前非法字符为：', denyList)
    print('当前原始密码元素为：', rawList)
    print('共有{}个密码'.format(len(pwList)))
    if flag:
        print("已在当前目录创建密码文件")
    else:
        print('尚未创建密码文件')


#  清屏
def clear():
    OS = platform.system()  # 得到当前系统
    if OS == 'Windows':
        os.system('cls')  # windows清屏命令
    else:
        os.system('clear')  # linux清屏命令


#  错误提示
def tipMainMenuInputError():
    clear()
    print('只能输入0-8的整数，等待{}秒后重新输入'.format(timeout))

def rawlistIndexError():
    clear()
    print('=' * 30)
    print('元素不能超过3个')
    print("3秒后返回主菜单")


#  获取原始数据列表
def getRawList():
    clear()
    global denyList
    global rawList
    print('输入回车后直接退出')
    print('原始密码列表为:', rawList)
    st = None
    while not st == '':  # 不输入值时退出循环
        st = input("请输入密码元素字符串:")
        if st in denyList:
            print('这个字符串是预先设定的非法字符串')
            continue
        else:
            rawList.append(st)
            clear()
            print('输入回车后直接退出')
            print('当前原始密码列表为:', rawList)


#  添加非法词
def addDenyList():
    clear()
    global denyList
    print('输入回车后直接退出')
    print('当前非法字符为:', denyList)
    st = None
    while not st == '':
        print("请输入需要添加的非法字符串:")
        denyList.append(st)
        clear()
        print('输入回车后退出')
        print('当前非法字符为:', denyList)


#  清空原始数据列表
def clearRawList():
    global rawList
    rawList = []


#  整理原始数据列表
def setRawList():
    global rawList
    global denyList
    a = set(rawList)
    b = set(denyList)
    rawList = []
    for str in set(a - b):
        rawList.append(str)


#  修改默认密码的长度
def modifyPasswordLen():
    clear()
    global maxLen
    global minLen
    while True:
        print('当前密码长度为{}-{}'.format(minLen, maxLen))
        min = input("请输入密码的最小值")
        max = input("请输入密码的最大值")
        try:
            minLen = int(min)
            maxLen = int(max)
        except ValueError:
            print('密码长度必须输入6~16')
            break
        if minLen not in range(6, 17) or maxLen not in range(6, 17):
            print('密码长度必须输入6~16')
            minLen = 6
            maxLen = 16
            continue
        if minLen == maxLen:
            res = input('确定将密码长度设定为{}吗(Yy/Nn)？'.format(minLen))
            if res not in list('yYNn'):
                print("请输入(Yy/Nn)")
                continue
            elif res in list('Yy'):
                print("已设定密码长度为", minLen)
                break
            else:
                print("请重新设定长度")
                continue
        elif minLen > maxLen:
            minLen, maxLen = maxLen, minLen
        else:
            print('设置完毕，{}秒后返回菜单'.format(timeout))
            time.sleep(timeout)
            break


#  创建密码列表
def createPasswordList():
    global rawList
    global pwList
    global maxLen
    global minLen
    titleList = []
    swapcaseList = []
    for st in rawList:
        swapcaseList.append(st.swapcase())  # 字符串字母大小写反写
        titleList.append(st.title())        # 标题格式（第一个字母大写后面小写）
    sub1 = []
    sub2 = []
    for st in set(rawList + titleList + swapcaseList):
        sub1.append(st)   # sub1内有每个元素的大小写和标题格式，以全面匹配不同可能性
    for i in range(2, len(sub1) + 1):
        if len(rawList) > 3:
            rawlistIndexError()
            time.sleep(3)
            break
        # permutations()可以将sub1取i个元素不重复排列
        # permutations("abc",2) -> ab,ac,ba,bc,ca,cb
        sub2 += list(itertools.permutations(sub1, i))
    for tup in sub2:
        PW = ''
        for subPW in tup:
            PW += subPW
        if len(PW) in range(minLen, maxLen + 1):
            pwList.append(PW)
        else:
            pass


#  显示创建密码
def showPassword():
    global pwList
    global timeout
    for i in range(len(pwList)):
        if i % 4 == 0:
            print(pwList[i])
        else:
            print(pwList[i])
    print('显示{}秒后，回到主菜单'.format(timeout))
    time.sleep(timeout)


#  创建密码字典文件
def createPasswordFile():
    global flag
    global pwList
    print('当前目录下创建字典文件：dic.txt')
    time.sleep(timeout)
    with open('./dic.txt', 'w+') as fp:
        for PW in pwList:
            fp.write(PW)
            fp.write('\n')
    flag = 1


if __name__ == '__main__':
    main()
