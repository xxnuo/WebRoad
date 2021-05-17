# -*- coding:utf-8 -*-
import math
from .共用 import *
from decimal import Decimal

@异常检测
def 到数值(数值):
    '正常小数计算可能会多出很多个0，可以把要计算的小数传进来，梳理后的数值再去计算就正常了'
    return Decimal(str(数值))


@异常检测
def 数值_保留位数(数值,位数=2):
    '保留小数点后指定位数'
    return format(数值,'.{}f'.format(位数))


@异常检测
def 数值_取最小数(数值列表):
    '传入要对比的列表,如(1,2,3),返回里面最小的数字'
    return min(数值列表)


@异常检测
def 数值_取最大数(数值列表):
    '传入要对比的列表,如(1,2,3),返回里面最大的数字'
    return max(数值列表)


@异常检测
def 数值_取上入整数(数值):
    '示例:1.1返回2'
    return math.ceil(数值)


@异常检测
def 数值_取下入整数(数值):
    '示例:1.9返回1'
    return math.floor(数值)


@异常检测
def 数值_四舍五入(数值, 保留位数=0):
    return round(数值, 保留位数)


@异常检测
def 数值_取绝对值(数值):
    '传入一个数值,正负数还是小数都返回正的数值'
    return abs(数值)


@异常检测
def 数值_求次方(数值, 次方数):
    return pow(数值, 次方数)

