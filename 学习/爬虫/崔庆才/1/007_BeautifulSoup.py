#! \Local\Programs\Python\Python36\python.exe
# -*- coding: utf-8 -*-
__author__ = '98221254@qq.com'
'''
BS是xml解析库,依赖于解析器(通常用lxml解析器)
'''
from bs4 import BeautifulSoup
with open('text.html', 'r') as fp:
    text = fp.read()
soup = BeautifulSoup(text, 'lxml')  # 自动补充缺失标签, 补全html,body,head等标签
# print(soup.prettify())   # 可以以字符串打印输出缩进格式的html
print(soup.title)          # 打印出整个title标签的代码
print(type(soup.title))    # 类型为bs4的元素标签对象  <class 'bs4.element.Tag'>
print(soup.title.string)   # 筛选出title节点, 打印节点文本(string)

print(soup.body.p.attrs)  # 自动补全后使用body标签下筛选, attrs可以获取属性字典
print(soup.p.attrs['name'])  # 字典类型使用[]提取内容
print(soup.p['name'])  # 获取属性的简单的写法

for i, child in enumerate(soup.p.children):
    print(i, child)
print(soup.a.contents)  # 以列表形式返回节点和文本的字符串

