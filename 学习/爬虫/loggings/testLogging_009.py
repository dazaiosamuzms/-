#! \Local\Programs\Python\Python36\python.exe
# -*- coding: utf-8 -*-
__author__ = '98221254@qq.com'

import logging


class TestLogging:
    def __init__(self):
        logFormat = '%(asctime)-12s %(levelname)-8s %(name)-10s %(message)-12s'
        logFilename = './testLog.txt'
        logging.basicConfig(level=logging.INFO, format=logFormat,  # loggings.INFO = 20
                            filename=logFilename, filemode='w')
        logging.debug('debug message')
        logging.info('info message')
        logging.warning('warning message')
        logging.error('error message')
        logging.critical('critical message')


if __name__ == '__main__':
    tl = TestLogging()
