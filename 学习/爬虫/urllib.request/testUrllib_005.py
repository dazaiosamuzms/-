
# -*- coding: utf-8 -*-

'''
urllib 的学习
'''

# python3 已经没有urllib2,合并在urllib.request
# import urllib2
from urllib import request
import time
import platform
import os


def clear():
    print("内容较多，3秒后清屏")
    time.sleep(3)
    OS = platform.system()
    if OS == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def linkBaidu():
    url = 'http://www.baidu.com'
    try:
        response = request.urlopen(url, timeout=3)

    except request.URLError:
        print('网络错误')
        exit()
        # 这里注意window下创建新的文档默认编码为gbk，必须在新建文件时确定解码格式
    with open('./baidu.txt', 'w', encoding='utf-8') as fp:
        rst = response.read()
        print(rst.decode('utf-8'))
        fp.write(rst.decode('utf-8'))
    print("获取url信息,response.geturl()：", response.geturl())
    print("获取返回代码,response.getcode()：", response.getcode())
    print("获取url信息,response.info()：", response.info())
    print("获取网页内容已经存入当前目录的baidu.txt文件中")


if __name__ == '__main__':
    linkBaidu()

