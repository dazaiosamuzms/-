#! \Local\Programs\Python\Python36\python.exe
# -*- coding: utf-8 -*-
__author__ = '98221254@qq.com'

'''
get 请求
'''
from urllib import request, parse


baseurl = 'https://baidu.com/s?'

data = {
    'wd': '大熊猫'
}
# 获得转码后的字符串
get_data = parse.urlencode(data)
print(get_data)
# 将url拼接，发送get请求
url = baseurl + get_data
rsp = request.urlopen(url)
print(rsp.read().decode()[200:300])  # 打印部分html字符
