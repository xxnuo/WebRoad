# -*- coding:utf-8 -*-
import sys,os,stat,hashlib
from functools import partial
from .共用 import *

@异常检测
def 文件_取运行目录():
    return os.getcwd()


@异常检测
def 文件_取临时目录(目录='.'):
    '打包exe资源文件的时候用的地址'
    return sys._MEIPASS if getattr(sys, "frozen", False) else os.path.abspath(目录)


@异常检测
def 文件_遍历指定路径文件(路径='.'):
    '.为单前目录，..为上级目录，目录下的文件名,文件夹名,不带路径'
    return os.listdir(路径)


@异常检测
def 文件_遍历指定路径所有子目录(路径='.'):
    '成功返回列表：(路径, [包含目录], [包含文件]),用法 for root, dirs, files in os.walk("..", topdown=False):'
    return list(os.walk(路径))


@异常检测
def 文件_创建单层目录(路径):
    '成功返回True,创建单层目录'
    os.mkdir(路径)
    return True


@异常检测
def 文件_创建多层目录(路径):
    '成功返回True,创建单层目录，如该目录已存在抛出异常'
    os.makedirs(路径)
    return True


@异常检测
def 文件_写入文件(文件名, 写入的数据,模式=0, 编码="utf-8"):
    """成功返回True
    如果文件不存在会创建新文件
    模式：0.文本追加 1.文本覆盖 2.字节集追加 3.字节集覆盖
    字节集不需要编码,默认为文本追加写入
    更多模式参考https://www.runoob.com/python3/python3-func-open.html"""
    字典 = {0:'a',1:'w',2:'ab',3:'wb'}
    目录, 文件 = os.path.split(文件名)
    if 目录 != '' and os.path.exists(目录) is False:
        os.makedirs(目录)
    if 模式 < 2:
        with open(文件名, 字典[模式], encoding=编码) as a:
            a.write(写入的数据)
    else:
        with open(文件名, 字典[模式]) as a:
            a.write(写入的数据)
    return True


@异常检测
def 文件_读取文件(文件名, 字节集=False,编码="utf-8", 读取长度=-1):
    '方式默认用r 字节集用rb 长度默认读取全部,更多模式参考https://www.runoob.com/python3/python3-func-open.html'
    if 字节集:
        with open(文件名, 'rb') as a:
            return a.read(读取长度)
    else:
        with open(文件名, 'r', encoding=编码) as a:
            return a.read(读取长度)


@异常检测
def 文件_删除文件(路径):
    '成功返回True,用于删除文件,如果文件是一个目录则返回一个错误'
    os.remove(路径)
    return True


@异常检测
def 文件_删除文件2(路径):
    '成功返回True,用于删除文件,如果文件是一个目录则返回一个错误'
    os.unlink(路径)
    return True


@异常检测
def 文件_删除单层空目录(路径):
    '成功返回True,失败返回False,删除单层空目录'
    try:
        os.rmdir(路径)
        return True
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return False

@异常检测
def 文件_删除多层空目录(路径):
    '成功返回True,递归删除目录，从子目录到父目录逐层尝试删除，遇到非空目录则抛出异常'
    os.removedirs(路径)
    return True


@异常检测
def 文件_重命名(原文件名, 新文件名):
    '成功返回True,可以是文件或文件夹'
    os.rename(原文件名, 新文件名)
    return True


@异常检测
def 文件_目录文件名分割(路径):
    '传入路径,返回元组类型 (目录,文件名)'
    return os.path.split(路径)


@异常检测
def 文件_文件扩展名分割(路径):
    '传入文件路径,返回元组类型 (文件名,扩展名)'
    return os.path.splitext(路径)


@异常检测
def 文件_取文件名(路径):
    '去掉目录路径，返回文件名'
    return os.path.basename(路径)


@异常检测
def 文件_取文件目录(路径):
    '去掉文件名，返回目录路径'
    return os.path.dirname(路径)


@异常检测
def 文件_更改当前工作目录(路径):
    '成功返回True'
    os.chdir(路径)
    return True


@异常检测
def 文件_更改当前进程目录(路径):
    '成功返回True'
    os.chroot(路径)
    return True

@异常检测
def 文件_检测权限(路径, 类型=0):
    '类型：0 是否存在 1 是否可读 2 是否可写 3 是否可执行，返回True或False'
    权限 = {0:os.F_OK,1:os.R_OK,2:os.W_OK,3:os.X_OK}
    return os.access(路径, 权限[类型])


@异常检测
def 文件_是否为绝对路径(路径):
    '传入路径返回True或False'
    return os.path.isabs(路径)


@异常检测
def 文件_是否为目录(路径):
    '传入路径返回True或False'
    return os.path.isdir(路径)


@异常检测
def 文件_是否为文件(路径):
    '传入路径返回True或False'
    return os.path.isfile(路径)


@异常检测
def 文件_是否存在(路径):
    '传入路径返回True或False'
    return os.path.exists(路径)


@异常检测
def 文件_取文件大小(路径):
    '返回文件长度'
    return os.path.getsize(路径)


@异常检测
def 文件_获取文件信息(路径):
    '成功返回(上次访问时间,修改时间,文件大小)，返回的是10位时间戳'
    结果 = os.stat(路径)
    return (结果.st_atime,结果.st_mtime,结果.st_size)


@异常检测
def 文件_修改文件时间(路径, 时间):
    '成功返回True,传入的时间为10位时间戳元组类型(访问时间戳,修改时间戳)'
    os.utime(路径, 时间)
    return True


@异常检测
def 文件_取最近访问时间(路径):
    '返回时间戳'
    return os.path.getatime(路径)


@异常检测
def 文件_取创建时间(路径):
    '返回时间戳'
    return os.path.ctime(路径)


@异常检测
def 文件_取修改时间(路径):
    '返回时间戳'
    return os.path.mtime(路径)


@异常检测
def 文件_修改权限(路径, 类型=0):
    '成功返回True,权限类型： 0 设为只读 1 取消只读,更多权限参考 http://www.runoob.com/python/os-chmod.html'
    权限 = {0:stat.S_IREAD,1:stat.S_IWRITE}
    os.chmod(路径, 权限[类型])
    return True


@异常检测
def 文件_取数据摘要(路径=""):
    '取文件MD5'
    with open(路径, mode='rb') as f:
        d = hashlib.md5()
        for buf in iter(partial(f.read, 128), b''):
            d.update(buf)
    return d.hexdigest()
