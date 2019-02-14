#! \Local\Programs\Python\Python36\python.exe
# -*- coding: utf-8 -*-
__author__ = '98221254@qq.com'

'''
修改header
不同user-Agent的请求，返回不同的html数据
'''
from urllib import request
# from .userAgent import userAgents  # 这个没有红线，但是调用出错
from userAgent import userAgents   # 这个有红线，但是可以调用方法


# request模块修改header
class UrllibModifyHeader:
    def __init__(self):
        PIUA = userAgents.pcUserAgent.get('IE 9.0')   # IE浏览器
        MUUA = userAgents.mobileUserAgent.get('UC standard')  # UC浏览器（手机）
        self.url = 'http://fanyi.youdao.com'

        self.useUserAgent(PIUA, 1)
        self.useUserAgent(MUUA, 2)

    # 请求访问操作，useragent:user-Agent版本  name: html文件名
    def useUserAgent(self, useragent, name):
        req = request.Request(self.url)
        req.add_header(useragent.split(':')[0], useragent.split(':')[1])
        # Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)
        # 上面2段代码可以用下面一条代替
        # req = request.Request(self.url, headers={useragent.split(':')[0]:useragent.split(':')[1]})
        response = request.urlopen(req)   # urlopen.url: 可以为字符串或Request对象
        filename = str(name) + '.html'
        with open(filename, 'w', encoding='utf-8') as fp:
            fp.write((useragent + "\n\n"))
            fp.write(response.read().decode('utf-8'))


if __name__ == "__main__":
    umh = UrllibModifyHeader()



