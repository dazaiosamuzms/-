# -*- coding: utf-8 -*-
'''
本爬虫功能可以批量爬取zcool.com.cn网站的图片
支持分页跳转，自动跳转页面
'''

import scrapy
import time
from kuzhan.items import KuzhanItem
from .userAgents import pcUserAgent


class PictureSpider(scrapy.Spider):
    name = 'picture'
    allowed_domains = ['zcool.com.cn']
    start_urls = ['https://www.zcool.com.cn/discover/0!0!0!0!0!!!!2!-1!1', ]

    for i in range(2,3):  # 获得前2页的页面url
        url = start_urls[0][:-1] + str(i)
        start_urls.append(url)
    useragent = pcUserAgent['Opera 11.11 - Windows']
    tag = None
    tags = []
    print(start_urls)

    custom_settings = {
        'LOG_LEVEL': 'DEBUG',
        'LOG_FILE': 'loger/log_{}.txt'.format(time.time()),
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse)

    def parse(self, response):
        for url in self.start_urls:  # 遍历每页的url
            item = KuzhanItem()
            item['start_url'] = url

            try:
                # print(response.url)
                pic = response.xpath('.//div[@class="reveal-work-wrap"]//img/@src').extract()
                title = response.xpath('.//head/title').extract()[0][7:-36]
                if not pic:
                    raise AttributeError
                # print(pic)
                item['title'] = title
                item['url'] = pic
                # print(title)
                yield item

            except AttributeError:
                self.tags = response.xpath('.//div[@class="card-img"]/a/@href').extract() or []
                # print(1)

            for tag in self.tags:
                self.tag = tag
                yield scrapy.Request(tag, self.parse)
            yield scrapy.Request(url, self.parse)
