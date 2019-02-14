#! \Local\Programs\Python\Python36\python.exe
# -*- coding: utf-8 -*-
__author__ = '98221254@qq.com'

import re
from urllib import request


# 获取影院当日影视
class TodayMovie:
    def __init__(self):
        self.url = 'http://www.jycinema.com/html/default/index.html'
        self.timeout = 5
        self.filename = './todayMoive.txt'
        self.getMovieInfo()

    def getMovieInfo(self):
        response = request.urlopen(self.url, timeout=self.timeout)
        print(response.read().decode('utf-8'))
        moiveList = re.findall('film-title.*', response.read().decode('utf-8'))
        with open(self.filename, 'w', encoding='utf-8') as fp:
            for moive in moiveList:
                moive = self.subStr(moive)
                print(moive)
                fp.write(moive + '\n')

    def subStr(self, st):
        st = st.replace('film-title">', '')
        st = st.replace('</h3>', '')
        return st


if __name__ == "__main__":
    tm = TodayMovie()
