# -*- coding: utf-8 -*-
from moive.items import MoiveItem
# from userAgents import pcUserAgent
import time

import scrapy


class MeijuSpider(scrapy.Spider):
    name = 'meiju'
    allowed_domains = ['lab.scrapyd.cn']
    start_urls = ['http://lab.scrapyd.cn']
    custom_settings = {
        'LOG_LEVEL': 'DEBUG',
        'LOG_FILE': './log/log_{}.txt'.format(time.time()),
        "DEFAULT_REQUEST_HEADERS": {
            'User-Agent': 'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
        }
    }
    # tag = '励志'

    def start_requests(self):
        url = 'http://lab.scrapyd.cn/'
        tag = getattr(self, 'tag', None)  # 获取tag值，也就是爬取时传过来的参数
        if tag is not None:  # 判断是否存在tag，若存在，重新构造url
            url = url + 'tag/' + tag  # 构造url若tag=爱情，url= "http://lab.scrapyd.cn/tag/爱情"
        yield scrapy.Request(url, self.parse)  # 发送请求爬取参数内容
        print('1', end=' ')

    def parse(self, response):
        mingyan = response.css('div.quote')
        for v in mingyan:
            item = MoiveItem()
            text = v.css('.text::text').extract_first()
            tags = v.css('.tags .tag::text').extract()
            tags = ','.join(tags)
            # filename = 'my_meiju.txt'
            # with open(filename, "a+", encoding='utf-8') as f:
            #     f.write(text + '\n')
            #     f.write('标签：' + tags)
            #     f.write('\n-------\n')

            item['text'] = text
            item['tags'] = tags
            yield item
        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
            print('2', end=' ')

    # def parse(self, response):
    #     mingyan = response.css('div.quote')
    #     for v in mingyan:
    #         item = MoiveItem()
    #         item['text'] = v.css('.text::text').extract_first()
    #         item['tags'] = v.css('.tags .tag::text').extract()
    #         item['tags'] = ','.join(item['tags'])
    #         item['next_page'] = response.css('li.next a::attr(href)').extract_first()
    #         if item['next_page'] is not None:
    #             item['next_page'] = response.urljoin(item['next_page'] )
    #         yield item
