# -*- coding:utf-8 -*-
import os,hashlib,random,time,execjs,re,requests,struct,base64,hmac,queue,json,subprocess
from .共用 import *

class 队列:

    def __init__(self,队列大小=0, 顺序=True):
        '如果队列大小小于1就表示无限长,顺序为假则队列是后进先出'
        if 顺序:
            self.__队列 = queue.Queue(maxsize=队列大小)
        else:
            self.__队列 =queue.LifoQueue(maxsize=队列大小)

    @异常检测
    def 是否为空(self):
        '返回True,False'
        return self.__队列.empty()

    @异常检测
    def 是否已满(self):
        '返回True,False'
        return self.__队列.full()

    @异常检测
    def 清空队列(self):
        '返回True,False'
        return self.__队列.queue.clear()

    @异常检测
    def 取出成员(self):
        "取出队列最前面或最后的一个值"
        if self.__队列.qsize() <= 0:
            return ''
        else:
            return self.__队列.get()

    @异常检测
    def 取队列成员数(self):
        '失败返回0'
        return self.__队列.qsize()

    @异常检测
    def 加入成员(self,值):
        '成功返回True'
        self.__队列.put(值)
        return True


@异常检测
def JSON_转字典(内容):
    return json.loads(内容)


@异常检测
def 系统_执行Dos_带返回(命令):
    '成功返回执行结果'
    p = subprocess.Popen(命令, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    结果 = p.stdout.readlines()[0].decode('utf8')
    return 结果

@异常检测
def 系统_执行Dos_带返回2(命令):
    '成功返回执行结果,不能用于打包独立exe'
    f = os.popen(命令)
    结果 = str(f.read())
    f.close()
    return 结果


@异常检测
def 系统_执行Dos(命令):
    '成功返回0 失败返回1'
    return os.system(命令)


@异常检测
def 宽带_拨号(宽带名称,宽带账号,宽带密码):
    dos = 'rasdial {} {} {}'.format(宽带名称,宽带账号,宽带密码)
    return False if os.system(dos) else True


@异常检测
def 宽带_断开(宽带名称):
    dos = 'rasdial {} /disconnect'.format(宽带名称)
    return False if os.system(dos) else True


@异常检测
def 程序_延时(延迟秒数):
    '延迟时间，可以用小数'
    time.sleep(延迟秒数)


@异常检测
def 调试输出(*args):
    '偶尔打错,就写一个放着用吧'
    print(*args)


@异常检测
def 讯代理_计算协议头(单号,秘钥,返回类型=0):
    '类型0.文本型完整协议头  1.字典格式 2.仅协议头内容,代理地址为 forward.xdaili.cn:80'
    时间戳 = str(round(time.time()))
    加密内容 = "orderno={},secret={},timestamp={}".format(单号, 秘钥, 时间戳)
    MD5 = hashlib.md5()
    MD5.update(加密内容.encode(encoding="utf-8"))
    if 返回类型 == 0:
        return "Proxy-Authorization:sign={}&orderno={}&timestamp={}".format(MD5.hexdigest().upper(),单号,时间戳)
    elif 返回类型 == 1:
        return {"Proxy-Authorization":"sign={}&orderno={}&timestamp={}".format(MD5.hexdigest().upper(),单号,时间戳)}
    else:
        return "sign={}&orderno={}&timestamp={}".format(MD5.hexdigest().upper(), 单号, 时间戳)


@异常检测
def JS_加载(JS代码):
    '成功返回个对象,可以直接调用运行方法'
    js = execjs.compile(JS代码)
    if js:
        return 普通js类(js)

class 普通js类:
    def __init__(self,js):
        self.js = js

    @异常检测
    def 运行(self,方法名,*参数):
        '通过JS_加载返回的对象,方法名后面可以直接传入多个参数'
        return self.js.call(方法名,*参数)


@异常检测
def 正则_匹配(原文本, 匹配规则):
    '匹配成功返回匹配到的列表'
    return re.findall(匹配规则, 原文本)


@异常检测
def 联众答题(账号, 密码, 图片字节集, 类型='1001',开发者Token='', 最短识别='', 最长识别=''):
    '类型参考,https://www.jsdati.com/docs/price 最长最短可空'
    data = {'user_name': 账号,'user_pw': 密码,'yzm_minlen': 最短识别,'yzm_maxlen': 最长识别,'yzmtype_mark': 类型,'zztool_token': 开发者Token}
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0',
        # 'Content-Type': 'multipart/form-data; boundary=---------------------------227973204131376',
        'Connection': 'keep-alive',
        'Host': 'v1-http-api.jsdama.com',
        'Upgrade-Insecure-Requests': '1'
    }
    图片 = {'upload': ('code.png', 图片字节集, 'image/png')}
    http = requests.session()
    return http.post("http://v1-http-api.jsdama.com/api.php?mod=php&act=upload", data=data,headers=headers, files=图片, verify=False).text


@异常检测
def 对象转文本(对象):
    '如：{1：1} 直接将字典转为文本型'
    return repr(对象)


@异常检测
def 谷歌身份验证(secret_key):
    '基于时间的算法'
    for x in range(5):#最多尝试5次补全
        try:
            decode_secret = base64.b32decode(secret_key, True)
            interval_number = int(time.time() // 30)
            message = struct.pack(">Q", interval_number)
            digest = hmac.new(decode_secret, message, hashlib.sha1).digest()
            index = ord(chr(digest[19])) % 16
            google_code = (struct.unpack(">I", digest[index:index + 4])[0] & 0x7fffffff) % 1000000
            return "%06d" % google_code
        except:
            secret_key += "="


@异常检测
def 运行python代码(代码,全局变量=None,局部变量=None):
    '动态执行python代码并返回值'
    return eval(代码,全局变量,局部变量)


@异常检测
def 运行python代码2(代码,全局变量=None,局部变量=None):
    '动态执行python代码,只返回None'
    return exec(代码,全局变量,局部变量)

@异常检测
def 滑块_计算滑动进度列表(距离):
    """
    拿到移动轨迹，模仿人的滑动行为，先匀加速后匀减速
    匀变速运动基本公式：
    ①v=v0+at
    ②s=v0t+½at²
    """
    # 初速度
    v = 0
    # 单位时间为0.3s来统计轨迹，轨迹即0.3内的位移
    t = 0.3
    # 位置/轨迹列表,列表内的一个元素代表0.3s的位移
    tracks = []
    # 当前的位移
    current = 0
    # 到达mid值开始减速
    mid = 距离*4/5
    while current < 距离:
        if current < mid:
            # 加速度越小,单位时间内的位移越小,模拟的轨迹就越多越详细
            a = 2
        else:
            a = -3

        # 初速度
        v0 = v
        # 0.3秒内的位移
        s = v0*t+0.5*a*(t**2)
        # 当前的位置
        current += s
        # 添加到轨迹列表
        tracks.append(round(s))
        # 速度已经达到v，该速度作为下次的初速度
        v = v0 + a*t
    tracks.reverse()
    return tracks
    # tracks: [第一个0.3秒的移动距离,第二个0.3秒的移动距离,...]
