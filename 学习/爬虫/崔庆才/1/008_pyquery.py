#! \Local\Programs\Python\Python36\python.exe
# -*- coding: utf-8 -*-
__author__ = '98221254@qq.com'
'''
pyquery使用css选择器
'''
from pyquery import PyQuery as pq


with open('text2.html', 'r', encoding='utf-8') as fp:
    text2 = fp.read()
doc = pq(text2)   # ①可以直接导入html代码
# doc = pq(filename='text2.html')  # ②也可以导入文件路径获取
# ③还可以传入地址自动获取html处理
# doc = pq(url='http://baidu.com')  # 等同于requests.get(url).text
print(doc('title'))  # 采用css选择器解析

# css选择器: #id(id值), .attr(属性名), li(标签名)
lis = doc('#container .list')    # 筛选到class为list的ul标签,空格隔开,.无空格则是有2个class值
# print(lis)
lis_0 = lis.children('.item-0')  # children可以在其子节点中查找
# print(lis_0)
lis_0_a = lis_0.find('.bold')  # find可以查找子孙节点 等同于children('a .bold')
# print(lis_0_a)
lis_0_u_act = lis_0_a.parents('ul').find('.item-1.active')  # parent父级, parents祖父级,2个class值
# print(lis_0_p)
lis_0_u_1 = lis_0_u_act.siblings()  # siblings所有的兄弟节点
# print(lis_0_u_1)

# 伪类选择器 first-child第一个节点, last-child()最后一个节点, nth-child()
li1 = doc('li:first-child')   #
li2 = doc('li:nth-child(2)')  # 第2个li标签, 参数为2n则表示第偶数个标签
li = doc('li:gt(2)')          # 序列小于2的标签
li4 = doc('li:contains(fourth)')  # 文本内容包含fourth的li标签
# print(li)

# 遍历 获取 修改
for li in lis_0_u_1.items():   # 遍历方法：类似于字典类型,需要items()获取遍历每个同级子节点
    a = 1
    # print(li)
    # html()(获取代码), text()(获取文本),  attr(获取属性值和操作属性)
    # print(li.text())         # 获取该标签文本
    # print(li.attr('class'))  # 1个参数可以获取参数名对应值
    # print(li.attr('name', 'link'))  # 2个参数可以修改属性值或者添加属性
    # li.add_class('add_class')   # 将'add_class'添加到class属性
    # print(li)
    # li.remove_class('add_class')  # 将属性值删除, 类似方法remove_attr()
    # print(li)
    # print(li.find('span').remove())  # li内移除span标签, 返回移除内容
    # print(li)




