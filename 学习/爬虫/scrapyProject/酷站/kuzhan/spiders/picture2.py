#! \Local\Programs\Python\Python36\python.exe
# -*- coding: utf-8 -*-
__author__ = '98221254@qq.com'

from urllib import request
from urllib import parse
from .userAgents import pcUserAgent



def zcool():
    url = 'https://www.zcool.com.cn/work/ZMjc3NjAwNjA=.html'

    headers = {

    }

    req = request.Request(url, data=None, headers=headers)
    useragent = pcUserAgent['Opera 11.11 - Windows']
    req.add_header(useragent.split(':')[0], useragent.split(':')[1])
    print(useragent)
    rsp = request.urlopen(req)
    res = rsp.read().decode('utf-8')
    with open('zcool.txt', 'w', encoding='utf-8') as fp:
        fp.write(res)




if __name__ == '__main__':
    z = zcool()