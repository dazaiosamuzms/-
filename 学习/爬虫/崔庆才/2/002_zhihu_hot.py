#! \Local\Programs\Python\Python36\python.exe
# -*- coding: utf-8 -*-
__author__ = '98221254@qq.com'
'''
爬取知乎发现页面热门话题部分, 数据存储(txt)
'''
import requests
from pyquery import PyQuery as pq


url = 'http://www.zhihu.com/explore'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',

}
html = requests.get(url, headers=headers).text
doc = pq(html)
items = doc('.explore-tab .feed-item').items()
for item in items:
    question = item.find('h2').text()
    author = item.find('.author-link-line').text()
    answer = pq(item.find('.content').html()).text()
    file = open('zhihu_explore.txt', 'w', encoding='utf-8')
    file.write('\n'.join([question, author, answer]))
    file.write('\n' + '='*50 + '\n')
    file.close()
