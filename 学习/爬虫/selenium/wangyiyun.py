#! \Local\Programs\Python\Python36\python.exe
# -*- coding: utf-8 -*-
__author__ = '98221254@qq.com'

import requests
from selenium import webdriver
from random import choice
import time


class Wangyiyun:
    def __init__(self):
        self.titles = []
        self.ids = []
        self.headers = {}

    def crawl(self, url):
        option = webdriver.ChromeOptions()
        option.add_argument("headless")
        driver = webdriver.Chrome(executable_path=r'C:\Users\Administrator\Desktop\chromedriver.exe', chrome_options=option)
        driver.set_window_size(1366, 768)
        driver.get(url)
        return driver

    # 网易云Api,大部分为get请求
    def getApi(self, s, url_type='album'):
        # 歌手热门前50
        singer = 'https://music.163.com/#/artist?id={}'
        # 搜索音乐
        search = 'https://music.163.com/#/search/m/?s=%{}&type={}'
        # 歌曲地址
        album = 'http://music.163.com/song/media/outer/url?id={}.mp3'
        # 歌曲名,封面,歌手
        # 注意得到的封面是大图,需要加上'param=90y90'参数来调节图片大小
        detail = 'https://music.163.com/api/song/detail/?ids=[{}]'
        # 歌单,参数是用户id 如我的49072873
        songlist = 'https://music.163.com/playlist?id={}'
        return eval(url_type).format(s)

    def singer_parse(self, driver):
        # 在源码中找到iframe标签
        # <iframe name="contentFrame" id="g_iframe" class="g-iframe"...></iframe>
        driver.switch_to.frame("g_iframe")
        driver.implicitly_wait(3)
        titles = driver.find_elements_by_xpath(
            '//table[@class="m-table m-table-1 m-table-4"]/tbody//span[@class="txt"]/a/b')
        ids = driver.find_elements_by_xpath(
            '//table[@class="m-table m-table-1 m-table-4"]/tbody//div[@class="hd"]/span[@class="ply "]')
        for _title in titles:
            self.titles.append(_title.get_attribute('title'))
        for _id in ids:
            self.ids.append(_id.get_attribute('data-res-id'))
        # print(titles[0].get_attribute('title'))
        # print(ids[0].get_attribute('data-res-id'))
        driver.close()

    def songlist_parse(self, driver):
        driver.switch_to.frame("g_iframe")
        driver.implicitly_wait(2)
        titles = driver.find_elements_by_xpath(
            '//table[@class="m-table"]/tbody/tr//span[@class="txt"]/a/b')
        ids = driver.find_elements_by_xpath(
            '//table[@class="m-table "]/tbody/tr/td[@class="left"]/div/span[@class="ply "]')
        for _title in titles:  # get_attribute(): 获取元素属性
            self.titles.append(_title.get_attribute('title'))
        for _id in ids:
            self.ids.append(_id.get_attribute('data-res-id'))
        driver.close()


class Setting:

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                      ' (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        'Accept-Language': 'zh-CN,zh;q=0.9',

    }

    proxies = ['http://111.177.178.170:9999', 'http://47.94.230.42:9999', 'http://111.177.174.58:9999',
               'http://110.52.235.77:9999', 'http://113.128.26.35:9999', 'http://58.211.183.46:40225',
               'http://117.90.252.244:9000', 'http://58.210.94.242:50514', 'http://60.184.34.232:9999',
               ]


def start():
    w = Wangyiyun()
    # url = w.getApi('3684', url_type='singer')
    url = w.getApi('49072873', url_type='songlist')
    driver = w.crawl(url)
    w.songlist_parse(driver)
    # print(w.ids)
    # 保存音乐文件
    # for i in range(3):
    #     url = w.getApi(w.ids[i])
    #     # res = request.urlopen(url)
    #     filename = w.titles[i] + '.mp3'
    #     print(url)
    #     proxy = choice(Setting.proxies)
    #     print(proxy)
    #     # rsq = requests.get(url, headers=Setting.headers, proxies={'http': proxy})
    #     rsq = requests.get(url, headers=Setting.headers)
    #     with open(filename, 'wb') as fp:
    #         fp.write(rsq.content)
    #     time.sleep(2)


if __name__ == '__main__':
    start()

