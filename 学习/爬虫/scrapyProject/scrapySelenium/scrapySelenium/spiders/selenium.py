# -*- coding: utf-8 -*-
import scrapy
import time


class SeleniumSpider(scrapy.Spider):
    name = 'selenium'

    def start_requests(self):
        url = 'https://music.163.com/artist?id=3684'
        yield scrapy.Request(url, callback=self.parse)

    custom_settings = {
        'LOG_LEVEL': 'DEBUG',
        'LOG_FILE': 'scrapySelenium/LOGGING/5688_log_%s.txt' % time.time(),
    }

    def parse(self, response):
        print('chrome is closed')
