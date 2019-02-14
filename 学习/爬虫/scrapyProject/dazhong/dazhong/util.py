#! \Local\Programs\Python\Python36\python.exe
# -*- coding: utf-8 -*-
__author__ = '98221254@qq.com'
import re
import requests
from lxml import etree
import math


headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'lxsdk_cuid=1688833df65c8-0636d6537cadf8-6313363-1fa400-1688833df66c8; _lxsdk=1688833df65c8-0636d6537cad'
              'f8-6313363-1fa400-1688833df66c8; _hc.v=eb32cf4c-76d1-0c38-d013-948dde30927b.1548473330; _lx_utm=utm_sou'
              'rce%3DBaidu%26utm_medium%3Dorganic; cy=7; cye=shenzhen; s_ViewType=10; _lxsdk_s=168e0fb8cf7-1ea-9-1e5%7C%7C139',
    'Host': 'www.dianping.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}


def get_tag(_list, offset=1):
    # 找到tag中共同的字母
    _new_list = [data[0:offset] for data in _list]

    if len(set(_new_list)) == 1:
        offset += 1
        return get_tag(_list, offset)
    else:
        _return_data = [data[0:offset - 1] for data in _list][0]
        return _return_data


def get_css_and_tag(content):
    '''

    :param content: 爬取的链接
    :return: css链接，内含span对应tag
    '''

    find_css_url = re.search(r'href="([^"]+svgtextcss[^"]+)"', content, re.M)
    print(find_css_url)
    if not find_css_url:
        raise Exception("不能找到css_url")
    css_url = "https:" + find_css_url.group(1)

    class_num_tag = re.findall("<d class=\"(.*?)\"></d>", content)
    class_word_tag = re.findall("<e class=\"(.*?)\"></e>", content)
    _num_tag = get_tag(class_num_tag)
    _word_tag = get_tag(class_word_tag)
    print(class_num_tag)
    print(class_word_tag)
    return css_url, _num_tag


def get_css_and_px_dict(css_url):
    '''

    :param css_url: 所需的css链接
    :return: 提取属性与像素值的字典数据
    '''
    con = requests.get(css_url, headers=headers).content.decode('utf-8')
    find_datas = re.findall(r'(\.[a-zA-Z0-9-]+)\{background:(\-\d+\.\d+)px (\-\d+\.\d+)px', con)
    css_name_and_px = {}
    for data in find_datas:
        span_class_attr_name = data[0][1:]
        offset = data[1]
        position = data[2]
        css_name_and_px[span_class_attr_name] = [offset, position]
    return css_name_and_px


def get_svg_threshold_and_int_dict(css_url, _tag):
    con = requests.get(css_url, headers=headers).content.decode("utf-8")
    index_and_word_dict = {}
    find_svg_url = re.search(r'span class\^="*?background\-image: url\((.*?)\);' % _tag, con)
    if not find_svg_url:
        raise Exception("不能找到svg文件")
    svg_url = 'https:' + find_svg_url.group(1)
    svg_content = requests.get(svg_url, headers=headers).content
    root = H.document_fromstring(svg_content)
    datas = root.xpath('//text')
    last = 0
    for index, data in enumerate(datas):
        y = int(data.xpath('@y')[0])
        int_data = data.xpath('text()')[0]
        index_and_word_dict[int_data] = range(last, y+1)
        last = y
    return index_and_word_dict


def get_data(url):
    '''

    :param url: 待获取的url
    :return:
    '''
    con = requests.get(url, headers=headers).content.decode('utf-8')
    css_url, _tag = get_css_and_tag(con)
    css_and_px_dict = get_css_and_px_dict(css_url)
    svg_threshold_and_int_dict = get_svg_threshold_and_int_dict(css_url, _tag)
    doc = etree.HTML(con)
    shops = doc.xpath('//div[@id="shop-all-list"]/ul/li')
    for shop in shops:
        name = shop.xpath('.//div[@class="tit"]/a')[0].attrib["title"]
        print(name)
        comment_num = 0

        comment_and_price_datas = shop.xpath('.//div[@class="comment"]')
        for comment_and_price_data in comment_and_price_datas:
            _comment_data = comment_and_price_data.xpath('a[@class="review-num"]/b/node()')

            for _node in _comment_data:
                if isinstance(_node, etree._ElementStringResult):
                    comment_num = comment_num * 10 + int(_node)
                else:
                    span_class_attr_name = _node.attrib["class"]
                    offset, position = css_and_px_dict[span_class_attr_name]
                    index = abs(int(float(offset)))
                    position = abs(int(float(position)))
                    for key, value in svg_threshold_and_int_dict.iteritems():
                        if position in value:
                            threshold = int(math.ceil(index/12))
                            number = int(key[threshold])
                            comment_num = comment_num * 10 + number
            print(comment_num)


if __name__ == "__main__":
    url = 'http://www.dianping.com/shop/2369572'
    get_data(url)

