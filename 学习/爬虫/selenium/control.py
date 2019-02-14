#! \Local\Programs\Python\Python36\python.exe
# -*- coding: utf-8 -*-
__author__ = '98221254@qq.com'

'''
selenium 是一个自动化工具
通过webdriver操作浏览器
'''

from selenium import webdriver
import time


# 通过Keys模拟键盘
from selenium.webdriver.common.keys import Keys

# 使用Phantomjs浏览器，想使用谷歌则用Chrome()
# driver会自动按照环境变量查找相应的浏览器，没有配置好则需要指定浏览器位置
driver = webdriver.PhantomJS(executable_path=r'D:\软件\phantomjs-2.1.1-windows\bin\phantomjs.exe')

driver.set_window_size(1366, 768)

# 如果没有在环境变量指定PhantomJS位置
# driver = webdriver.PhantomJS(executable_path = "./phantomjs")
# get方法会一直等到页面加载，然后才会继续程序，通常测试会在这里选择time.sleep(2)
driver.get("http://www.baidu.com/")

# 获取页面名为wraper的id标签的文本内容
data = driver.find_element_by_id('wrapper').text

# 打印数据内容
print(data)

# 生成页面快照并保存
# driver.save_screenshot("baidu.png")
#
# # id="kw"是百度搜索输入框，输入字符串"长城"
# driver.find_element_by_id('kw').send_keys(u'长城')
#
# # id="su"是百度搜索按钮，click()是模拟点击
# driver.find_element_by_id('su').click()
#
# # 获取新的页面快照
# driver.save_screenshot("长城.png")
#
# # 打印网页渲染后的源代码
# # print(driver.page_source)
#
# #获取当前页面Cookie
# # print(driver.get_cookies())
#
# # ctrl+a全选输入框内容
# driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'a')
# # ctrl+x剪切输入框内容
# driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'x')
#
# # 输入框重新输入内容
# driver.find_element_by_id('kw').send_keys('itcast')
#
# # 模拟Enter回车键
# driver.find_element_by_id('su').send_keys(Keys.RETURN)
# time.sleep(5)
#
# # 清空输入框内容
# driver.find_element_by_id('kw').clear()
#
# # 生成新的页面快照
# driver.save_screenshot('itcast.png')
#
# # 获取当前url
# print(driver.current_url)

