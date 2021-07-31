# -*- coding:utf-8 -*-
import binascii,hashlib,base64,hmac
from urllib import parse
from .共用 import *

@异常检测
def 编码_UTF8编码(内容):
    return 内容.encode(encoding='UTF-8', errors='strict')


@异常检测
def 编码_UTF8解码(内容):
    return 内容.decode(encoding='UTF-8', errors='strict')


@异常检测
def 编码_URL编码(内容,不处理字符=''):
    return parse.quote(内容,safe=不处理字符)


@异常检测
def 编码_URL解码(内容):
    return parse.unquote(内容)


@异常检测
def 编码_GBK编码(内容):
    return 内容.encode(encoding='GBK', errors='strict')


@异常检测
def 编码_GBK解码(内容):
    return 内容.decode(encoding='GBK', errors='strict')


@异常检测
def 编码_ANSI到USC2(内容):
    return ascii(内容)


@异常检测
def 编码_USC2到ANSI(内容):
    return 内容.encode('utf-8').decode('unicode_escape')


@异常检测
def 编码_BASE64编码(内容):
    '要编码的内容支持文本跟字节集'
    if type(内容)==str:
        return base64.b64encode(内容.encode('UTF-8')).decode("UTF-8")
    else:
        return base64.b64encode(内容).decode("UTF-8")


@异常检测
def 编码_BASE64解码(内容, 返回字节集=False):
    '字节集用于解码图片'
    if 返回字节集:
        return base64.b64decode(内容)
    else:
        return base64.b64decode(内容).decode("UTF-8")


@异常检测
def 加密_MD5(内容, 编码="utf-8"):
    MD5 = hashlib.md5()
    MD5.update(内容.encode(encoding=编码))
    return MD5.hexdigest()


@异常检测
def 加密_SHA(内容, 方式=0):
    '方式： 0.SHA1 1.SHA224 2.SHA256 3.SHA384 4.SHA512'
    字典 = {0: hashlib.sha1(), 1: hashlib.sha224(), 2: hashlib.sha256(), 3: hashlib.sha384(), 4: hashlib.sha512()}
    字典[方式].update(str(内容).encode('utf-8'))
    return 字典[方式].hexdigest()


@异常检测
def 加密_SHA3(内容, 方式=0):
    '方式： 0.SHA224 1.SHA256 2.SHA384 3.SHA512'
    字典 = {0: hashlib.sha3_224(), 1: hashlib.sha3_256(), 2: hashlib.sha3_384(), 3: hashlib.sha3_512()}
    字典[方式].update(str(内容).encode('utf-8'))
    return 字典[方式].hexdigest()


@异常检测
def 加密_HmacSHA256(key,内容):
    return base64.b64encode(hmac.new(bytes(key, encoding='utf-8'), bytes(内容, encoding='utf-8'),digestmod=hashlib.sha256).digest()).decode("utf-8")


@异常检测
def 加密_CRC32(内容):
    return binascii.crc32(内容.encode("utf-8"))



@异常检测
def 进制_十到二(内容):
    return bin(内容)


@异常检测
def 进制_十到八(内容):
    return oct(内容)


@异常检测
def 进制_十到十六(内容):
    return hex(内容)


@异常检测
def 进制_二到十(内容):
    return int(内容, base=2)


@异常检测
def 进制_八到十(原内容):
    return int(原内容, base=8)


@异常检测
def 进制_十六到十(内容):
    return int(内容, base=16)
