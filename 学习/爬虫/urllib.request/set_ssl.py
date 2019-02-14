#! \Local\Programs\Python\Python36\python.exe
# -*- coding: utf-8 -*-
__author__ = '98221254@qq.com'

from urllib import request
import ssl


ssl._create_default_https_context = ssl._create_unverified_context
url = 'http://www.12306.cn/mormhweb/'
rsp = request.urlopen(url)
html = rsp.read().decode()
print(html)