#! \Local\Programs\Python\Python36\python.exe
# -*- coding: utf-8 -*-
__author__ = '98221254@qq.com'

from urllib import request
import sys
import os
import re


# 过滤输入参数
def testAragument():
    if len(sys.argv) != 2:
        print('只需要一个参数')
        tipUse()
        exit()
    else:
        TP = TestProxy(sys.argv[1])


# 显示提示信息
def tipUse():
    print("该程序之只能输入一个参数，这个参数必须是可用的proxy")
    print('usage: python testUrllibWithProxy_006.py http://192.168.0.1:4')
    print('usage: python testUrllibWithProxy_006.py https://192.168.0.1:4')


# TestProxy()作用是用于测试proxy是否有效
class TestProxy:
    def __init__(self, proxy):
        self.proxy = proxy
        self.checkProxyFormat(self.proxy)
        self.url = 'http://www.baidu.com'
        self.url = 'http://47.94.145.254:8081/home/'
        self.timeout = 5
        self.flagWord = '百度'
        self.useProxy(self.proxy)

    def checkProxyFormat(self, proxy):
        try:
            proxyMatch = re.compile('http[s]?://[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}:[\d]{1,5}$')
            re.search(proxyMatch, proxy).group()
        except AttributeError:
            tipUse()
            exit()
        flag = 1
        proxy = proxy.replace('//','')
        ip, protocol, port = '', '', ''
        try:
            protocol = proxy.split(':')[0]
            ip = proxy.split(':')[1]
            port = proxy.split(':')[2]
        except IndexError:
            print("index索引值超出列表范围")
            tipUse()
            exit()
        flag = flag and len(proxy.split(':')) == 3 and len(ip.split('.')) == 4
        flag = ip.split('.')[0] in map(str, range(1, 256)) and flag
        flag = ip.split('.')[1] in map(str, range(256)) and flag
        flag = ip.split('.')[2] in map(str, range(256)) and flag
        flag = ip.split('.')[3] in map(str, range(1, 255)) and flag
        flag = protocol in ['http', 'https'] and flag
        flag = port in map(str, range(1, 65535)) and flag

        if flag:
            print("输入的http代理服务器符合标准")
        else:
            tipUse()
            exit()

    def useProxy(self, proxy):
        protocol = proxy.split('//')[0].replace(':', '')
        ip = proxy.split('//')[1]
        # opener = request.build_opener(request.ProxyHandler({protocol: ip}))
        # request.install_open?er(opener)
        response = None
        try:
            response = request.urlopen(self.url, timeout=self.timeout)
        except:
            print(response)
            print('连接错误，退出程序')
            exit()
        str = response.read()
        if re.search(self.flagWord, str):
            print('已经取得特征词，该代理可用')
        else:
            print("该代理不可用")


if __name__ == '__main__':
    testAragument()
