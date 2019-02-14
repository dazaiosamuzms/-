#! \Local\Programs\Python\Python36\python.exe
# -*- coding: utf-8 -*-
__author__ = '98221254@qq.com'

'''
通过查看js文件，找到加密方式
'''

'''
分别查看boy和girl搜索时的请求，发现ts, salt, sign是不一样的
在fanyi.min.js中找到几个参数的计算函数

ts = r = "" + (new Date).getTime(),
salt = i = r + parseInt(10 * Math.random(), 10);
sign = n.md5("fanyideskweb" + e + i + "p09@Bn{h02_BIEe]$P^nG")
e = key
'''

import time
import random


def getTs():
    rst = int(time.time()*1000)
    rst = str(rst)
    return rst


def getSalt(r):
    rst = r + str(int(10 * random.random()))
    return rst


# MD5加密方式
def getMD5(v):
    import hashlib
    md5 = hashlib.md5()
    # update内的值需要bytes格式
    md5.update(v.encode('utf-8'))
    sign = md5.hexdigest()
    return sign


def getSign(key, salt):
    sign = "fanyideskweb" + key + salt + "p09@Bn{h02_BIEe]$P^nG"
    sign = getMD5(sign)  # getMD5()方法实现了js语言的n.md5()方法
    return sign

# 注意：ts是和时间相关，所以必须ts的值只能获取一次
ts = getTs()
salt = getSalt(ts)

from urllib import request, parse


def youdao(key):
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    # data和headers 都是直接复制网站中的请求数据
    data = {
        'i': key,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': salt,
        'sign': getSign(key, salt),
        'ts': ts,
        'bv': 'b33a2f3f9d09bde064c9275bcb33d94e',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTIME',
        'typoResult': 'false',
    }

    data = parse.urlencode(data).encode()
    print(data)
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        # 'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': len(data),  # data的长度不是固定的
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'OUTFOX_SEARCH_USER_ID=-1921669260@116.30.212.208; YOUDAO_MOBILE_ACCESS_TYPE=1;' \
                  ' OUTFOX_SEARCH_USER_ID_NCOO=1772025923.5816336; _ntes_nnid=de4fd8eba93945c35fd998ded0109b60,' \
                  '1547280374881; JSESSIONID=aaasS3h77LWOj80i7VAHw; ___rl__test__cookies=1547710763063',
        'Host': 'fanyi.youdao.com',
        'Origin': 'http://fanyi.youdao.com',
        'Referer': 'http://fanyi.youdao.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',

    }

    req = request.Request(url=url, data=data, headers=headers)
    rsp = request.urlopen(req)

    html = rsp.read().decode()
    print(html)


if __name__ == '__main__':
    youdao('girl')
