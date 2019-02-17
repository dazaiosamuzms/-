#! \Local\Programs\Python\Python36\python.exe
# -*- coding: utf-8 -*-
__author__ = '98221254@qq.com'
'''
MySQL 数据库使用来存储
'''
import pymysql


def add_data(_db, _table, _data):
    cursor = _db.cursor()  # cursor()获得数据库的操作游标
    cursor.execute('SELECT VERSION()')  # execute()输入代码,如同在mysql-cli中操作一样
    version = cursor.fetchone()
    print('Database version:', version)
    # 创建数据库spiders, 只需要执行一次
    # cursor.execute('CREATE DATABASE spiders DEFAULT CHARACTER SET utf8')
    cursor.execute('USE spiders')
    # 创建数据表students, 只需要执行一次
    # sql = 'CREATE TABLE IF NOT EXISTS students(id VARCHAR(255) NOT NULL, ' \
    #       'name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY (id))'
    # cursor.execute(sql)

    for i in range(len(_data)):
        table = _table  # 将所有可变值以参数形式导入sql语句
        keys = ','.join(_data[i].keys())
        values = ','.join(['%s'] * len(_data[i]))
        sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)

        try:  # 为了保持一致性, 标准格式为出错则滚回
            print(sql)
            cursor.execute(sql, tuple(_data[i].values()))  # execute()可以加入元组参数来补充sql语句变量
            _db.commit()  # 对于数据的插入, 更新, 修改操作时必须commit()提交
            print('success')
        except:
            _db.rollback()  # 数据滚回,取消修改
            print('fail')
            db.close()


# 去重处理 若重复则更新,不存在则创建, 升级版add_data()
def add_update_data(_db, _table, _data):
    cursor = _db.cursor()  # cursor()获得数据库的操作游标
    cursor.execute('USE spiders')
    for i in range(len(_data)):
        table = _table
        keys = ', '.join(_data[i].keys())
        values = ', '.join(['%s'] * len(_data[i]))
        sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table=table, keys=keys, values=values)
        update = ','.join([" {key} = %s".format(key=key) for key in _data[i]])
        sql = sql + update
        print(sql)
        print(tuple(_data[i].values())*2)
        try:
            cursor.execute(sql, tuple(_data[i].values())*2)
            print('add success')
            _db.commit()
        except:
            print('add or update fail')
            _db.rollback()
            db.close()


def del_data(_db, condition, _table):
    cursor = _db.cursor()
    sql = 'DELETE FROM {table} WHERE {condition}'.format(table=_table, condition=condition)
    try:
        cursor.execute(sql)
        db.commit()
        print('del success')
    except:
        print('del fail')
        db.rollback()


# 查询不需要提交, 所以也不需要滚回
def show_data(_db, condition, _table):
    cursor = _db.cursor()
    sql = 'SELECT * FROM {table} WHERE {condition}'.format(table=_table, condition=condition)
    try:
        cursor.execute(sql)
        print('show success')
        # return cursor.fetchall()  # fetchall可以查询出所有符合条件的数据,但是面对大量数据十分费时
        row = cursor.fetchone()  # fetchone可以一次查询数一条数据
        while row:
            print('Count:', row)
            row = cursor.fetchone()
        return row
    except:
        print('show fail')


if __name__ == '__main__':
    db = pymysql.connect(host='localhost', user='root', password='12345678', port=3306)  # 连接数据库
    data = [{'id': '2001', 'name': 'Bob', 'age': 20}, {'id': '2002', 'name': '郑', 'age': 24}]
    table = 'students'
    # add_data(db, table, data)
    updata = [{'id': '2001', 'name': 'Bob', 'age': 23}, ]
    add_update_data(db, table, updata)

    cond1 = 'age < 24'
    cond2 = 'age >= 24'
    del_data(db, cond1, table)
    show_data(db, cond2, table)
    # show = show_data(db, cond2, table)
    # print('Count:', show)

    db.close()

