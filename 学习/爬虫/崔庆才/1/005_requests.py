#! \Local\Programs\Python\Python36\python.exe
# -*- coding: utf-8 -*-
__author__ = '98221254@qq.com'
'''
request 部分高级用法
'''

import requests


def get_req():
    data = {'name': '郑', 'age': 24}  # get参数
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    r = requests.get('http://httpbin.org/get', params=data, headers=headers)
    # print(r.text)    # 返回类型为str, 就算json数据也格式转换为str
    # print(r.json())  # 返回为json数据时, 直接将数据解析为字典
    # 获取返回的cookies和设置请求时的cookies
    print(r.cookies)
    for key, value in r.cookies.items():
        print(key, "+", value)
    # 抓取二进制数据 -- 图片, 视频, 音频
    res = requests.get('http://github.com/favicon.ico', timeout=2)  # 设置请求时间
    print(res.content[:10])  # 将r.content用open方法保存为相应的格式即可以正常显示


def post_req():
    url = 'http://httpbin.org/post'
    data = {'name': '郑', 'age': 24}
    r = requests.post(url, data=data)
    print(r.text)
    #文件上传
    files = {'file': open('cookies.txt', 'r')}  # 图片等二进制文件需要用'rb'模式
    r_file = requests.post(url, files=files)
    print(r_file.text)  # 文件会在单独的files字段中传输(不是存在form字段)


def set_cookies_proxies():
    cookies = '_xsrf=SDMBgJ0cVRvMHzz7zPy2lrr2qZ5CKkrR; _zap=f43d762c-46aa-484a-8967-28c8873057c7;' \
              ' d_c0="AABi5CeOuQ6PTq18JtB-yDrok7TgJYFAMwg=|1545750573"; z_c0="2|1:0|10:1545750594|4:' \
              'z_c0|92:Mi4xM1ZHTEF3QUFBQUFBc09EVko0NjVEaVlBQUFCZ0FsVk5RcFlQWFFDbnhmUGk2OHdMNzVPc3NHQW' \
              'thMG9RUFRIMGVR|56ea822a353a932a64264f6da35674f4f4e6ebadd435e41f36a40678fad1baf4";' \
              ' __gads=ID=c29cf3052767f58f:T=1546914942:S=ALNI_MaOX1mv1B9u5Szx8IALVUgbWvgwJQ;' \
              ' __utma=51854390.1638288843.1548061375.1548061375.1548061375.1; __utmz=51854390.' \
              '1548061375.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=51854390.100--' \
              '|2=registration_date=20161007=1^3=entry_date=20161007=1; q_c1=f5f0e347273a45869564eecb' \
              'f627f0d2|1548411284000|1545750596000; tgw_l7_route=66cb16bc7f45da64562a077714739c11; tst=r'
    jar = requests.cookies.RequestsCookieJar()  # 显示不可用,但是可用
    headers = {
        'Host': 'www.zhihu.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    proxies = {'http': 'http://10.10.1.10:3128',
               'https': 'http://10.10.1.10:1080'}  # 目前代理无效
    proxies = {'http': 'sock5://user:password@host:port',
               'https': 'sock5://user:password@host:port'}
    for cookie in cookies.split(';'):
        key, value = cookie.split('=', 1)
        jar.set(key, value)
    r = requests.get('http://www.zhihu.com', cookies=jar, headers=headers, proxies=proxies)
    print(r.text)


# 使用get和post请求同一地址时,requests在不同的会话中,需要提供一致的cookies才能保存同一状态
# 为了解决不同请求在用一个浏览器中进行, 可以使用session会话来保存, 通常用于模拟登录后操作
def set_session():
    s = requests.Session()
    r1 = s.get('http://httpbin.org/cookies/set/number/123456789')
    r2 = s.get('http://httpbin.org/cookies')
    print(r2.text)
    print(r2.cookies)


def set_ssl():
    r = requests.get('https://www.12306.cn', verify=False)  # 忽略证书认证
    # r = requests.get('https://www.12306.cn', cert=('/path/server.crt', '/path/key'))  # 设置
    print(r.status_code)


def auth_login():  # 身份认证
    r = requests.get('http://localhost:5000', auth=('username', 'password'))
    print(r.status_code)


if __name__ == '__main__':
    # get_req()
    # post_req()
    # set_cookies_proxies()
    # set_session()
    # set_ssl()
    auth_login()
