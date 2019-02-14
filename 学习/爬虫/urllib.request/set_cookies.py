#! \Local\Programs\Python\Python36\python.exe
# -*- coding: utf-8 -*-
__author__ = '98221254@qq.com'


# from urllib import request
#
# '''
# 手动的设置cookies数据
# '''
#
# url = "http://47.94.145.254:8082/news/"
# cookies = 'user_pk=MiJkFsF4jrEPHFevFWnXYe; csrftoken=8TgMZWwYajSgCYl' \
#           'CTON7BNECioVPrYXsP0IFErdsjuaA7i0L16zE6y4mHEM1MtsK;' \
#           ' sessionid=hc3ghtt27nzqitj9k4789g7nyfpei0e9'
#
# headers = {
#     'Cookie': cookies
# }
# req = request.Request(url, headers=headers)
# rsp = request.urlopen(req)
# html = rsp.read().decode()
#
# with open('rsp.html', 'w', encoding='utf-8') as f:
#     f.write(html)


'''
自动设置cookies数据
'''

# 使用http中的关于cookie的模块，自动获取cookie
# CookieJar > FileCookieJar > MozillaCookieJar & LwpCookieJar
# cookieJar: 管理存储cookie,向传出的http请求添加到cookie
#            cookie存储到内存中， CookieJar实例回收后cookie消失
# FileCookieJar: 使用文件管理cookie,filename来保存cookie文件
# MozillaCookieJar: 创建与mocilla浏览器cookie.txt兼容的FileCookieJar实例
# LwpCookieJar: 创建与libwww.perl标准兼容的Set-Cookie3格式的FileCookieJar实例


# FileCookieJar(filename, delayload=None, policy=None)
from urllib import request, parse
from http import cookiejar

# 创建cookiejar实例
cookie = cookiejar.CookieJar()
# 生成cookie的管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
# 生成http请求管理器
http_handler = request.HTTPHandler()
# 生成https请求管理器
https_handler = request.HTTPSHandler()
# 创建请求管理器
# build_opener(*handler) 其中handler是Handler的实例，封装不同的请求参数
# opener是OpenerDirector对象,用于操作的函数有open()
opener = request.build_opener(http_handler, https_handler, cookie_handler)


def login():
    '''
    负责初次登录
    需要输入用户名密码来获取cookie凭证
    :return:
    '''

    url = 'http://47.94.145.254:8082/xfz/login/'

    data = {
        'phone': '1234567890',
        'password': '12345678',
    }
    data = parse.urlencode(data)  # 将用户的账号密码格式转换
    # data: 'email=1234567890&password=12345678'
    req = request.Request(url, data=data.encode())

    rsp = opener.open(req)

def getHomePage():
    url = 'http://47.94.145.254:8082/news'
    # 如果已经执行了login函数， 则opener自动已经包含相应cookie值
    rsp = opener.open(url)
    html = rsp.read().decode()
    with open('rsp_2.html', 'w', encoding='utf-8') as f:
        f.write(html)


if __name__ == '__main__':
    login()
    #getHomePage()
    print(opener)
    print(cookie)   # 就是cookiejar.CookieJar()实例的值
    for cook in cookie:
        print('{}: {}'.format(cook.name, cook.value))






