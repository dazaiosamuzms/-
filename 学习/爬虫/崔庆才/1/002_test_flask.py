#! \Local\Programs\Python\Python36\python.exe
# -*- coding: utf-8 -*-
__author__ = '98221254@qq.com'

from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return 'hello world'


if __name__ == "__main__":
    app.run()

