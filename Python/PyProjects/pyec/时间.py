# -*- coding:utf-8 -*-
import datetime,time,random,locale
from .共用 import *

@异常检测
def 时间_取日期(增减天数=0):
    '默认返回当天日期,可直接用str转成文本,-1表示取昨天'
    if (增减天数 < 0):
        增减天数 = abs(增减天数)
        return datetime.date.today() - datetime.timedelta(days=增减天数)
    else:
        return datetime.date.today() + datetime.timedelta(days=增减天数)


def 时间_取启动时间():
    '3.8版本前使用,返回浮点数时间，计算指定程序,函数运行的时间'
    return time.clock()



def 时间_取启动时间2():
    '3.8版本起使用,返回浮点数时间，计算指定程序,函数运行的时间'
    return time.clock()


@异常检测
def 时间_取指定类型(时间戳=0, 类型='%X'):
    """出错返回空,传入时间戳,默认为当前时间的时间戳,默认返回 时:分:秒
    类型:
    %a  # 本地(local) 简化星期名称
    %A  # 本地完整星期名称
    %b  # 本地简化月份名称
    %B  # 本地完整月份名称
    %c  # 本地相应的日期和时间表示
    %d  # 一个月中的第几天（01-31）
    %H  # 一天中的第几个小时（24小时制00-23）
    %I  # 第几个小时（12小时制01-12）
    %j  # 一年中的第几天（001-366）
    %m  # 月份（01-12）
    %M  # 分钟数（00-59）
    %p  # 本地am或pm的相应符
    %S  # 秒（01-60）
    %U  # 一年中的星期数。（00-53 星期天是一个星期的开始）第一个星期天之前的所有天数都放在第0周
    %w  # 一个星期中的第几天（0-6 0是星期天）
    %W  # 和%U基本相同，不同的是%W以星期一为一个星期的开始
    %x  # 本地相应日期
    %X  # 本地相应时间
    %y  # 去掉世纪的年份（00-99）
    %Y  # 完整的年份
    %z  # 时区的名字
    """
    时间戳 = 时间戳 if 时间戳 else time.time()
    return time.strftime(类型, time.localtime(float(时间戳)))


def 时间_取现行时间_datetime():
    '返回datetime格式的时间'
    return datetime.datetime.now()


@异常检测
def 时间_取现行时间(格式="%Y-%m-%d %H:%M:%S"):
    '返回文本型的时间'
    return time.strftime(格式)


@异常检测
def 时间_取随机时间戳():
    "返回字符串类型的随机时间戳,0-1中间的数"
    return str(random.random())


@异常检测
def 时间_格式化(原时间, 时间格式="%Y-%m-%d %H:%M:%S"):
    '原时间可以是文本或datetime型,返回文本型'
    if isinstance(原时间, str):
        return datetime.datetime.strftime(datetime.datetime.strptime(原时间, "%Y-%m-%d %H:%M:%S"), 时间格式)
    else:
        return datetime.datetime.strftime(原时间, 时间格式)


@异常检测
def 时间_时间转文本(时间, 格式="%Y-%m-%d %H:%M:%S"):
    'datetime时间转成文本'
    return 时间.strftime(格式)


@异常检测
def 时间_增减(原时间, 增减部分, 增减数值):
    "原时间可以是文本或datetime型,返回datetime类型的时间,增减部分：1是星期,2是天,3是时,4是分,5是秒,6是毫秒,加时间就传正数,减时间传负数"
    字典 = {
        1: datetime.timedelta(weeks=增减数值),
        2: datetime.timedelta(days=增减数值),
        3: datetime.timedelta(hours=增减数值),
        4: datetime.timedelta(minutes=增减数值),
        5: datetime.timedelta(seconds=增减数值),
        6: datetime.timedelta(milliseconds=增减数值)
    }
    时间差 = 字典[增减部分]
    if isinstance(原时间, str):
        locale.setlocale(locale.LC_ALL, '')
        return datetime.datetime.strptime(原时间, "%Y-%m-%d %H:%M:%S") + 时间差
    else:
        return 原时间 + 时间差


@异常检测
def 时间_取时间间隔(原时间, 对比时间):
    "传入文本型的时间,返回秒数,整数型"
    return int(time.mktime(time.strptime(原时间, "%Y-%m-%d %H:%M:%S"))) - int(time.mktime(time.strptime(对比时间, "%Y-%m-%d %H:%M:%S")))


@异常检测
def 时间_时间转时间戳(时间, 格式="%Y-%m-%d %H:%M:%S"):
    "传入字符串类型时间,返回10位文本型时间戳"
    locale.setlocale(locale.LC_ALL, '')
    return str(int(time.mktime(time.strptime(时间, 格式))))


@异常检测
def 时间_时间戳转时间(时间戳, 格式='%Y-%m-%d %H:%M:%S'):
    '时间戳转换成文本型时间，支持10位或13位时间戳'
    if len(str(时间戳)) == 13:
        return time.strftime(格式, time.localtime(int(int(时间戳) / 1000)))
    elif len(str(时间戳)) == 10:
        return time.strftime(格式, time.localtime(int(时间戳)))

@异常检测
def 时间_取现行时间戳(是否取十位=False):
    "返回文本型时间戳,默认取13位时间戳"
    if 是否取十位 == True:
        return str(round(time.time()))
    else:
        datetime_object = datetime.datetime.now()
        now_timetuple = datetime_object.timetuple()
        now_second = time.mktime(now_timetuple)
        return int(now_second * 1000 + datetime_object.microsecond / 1000)
