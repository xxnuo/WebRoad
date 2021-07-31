# -*- coding:utf-8 -*-
import traceback,datetime


def 异常检测(function):
    '装饰器'
    def box(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except:
            print(function.__name__, "函数发生异常")
            print("错误发生时间：", str(datetime.datetime.now()))
            print("错误的详细情况：", traceback.format_exc())
    return box