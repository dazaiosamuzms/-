# -*- coding: utf-8 -*-
import scrapy
import scrapy_splash


class JdSpider(scrapy.Spider):
    name = 'jd'
    # allowed_domains = ['www.item.jd.com']

    def start_requests(self):
        # start_urls = ['https://item.jd.com/6946605.html']  # 编码为'gbk'
        start_urls = ['https://music.163.com']
        change_url = 'https://music.163.com/artist?id=3684'
        args = {
            'html': 1,
            'png': 1,
            'wait': 0.5,
        }
        for url in start_urls:
            # 使用scrapy-splash的方法一
            yield scrapy_splash.SplashRequest(url, self.parse, args={'wait': 2.5}, splash_url=change_url)
            # yield scrapy.Request(url, self.parse)
            # 使用scrapy-splash的方法二
            # yield scrapy.Request(url, self.parse,
            #                      meta={'splash': {
            #                          'args': args,
            #                          'endpoint': 'render.json',
            #                      }})

    def parse(self, response):
        # print(response.body.decode('gbk'))
        # price = response.xpath('//span[@class="p-price"]/span/text()').extract()[1]
        # sales = response.xpath('//div[@class="prom-item"]/em/text()').extract()
        # value_addeds = response.xpath('//ul[@class="choose-support lh"]/li/a/span/text()').extract()
        # colors = response.xpath('//div[@id="choose-attr-1"]/div[@class="dd"]/div/a/i/text()').extract()
        # versions = response.xpath('//div[@id="choose-attr-3"]/div[@class="dd"]/div/a/text()').extract()
        # print(value_addeds)
        # print(colors)
        # print(versions)

        with open('wy.txt', 'w', encoding='utf-8') as fp:
            fp.write(response.body.decode())

        # print(response.body.decode())
        # song_id = response.decode().xpath('.//table[@class="m-table m-table-1 m-table-4"]//span[@class="txt"]/a/@href').extract()[0]
        # print(3)
        # title = response.xpath('.//table[@class="m-table m-table-1 m-table-4"]//span[@class="txt"]/a/b/@title').extract()[0]
        # print(song_id, title)
        print(2)

