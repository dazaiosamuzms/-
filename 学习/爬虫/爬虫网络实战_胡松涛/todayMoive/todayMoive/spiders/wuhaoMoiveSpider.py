# -*- coding: utf-8 -*-
import scrapy
from todayMoive.items import TodaymoiveItem
import json


class WuhaomoivespiderSpider(scrapy.Spider):
    name = 'wuhaoMoiveSpider'
    allowed_domains = ['jycinema.com']
    start_urls = ['http://www.jycinema.com/html/default/index.html', ]

    def start_requests(self):
        params = {
                "status": "HOT",
                "cityName": "深圳市",
                "type": "queryFilm",
                "DBType": "mongoDB",
                "channelCode": "J0002",
                "channelId": "3",
            }
        url = 'http://www.jycinema.com/frontUIWebapp/appserver/cinCinemaFilmViewService/findFilm'
        # yield scrapy.FormRequest(url=url,formdata=params)
        yield scrapy.Request(url, body=json.dumps(params), method='POST', headers={'Content-Type': 'application/json'},)

    def parse(self, response):
        # subSelector = response.xpath('//div[@class="film-header"]')
        subSelecotor = response.text
        print(subSelecotor)
        items = []
        # for sub in subSelector:
        #     item = TodaymoiveItem()
        #     item['moiveName'] = sub.xpath('./a/h3/text()').extract()
        #     items.append(item)
        # return items
