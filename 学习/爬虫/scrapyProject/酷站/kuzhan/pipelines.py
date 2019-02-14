# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from urllib import request
import os


class KuzhanPipeline(object):
    def process_item(self, item, spider):
        dir_path = 'Picture/'
        start_url = item['start_url']
        page = start_url[-1:]
        urls = item['url']
        pic_num = 1

        dir = dir_path + page
        if not os.path.exists(dir):
            os.mkdir(dir)  # 建立文件夹

        for url in urls[1:]:  # 暂时未解决分页问题
            type = '.' + url.split('.')[-1]
            title = item['title'].split('/')[-1]    # 去除'/'，防止文件路径错误问题
            title = title.strip()                   # 去除多余的空格，防止文件保存错误
            title = title.replace('|', '')          # 小心特殊字符导致的无法保存文件
            title = title + '_' + str(pic_num)      # 添加每页的图片序列
            title = page + '/' + title              # 每页分开文件夹
            title = dir_path + title + type
            # print(title + start_url)
            pic_num += 1
            pic = request.urlopen(url).read()

            with open(title, 'wb+') as fp:
                fp.write(pic)
                pic_num += 1
                print(title)
        return item


