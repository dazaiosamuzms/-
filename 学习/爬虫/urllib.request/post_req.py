#! \Local\Programs\Python\Python36\python.exe
# -*- coding: utf-8 -*-
__author__ = '98221254@qq.com'

'''
post 请求
'''

from urllib import request, parse
import json


baseurl = 'https://fanyi.baidu.com/sug'

data = {
    'kw': 'world',
}
# 用parse.urlencode()可以将字典解析成字节编码字符串
data = parse.urlencode(data).encode()
print(data)
# 请求头
headers = {
    'Content-Length': len(data)
}

# 构造请求
req = request.Request(url=baseurl, data=data, headers=headers)
# req.add_header()

# 发送请求
rsp = request.urlopen(req)
json_data = rsp.read().decode()  # decode()解码时，默认为utf-8
print(type(json_data))
print(json_data)

# json数据必须用json.loads()解析
json_data = json.loads(json_data)
print(json_data)