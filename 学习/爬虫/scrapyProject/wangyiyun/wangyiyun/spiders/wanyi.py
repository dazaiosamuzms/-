# -*- coding: utf-8 -*-
import scrapy
import scrapy_splash


class WanyiSpider(scrapy.Spider):
    name = 'wanyi'
    start_urls = ['https://music.163.com/#/artist?id=3684', ]
    url = 'http://music.163.com/song/media/outer/url?id=554242032'
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy_splash.SplashRequest(url,self.parse, args={'wait': 1.5})
            # yield  scrapy.Request(url, self.parse)

    def parse(self, response):
        print(1)
        song_id = response.xpath('.//table[@class="m-table m-table-1 m-table-4"]//span[@class="txt"]/a/@href').extract()[0]
        title = response.xpath('.//table[@class="m-table m-table-1 m-table-4"]//span[@class="txt"]/a/b/@title').extract()[0]
        print(song_id, title)
        # print(response.body)
        # with open('a.mp3', 'wb') as f:
        #     f.write(response.body)
        # with open('c.html','w',encoding='utf-8') as f:
        #     f.write(response.body.decode())
        # print(2)
