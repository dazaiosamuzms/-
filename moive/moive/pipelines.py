# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from .spiders.meiju import MeijuSpider


class MoivePipeline(object):
    def process_item(self, item, spider):
        # with open("my_meiju.txt", 'a', encoding='utf-8') as fp:
        #     fp.write(item['name'] + '\n')

        filename = 'my_meiju.txt'
        with open(filename, "a+", encoding='utf-8') as f:
            f.write(item['text'] + '\n')
            f.write('标签：' + item['tags'])
            f.write('\n-------\n')
            print('3', end=' ')
            return item


