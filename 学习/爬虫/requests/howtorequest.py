#! \Local\Programs\Python\Python36\python.exe
# -*- coding: utf-8 -*-
__author__ = '98221254@qq.com'

'''
get请求
'''

import requests


url = 'https://baidu.com/s?'
params = {
    'wd': '大熊猫',
}


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                  ' (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}

# 使用requests.request()的方法
# rsp = requests.request('get', url, params=params, headers=headers)
# 使用requests.get()的方法
rsp = requests.get(url, params=params, headers=headers)

print(rsp.status_code)
# print(rsp.content)


'''
post请求
'''

import requests


url = 'https://fanyi.baidu.com/sug'
data = {
    'kw': 'world',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                  ' (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    'Content-Length': str(len(data))
}

# 使用requests.request()的方法
# rsp = requests.request('post', url, data=data, headers=headers)
# 使用requests.post()的方法
rsp = requests.post(url, data=data, headers=headers, json=None)

cookie = requests.utils.dict_from_cookiejar(rsp.cookies)
print(cookie)
print(dict(rsp.cookies))
# print(rsp.content)
