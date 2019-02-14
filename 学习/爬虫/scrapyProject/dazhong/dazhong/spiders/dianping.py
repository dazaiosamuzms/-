# -*- coding: utf-8 -*-
import scrapy


class DianpingSpider(scrapy.Spider):
    name = 'dianping'
    allowed_domains = ['http://www.dianping.com/']
    start_urls = ['http://www.dianping.com/shop/2369572']

    def parse(self, response):
        selectors = response.Xpath('')
