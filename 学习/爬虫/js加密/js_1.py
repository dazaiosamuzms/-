#! \Local\Programs\Python\Python36\python.exe
# -*- coding: utf-8 -*-
__author__ = '98221254@qq.com'
from urllib import request, parse

'''
通过请求时发送的参数，返回js
'''


def youdao(key):
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    # data和headers 都是直接复制网站中的请求数据
    data = {
        'i': 'girl',
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': '15477107630707',
        'sign': '16358e7a63fe19ad02ca8cd7452f6f39',
        'ts': '1547710763070',
        'bv': 'b33a2f3f9d09bde064c9275bcb33d94e',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTIME',
        'typoResult': 'false',
    }

    data = parse.urlencode(data).encode()
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        # 'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '254',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'OUTFOX_SEARCH_USER_ID=-1921669260@116.30.212.208; YOUDAO_MOBILE_ACCESS_TYPE=1;' \
                  ' OUTFOX_SEARCH_USER_ID_NCOO=1772025923.5816336; _ntes_nnid=de4fd8eba93945c35fd998ded0109b60,' \
                  '1547280374881; JSESSIONID=aaasS3h77LWOj80i7VAHw; ___rl__test__cookies=1547710763063',
        'Host': 'fanyi.youdao.com',
        'Origin': 'http://fanyi.youdao.com',
        'Referer': 'http://fanyi.youdao.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                      ' (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',

    }

    req = request.Request(url=url, data=data, headers=headers)
    rsp = request.urlopen(req)

    html = rsp.read().decode()
    print(html)


if __name__ == '__main__':
    youdao('girl')

