# -*- coding: utf-8 -*-
import scrapy
from urllib import parse
import scrapy_splash


class GoodsSpider(scrapy.Spider):
    name = 'goods'
    allowed_domains = ['https://www.amazon.cn/']

    def start_requests(self):
        base_url = 'https://www.amazon.cn/'
        data = {
            '__mk_zh_CN': '亚马逊网站',
            'url': 'search-alias=aps',
            'field-keywords': '人间失格',
        }
        get_data = parse.urlencode(data)
        url = base_url + 's/ref=nb_sb_noss_1' + get_data
        print(url)
        yield scrapy_splash.SplashRequest(url=url, callback=self.parse)

    def parse(self, response):
        print(response.text)
