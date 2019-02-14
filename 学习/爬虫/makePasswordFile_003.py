'''
面向对象编程方式

生成密码字典的文件
'''


import os
import platform
import itertools
import time


class MakePassword:
    def __init__(self):
        self.rawList = []
        self.denyList = [' ', '', '@']
        self.pwList = []
        self.minLen, self.maxLen = 6, 16
        self.timeout = 3
        self.flag = 0
        self.run = {
            '0': exit,                 # 退出
            '1': self.getRawList,           # 创建原始列表
            '2': self.addDenyList,          # 添加不可能出现的列表
            '3': self.clearRawList,         # 清除列表
            '4': self.setRawList,           # 原始列表排序
            '5': self.modifyPasswordLen,    # 修改最终的密码长度
            '6': self.createPasswordList,   # 创建最终的字典列表
            '7': self.showPassword,         # 显示密码
            '8': self.createPasswordFile,   # 创建密码文件
        }

        self.main()

    def main(self):
        while True:
            self.mainMenu()
            op = input('输入选项:')
            # list[map(str, range(len(run)))] = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
            if op in map(str, range(len(self.run))):
                self.run.get(op)()
            else:
                self.tipMainMenuInputError()
                continue

    def mainMenu(self):
        self.clear()
        print('||')
        print('=' * 40)
        print('||')
        print('|| 0: 退出程序')
        print('|| 1: 输入原始字符串')
        print('|| 2: 添加非法字符到列表')
        print('|| 3: 清空原始密码列表')
        print('|| 4: 原始列表排序')
        print('|| 5: 修改最终的密码长度{}~{}'.format(self.minLen, self.maxLen))
        print('|| 6: 创建最终的字典列表')
        print('|| 7: 显示密码')
        print('|| 8: 创建密码文件')
        print('||')
        print('=' * 40)
        print('||')
        print('当前非法字符为：', self.denyList)
        print('当前原始密码元素为：', self.rawList)
        print('共有{}个密码'.format(len(self.pwList)))
        if self.flag:
            print("已在当前目录创建密码文件")
        else:
            print('尚未创建密码文件')

    def clear(self):
        OS = platform.system()  # 得到当前系统
        if OS == 'Windows':
            os.system('cls')  # windows清屏命令
        else:
            os.system('clear')  # linux清屏命令

    #  错误提示
    def tipMainMenuInputError(self):
        self.clear()
        print('只能输入0-8的整数，等待{}秒后重新输入'.format(self.timeout))

    def rawlistIndexError(self):
        self.clear()
        print('=' * 30)
        print('元素不能超过3个')
        print("3秒后返回主菜单")

    #  获取原始数据列表
    def getRawList(self):
        self.clear()
        print('输入回车后直接退出')
        print('原始密码列表为:', self.rawList)
        st = None
        while not st == '':  # 不输入值时退出循环
            st = input("请输入密码元素字符串:")
            if st in self.denyList:
                print('这个字符串是预先设定的非法字符串')
                continue
            else:
                self.rawList.append(st)
                self.clear()
                print('输入回车后直接退出')
                print('当前原始密码列表为:', self.rawList)

    #  添加非法词
    def addDenyList(self):
        self.clear()
        print('输入回车后直接退出')
        print('当前非法字符为:', self.denyList)
        st = None
        while not st == '':
            print("请输入需要添加的非法字符串:")
            self.denyList.append(st)
            self.clear()
            print('输入回车后退出')
            print('当前非法字符为:', self.denyList)

    #  清空原始数据列表
    def clearRawList(self):
        self.rawList = []

    #  整理原始数据列表
    def setRawList(self):
        a = set(self.rawList)
        b = set(self.denyList)
        self.rawList = []
        for str in set(a - b):
            self.rawList.append(str)

    #  修改默认密码的长度
    def modifyPasswordLen(self):
        self.clear()
        while True:
            print('当前密码长度为{}-{}'.format(self.minLen, self.maxLen))
            min = input("请输入密码的最小值")
            max = input("请输入密码的最大值")
            try:
                self.minLen = int(min)
                self.maxLen = int(max)
            except ValueError:
                print('密码长度必须输入6~16')
                break
            if self.minLen not in range(6, 17) or self.maxLen not in range(6, 17):
                print('密码长度必须输入6~16')
                self.minLen = 6
                self.maxLen = 16
                continue
            if self.minLen == self.maxLen:
                res = input('确定将密码长度设定为{}吗(Yy/Nn)？'.format(self.minLen))
                if res not in list('yYNn'):
                    print("请输入(Yy/Nn)")
                    continue
                elif res in list('Yy'):
                    print("已设定密码长度为", self.minLen)
                    break
                else:
                    print("请重新设定长度")
                    continue
            elif self.minLen > self.maxLen:
                self.minLen, self.maxLen = self.maxLen, self.minLen
            else:
                print('设置完毕，{}秒后返回菜单'.format(self.timeout))
                time.sleep(self.timeout)
                break

    #  创建密码列表
    def createPasswordList(self):
        titleList = []
        swapcaseList = []
        for st in self.rawList:
            swapcaseList.append(st.swapcase())  # 字符串字母大小写反写
            titleList.append(st.title())  # 标题格式（第一个字母大写后面小写）
        sub1 = []
        sub2 = []
        for st in set(self.rawList + titleList + swapcaseList):
            sub1.append(st)  # sub1内有每个元素的大小写和标题格式，以全面匹配不同可能性
        for i in range(2, len(sub1) + 1):
            if len(self.rawList) > 3:
                self.rawlistIndexError()
                time.sleep(3)
                break
            # permutations()可以将sub1取i个元素不重复排列
            # permutations("abc",2) -> ab,ac,ba,bc,ca,cb
            sub2 += list(itertools.permutations(sub1, i))
        for tup in sub2:
            PW = ''
            for subPW in tup:
                PW += subPW
            if len(PW) in range(self.minLen, self.maxLen + 1):
                self.pwList.append(PW)
            else:
                pass

    #  显示创建密码
    def showPassword(self):
        for i in range(len(self.pwList)):
            if i % 4 == 0:
                print(self.pwList[i])
            else:
                print(self.pwList[i])
        print('显示{}秒后，回到主菜单'.format(self.timeout))
        time.sleep(self.timeout)

    #  创建密码字典文件
    def createPasswordFile(self):
        print('当前目录下创建字典文件：dic.txt')
        time.sleep(self.timeout)
        with open('./dic.txt', 'w+') as fp:
            for PW in self.pwList:
                fp.write(PW)
                fp.write('\n')
        self.flag = 1


if __name__ == '__main__':
    mp = MakePassword()

