#! \Local\Programs\Python\Python36\python.exe
# -*- coding: utf-8 -*-
__author__ = '98221254@qq.com'
import re
import requests
from lxml import etree

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


def get_css_svg_url(url, type='css'):
    if type == 'css':
        # content = requests.get(url, headers=headers).content.decode()
        # p = re.compile('info-name">电话：</span>(.*?)/p>')
        # su = p.search(content).group(1)
        su = '<d class="uoi135"></d><d class="uoiarx"></d><d class="uoieyw"></d><d class="uoieyw"></d>-<d class="uoi2vg"></d><d class="uoieyw"></d><d class="uoiuoa"></d>1<d class="uoiarx"></d><d class="uoiarx"></d><d class="uoi2vg"></d><d class="uoi2vg"></d> &nbsp; <d class="uoi135"></d><d class="uoiarx"></d><d class="uoieyw"></d><d class="uoieyw"></d>-<d class="uoi2vg"></d><d class="uoieyw"></d><d class="uoiuoa"></d><d class="uoi135"></d><d class="uoiarx"></d><d class="uoiarx"></d>11 <'
        print(su)
        result = re.findall(, su)
        # result.remove('')
        print(result)

if __name__ == '__main__':
    url = 'http://www.dianping.com/shop/2369572'
    get_css_svg_url(url)
