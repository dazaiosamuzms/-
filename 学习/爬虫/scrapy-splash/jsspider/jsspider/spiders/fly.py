import json
import base64
import scrapy
from scrapy_splash import SplashRequest


class MySpider(scrapy.Spider):
    name = 'fly'
    start_urls = ['https://www.baidu.com', ]

    def start_requests(self):
        splash_args = {
            'html': 1,
            'png': 1,
            'width': 600,
            'render_all': 1,
        }
        for url in self.start_urls:
            print(1)
            yield SplashRequest('https://www.baidu.com', self.parse, args=splash_args)
            print(3)

    # ...
    def parse(self, response):
        print(2)
        # magic responses are turned ON by default,
        # so the result under 'html' key is available as response.body
        html = response.body

        # you can also query the html result as usual
        title = response.css('title').extract_first()

        # full decoded JSON data is available as response.data:
        png_bytes = base64.b64decode(response.data['png'])

        print(html)
        print(png_bytes)
        # with open('1.png', 'wb') as fp:
        #     fp.write(png_bytes)


