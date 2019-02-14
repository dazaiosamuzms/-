#! \Local\Programs\Python\Python36\python.exe
# -*- coding: utf-8 -*-
__author__ = '98221254@qq.com'

from urllib import request, error


url = 'http://www.baidu.com'

# 使用proxy代理的步骤
# 1.设置代理地址,代理服务器在网上收集
proxy = {'http': '120.194.18.90:81', }
# 2.创建proxyHandler
proxy_handler = request.ProxyHandler(proxy)
# 3.创建Opener
opener = request.build_opener(proxy_handler)
# 4.安装Opener
request.install_opener(opener)

try:
    rsp = request.urlopen(url)
    html = rsp.read().decode()
    print(html)
except error.URLError as e:
    print(e)
except Exception as e:
    print(e)
