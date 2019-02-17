# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import time


class TodaymoivePipeline(object):
    def process_item(self, item, spider):
        now = time.strftime('%y-%m-%d', time.localtime())
        filename = 'wuHao' + now + '.txt'
        with open(filename, 'a', encoding='utf-8') as fp:
            fp.write(item['moiveName'][0].encode('utf-8') + '\n\n')
        return item
