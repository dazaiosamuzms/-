#! \Local\Programs\Python\Python36\python.exe
# -*- coding: utf-8 -*-
__author__ = '98221254@qq.com'
'''
json库
'''
import json


# 注意: json数据格式(内部的数据必须以""(双引号)包围, 不然造成loads()解析失败)
st = '''
[{
    "name": "Bob",
    "gender": "male",
    "birthday": "1992-10-18"
},{
    "name": "lina",
    "gender": "female",
    "birthday": "1995-10-18"
}]
'''
print(type(st))
data = json.loads(st)  # loads()可以将json数据转化为js的对象或数组
print(type(data))      # js数组 也就是python列表
print(data)            # 注意得到的数据都是str格式
print(data[0].get('name'))  # 或者data[0]['name']

with open('data.json', 'r', encoding='utf-8') as fp:  # 读取文本的json数据
    st2 = fp.read()
    data = json.loads(st2)
    print(data)
    data[0].update({'age': '25'})
    print(data)
    fp.write(json.dumps(data, indent=2))  # dumps()可以将字典或列表转换为json对象, indent表示str的缩进字符个数
    # fp.write(json.dumps(data, indent=2, ensure_ascii=False))  # ensure_ascii可以防止中文编码, 但是一般不使用
