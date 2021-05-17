# -*- coding:utf-8 -*-
from io import BytesIO,StringIO
from .共用 import *

class IO共用类():

    @异常检测
    def 取内容(self,*args,**kwargs):
        '长度：要取出的内容长度,-1为全部'
        return self.read(*args,**kwargs)

    @异常检测
    def 取全部内容(self):
        return self.getvalue()

    @异常检测
    def 加入内容(self,*args,**kwargs):
        '在当前位置插入新内容,默认为0,可使用 移动 调整位置'
        self.write(*args,**kwargs)
        return True

    @异常检测
    def 加入内容_列表(self,*args,**kwargs):
        "写入流列表，不提供换行符,用列表格式加入多行数据,如：self.writelines(['1','2'])"
        self.writelines(*args,**kwargs)
        return True

    @异常检测
    def 是否关闭(self):
        '如果流文件被关闭则返回True否则返回False'
        return self.closed()

    @异常检测
    def 是否可读取(self):
        '如果可以从流中读取则返回True否则返回False'
        return self.readable()

    @异常检测
    def 关闭(self):
        '释放缓冲区，执行此函数后，数据将被释放，也不可再进行操作'
        self.close()
        return True

    @异常检测
    def 刷新(self):
        '刷新缓冲区'
        self.flush()
        return True

    @异常检测
    def 移动(self,*args,**kwargs):
        '移动到指定位置'
        self.flush(*args,**kwargs)
        return True

    @异常检测
    def 取当前位置(self):
        return self.tell()

    @异常检测
    def 调整长度(self,*args,**kwargs):
        '将流大小调整为以字节为单位的给定大小（size），返回新的文件大小'
        return self.truncate(*args,**kwargs)

    @异常检测
    def 取行内容_列表(self,*args,**kwargs):
        '取出指定位置前的所有行,默认为全部行,并返回列表,一行一个成员'
        return self.readlines(*args,**kwargs)

    @异常检测
    def 取下一行(self, *args, **kwargs):
        '一行一行度,如果指定了长度则置则读取指定大小字节的数据'
        return self.readline(*args, **kwargs)

    @异常检测
    def 是否支持随机访问(self):
        '如果流支持随机访问则返回True否则返回false'
        return self.seekable()

    @异常检测
    def 是否支持写入(self):
        '如果流支持写入则返回true，否则返回false'
        return self.writable()


class 二进制流(IO共用类,BytesIO):
    '可以创建个io对象当路径用来写入二进制或者传入二进制返回个io对象当路径'
    pass


class 文本流(IO共用类,StringIO):
    pass