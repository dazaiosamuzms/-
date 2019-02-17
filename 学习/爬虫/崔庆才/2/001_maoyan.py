#! \Local\Programs\Python\Python36\python.exe
# -*- coding: utf-8 -*-
__author__ = '98221254@qq.com'
'''
爬取猫眼电影排行
'''
import requests
import re
import json


def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                          ' (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return
    except requests.exceptions.RequestException as e:
        return e.response


def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?">(.*?)</i>.*?data-src="(.*?)".*?data-val.*?>(.*?)</a>.*?'
                         'star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2].strip(),
            'actor': item[3].strip()[3:] if len(item[3]) > 3 else '',
            'time': item[4].strip()[5:] if len(item[4]) > 5 else '',
            'score': item[5].strip() + item[6].strip()
        }


def write_to_file(data):
    with open('猫眼电影前100.txt', 'a', encoding='utf-8') as fp:
        fp.write(json.dumps(data, ensure_ascii=False) + '\n')  # 将字典转化编码为json数据


def main(offset):
    url = 'https://maoyan.com/board/4' + '?offset=' + str(offset)
    html = get_one_page(url)
    items = parse_one_page(html)
    for item in items:
        # print(item)
        write_to_file(item)


if __name__ == '__main__':
    for i in range(10):
        main(offset=i * 10)
