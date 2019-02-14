#! \Local\Programs\Python\Python36\python.exe
# -*- coding: utf-8 -*-
__author__ = '98221254@qq.com'
import requests
import json
# from lxml import etree
import re


def request_detail(url):
    dataes = []
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host': 'music.163.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                      ' (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',

    }
    session = requests.Session()
    rsq = session.get(url, headers=headers)
    text = json.loads(rsq.content)
    # print(text)
    title = text['songs'][0]['name']
    singer = text['songs'][0]['artists'][0]['name']
    imageUrl = text['songs'][0]['album']['blurPicUrl'] + '?param=180y180'
    data = {
        'title': title,
        'singer': singer,
        'songUrl': url,
        'imageUrl': imageUrl,
    }
    dataes.append(data)
    print(dataes)
    return dataes


rsq = request_detail('https://music.163.com/api/song/detail/?ids=[1318880077]')
# print(rsq)

