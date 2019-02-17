#! \Local\Programs\Python\Python36\python.exe
# -*- coding: utf-8 -*-
__author__ = '98221254@qq.com'
'''
urllib 的部分高级用法
'''

from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

import http.cookiejar
import urllib.request
import urllib.parse


# handler + opener 来构造用户名和密码验证
def login():
    username = 'zheng'
    password = '12345678'
    url = 'http://47.94.145.254:8081/account/login/'

    p = HTTPPasswordMgrWithDefaultRealm()
    p.add_password(None, url, username, password)
    auth_handler = HTTPBasicAuthHandler(p)
    opener = build_opener(auth_handler)

    try:
        result = opener.open(url)
        html = result.read().decode('utf-8')
        print(html)
    except URLError as e:
        print(e.reason)


def set_proxy():
    proxy_handler = ProxyHandler({
        'http': 'http://127.0.0.1:9743',
        'https': 'https://127.0.0.1:9743',
    })
    opener = build_opener(proxy_handler)
    try:
        response = opener.open('http://47.94.145.254:8081/home/')
        print(response.read().decode('utf-8'))
    except URLError as e:
        print(e.reason)


def set_cookies():
    # 打印cookie
    cookie = http.cookiejar.CookieJar()
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    response = opener.open('http://www.baidu.com/')
    for item in cookie:
        print(item.name + '=' + item.value)
    # 将cookie保存为文件的方法
    filename = 'cookies.txt'
    cookie2 = http.cookiejar.MozillaCookieJar(filename)
    # cookie2 = http.cookiejar.LWPCookieJar(filename)  # 保存为lwp格式
    handler2 = urllib.request.HTTPCookieProcessor(cookie2)
    opener2 = urllib.request.build_opener(handler2)
    response2 = opener2.open('http://www.baidu.com/')
    cookie2.save(ignore_discard=True, ignore_expires=True)


def parse_function():
    # 将url解析成6个部分
    base_url = 'http://www.baidu.com/index.html;user?id=5#comment'
    result = urllib.parse.urlparse(base_url)
    print(type(result), result)
    result2 = urllib.parse.urlsplit(base_url)
    print(type(result2), result)
    data = list(result)
    print(data)
    url = urllib.parse.urlunparse(data)
    print(url)
    # urljoin()  后面补充或者覆盖前面地址
    print(urllib.parse.urljoin('http://www.baidu.com', '?category=2#commit'))
    print(urllib.parse.urljoin('http://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html'))
    # urlencode() 拼接get请求参数序列化字典,  parse_qs 则反序列化为字典, parse_qsl 反序列化为元组
    params = {'name': '郑', 'age': 24}
    print('http://baidu.com?' + urllib.parse.urlencode(params))
    query = 'name=%E9%83%91&age=24'
    print(urllib.parse.parse_qs(query))


if __name__ == "__main__":
    # login()
    # set_proxy()
    # set_cookies()
    parse_function()
