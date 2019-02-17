#! \Local\Programs\Python\Python36\python.exe
# -*- coding: utf-8 -*-
__author__ = '98221254@qq.com'
'''
xpath的使用需要借助lxml库
'''
from lxml import etree


text = '''
<div class='text'>
<ul>
<li class="item-0"><a href="link1.html">1 item</a></li>
<li class="item-1"><a href="link2.html">2 item</li>
<li class="item-inactive"><a href="link3.html">3 item</a></li>
<li class="item-0"><a href="link4.html">4 item</a></li>
<li class="item-1"><a href="link5.html">5 item</a>
</ul>
</div>
'''
html = etree.HTML(text)  # 可以自动修正,将text的缺失标签补充完整,并加上body和html标签
# html = etree.parse('./text.html', etree.HTMLParser())  # 直接读取文件
# print(html)
result = etree.tostring(html)  # 将html对象转化为str类型
# print(result.decode('utf-8'))  # bytes类型, 需要转码

selector1 = html.xpath('//li/a')  # xpath选择器筛选代码段
selector2 = html.xpath('//a[@href="link4.html"]/../@class')  # '../'可以向前找标签
sel_text = html.xpath('//li/a/text()')  # text() 获取标签文本内容
sel_attr = html.xpath('//li/a/@href')  # @href 获取标签的href属性值(不同属性名可不同)
selector3 = html.xpath('//li[position()<3]/a/text()')  # postion()可以筛选第几个同级标签,还有last()筛选最后一个
selector4 = html.xpath('//li[1]/ancestor::div/@class')  # ancestor获取祖先标签, child(子标签), descendant(子孙标签)
selector5 = html.xpath('//li[1]/attribute::*')  # attribute获取标签属性

print(selector4)
print(sel_attr)
