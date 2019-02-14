#! \Local\Programs\Python\Python36\python.exe
# -*- coding: utf-8 -*-
__author__ = '98221254@qq.com'
import requests
from lxml import etree
import re

# 注意每几个小时需要重新更新cookie
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': '_lxsdk_cuid=1688833df65c8-0636d6537cadf8-6313363-1fa400-1688833df66c8; _lxsdk=1688833df65c8-0636d6537cad'
              'f8-6313363-1fa400-1688833df66c8; _hc.v=eb32cf4c-76d1-0c38-d013-948dde30927b.1548473330; cy=7; cye=shenzhen;'
              ' s_ViewType=10; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_s=168e61c0444-a83-499-e32%7C%7C20',
    'Host': 'www.dianping.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}


def get_tag(_list, offset=1):
    _new_list = [data[0:offset] for data in _list]

    if len(set(_new_list)) == 1:
        offset += 1
        return get_tag(_list, offset)
    else:
        _return_data = [data[0:offset - 1] for data in _list][0]
        return _return_data


def get_tag_word(tags, css_url):
    '''

    :param tags: tag列表
    :return:
    '''
    css_content = requests.get(url=css_url).content.decode()
    _tag = get_tag(tags)
    com = re.compile('class\^="' + _tag + '".*?background-image: url\((.*?)\);')
    _svg_url = com.search(css_content).group(1)
    _svg_url = 'http:' + _svg_url

    index_word_dict = []
    for tag in tags:
        p = re.compile(tag + '\{+background:(?P<x>.*?)px (?P<y>.*?)px;')
        index_word_dict.append(p.search(css_content).groupdict())

    svg_content = requests.get(url=_svg_url).content.decode()
    selector = etree.HTML(svg_content.encode())
    datas = selector.xpath('//text')
    words = []
    for i in range(len(index_word_dict)):
        # 这里是难点，使用markmen测量出每个字位置关系
        tag_x = round((abs(eval(index_word_dict[i]['x'])) + 8) / 14)
        tag_y = int(abs(eval(index_word_dict[i]['y'])))
        for index, data in enumerate(datas):
            y = int(data.xpath('@y')[0])
            if tag_y < y:
                int_data = data.xpath('text()')[0]
                words.append(int_data[tag_x-1])
                break
    tag_word, i = {}, 0
    for tag in tags:
        tag_word.update({tag: words[i]})
        i += 1
    print(tag_word)
    return tag_word


def get_css_data(url):
    content = requests.get(url, headers=headers).content.decode()
    css_url = re.search(r'(s3plus\.meituan\.net.*?)\.css', content).group()
    css_url = 'http://' + css_url
    tags1 = re.findall(r'<d class="(\w*?)\"', content, re.M)
    tags2 = re.findall(r'<e class="(\w*?)\"', content, re.M)
    word1 = get_tag_word(tags1, css_url)
    word2 = get_tag_word(tags2, css_url)

# css_url = 'http://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/04858aaa1240e40354b6ea49e4bcbfb2.css'
# svg_url = 'http://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/f001adbda0ba52a3d5a17efe9c352f51.svg'


def start():
    p = re.compile('info-name">电话：</span>(.*?)/p>')


if __name__ == "__main__":
    url = 'http://www.dianping.com/shop/2369572'
    start(url)
