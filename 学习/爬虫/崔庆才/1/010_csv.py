#! \Local\Programs\Python\Python36\python.exe
# -*- coding: utf-8 -*-
__author__ = '98221254@qq.com'
'''
csv格式, 可以使用excel文件打开的纯文本字符串表格格式
'''
import csv


def csv_list():
    with open('data.csv', 'w', encoding='utf-8') as fp:
        writer = csv.writer(fp, delimiter=' ')  # write对象进行输入, delimiter表示分割符, 默认为','
        writer.writerow(['id', 'name', 'age'])  # 支持列表导入
        writer.writerows([['1001', 'Bob', '24'], ['1002', '郑', '25']])  # 也支持多行导入,注意用2维列表


# 爬虫爬取数据通常为字典类型, 因此也可以通过字典导入
def csv_dict():
    with open('data2.csv', 'w', encoding='utf-8') as f:
        fieldnames = ['id', 'name', 'age']
        writer = csv.DictWriter(f, fieldnames=fieldnames)  # filenames来导入使用字段, 必须导入
        writer.writeheader()  # 调用writeheader()先写入头信息, 才可以直接导入字典
        writer.writerow({'id': '1001', 'name': 'Bob', 'age': 24})
        writer.writerow({'id': '1002', 'name': '郑', 'age': 25})


def csv_open():
    with open('data2.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if row:  # 有空行
                print(row)


csv_list()
csv_dict()
csv_open()
