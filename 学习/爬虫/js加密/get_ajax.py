#! \Local\Programs\Python\Python36\python.exe
# -*- coding: utf-8 -*-
__author__ = '98221254@qq.com'

'''
ajax请求会根据你的操作继续发送请求
比如下滑页面会不断刷新，需要分析每次下滑时的请求地址和请求类型
'''

from urllib import request, parse
import json


'''
分析请求地址
https://movie.douban.com/typerank?type_name=%E5%96%9C%E5%89%A7&type=24&interval_id=100:90&action=  (页面原始地址)
https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=20&limit=20   (下滑后第一个请求地址)
https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=40&limit=20   (下滑后第二个请求地址)

interval_id=100%3A90   代表评分区间
action=                未知
start=20               开始电影序列
limit=20               获取数据个数
'''

# 豆瓣电影喜剧片排行榜 get请求
url_base = 'https://movie.douban.com/j/chart/top_list?type=24&'


def get(start, end):
    if end - start == 10 and end % 10 == 0:
        rst = '' + str(end) + ':' + str(start)
        return rst

date = {
    'interval_id': get(90, 100),
    'action': '',
    'start': 20,
    'limit': 20,
}

date = parse.urlencode(date)
url = url_base + date
# https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=20&limit=20

print(url)
rsp = request.urlopen(url)
data = rsp.read().decode()
data = json.loads(data)
print(data)
