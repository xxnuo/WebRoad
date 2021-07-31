# -*- coding:utf-8 -*-
#会弹出新窗口 不知道怎么在原窗口加载页面 临时应急凑活用的

from .共用 import *
from cefpython3 import cefpython as cef
import platform,sys,threading,time

class CEF浏览器:

    @异常检测
    def 启动(self, 父窗口句柄=None,URL='http://www.baidu.com', 标题='CEF浏览器', 禁止加载图片=False, 禁止加载JS=False, 禁止加载插件=False, 禁用GPU渲染=False,
        禁止使用本地储存=False, 禁止TAB切换元素=False, 禁用安全策略=False, 调试模式=False,忽略证书错误=True,代理=[0, ''], 不走系统代理=False,允许右键检查 = True,
        允许右键打印 = True,允许右键查看源码 = True,允许右键点击 = True,允许外部打开页面 = True,允许前进后退刷新 = True,
        协议头='mozilla/5.0 (windows nt 10.0; win64; x64) applewebkit/537.36 (khtml, like gecko) chrome/85.0.4183.83 safari/537.36'):

        '代理格式：[0,"127.0.0.1:88"] 0.http  1.socks  2.sock4  3. socks5'

        self.cef = cef
        settings = {}
        switches = {}
        代理字典 = {0:'https=',1:'socks://',2:'sock4://',3:'socks5://'}
        if 禁用GPU渲染:
            switches['disable-gpu'] = ''
        if 代理[1]:
            switches['proxy-server'] = 代理字典[代理[0]]+ 代理[1]
        if 不走系统代理:
            switches['no-proxy-server'] = ''

        if 协议头:
            settings['user_agent'] = 协议头
        窗口信息 = cef.WindowInfo()
        if 父窗口句柄:
            窗口信息.SetAsChild(父窗口句柄)
            settings['external_message_pump'] = True


        settings['debug'] = 调试模式
        settings['ignore_certificate_errors'] = 忽略证书错误
        settings['context_menu'] = {"enabled":允许右键点击,"navigation":允许前进后退刷新,"print":允许右键打印,'view_source':允许外部打开页面,'devtools':允许右键检查}
        sys.excepthook = self.cef.ExceptHook # 替换python预定义异常处理逻辑，为保证异常发生时能够结束所有进程
        self.cef.Initialize(settings=settings,switches=switches) # 创建浏览器



        settings = {}
        settings['image_load_disabled'] = 禁止加载图片
        settings['javascript_disabled'] = 禁止加载JS
        settings['plugins_disabled'] = 禁止加载插件
        settings['local_storage_disabled'] = 禁止使用本地储存
        settings['tab_to_links_disabled'] = 禁止TAB切换元素
        settings['web_security_disabled'] = 禁用安全策略

        self.浏览器 = self.cef.CreateBrowserSync(窗口信息,url=URL,window_title=标题,settings=settings)
        # self.浏览器.SetClientHandler(self.ClientHandler())#需要拦截修改再开

        if 父窗口句柄:
            threading.Thread(target=self.循环消息).start()
        else:
            self.cef.MessageLoop()  # 消息循环：监听信号和处理事件
            self.cef.Shutdown()  # 结束进程
        return True


    class ClientHandler(object):#类名可以修改，拦截修改用
        def OnBeforeResourceLoad(self, browser, frame, request): #这里不要去改动
            if request.GetUrl() == 'https://www.baidu.com/':#示例判断
                # print(request.GetUrl()) #取URL
                # print(request.GetMethod()) #取请求方式 GET POST等
                # print(request.GetPostData())#取提交的内容 字典格式
                # print(request.GetHeaderMap())#取提交的协议头 字典格式
                #
                # print(request.SetUrl())  # 修改URL
                # print(request.SetMethod())  # 修改请求方式 GET POST等
                # print(request.SetPostData())  # 修改提交的内容 字典格式
                # print(request.SetHeaderMap())  # 修改提交的协议头 字典格式
                return False #返回True表示拦截不发送请求




    @异常检测
    def 运行JS代码段(self,JS代码):
        '没有返回'
        self.浏览器.ExecuteJavascript(jsCode=JS代码)
        return True

    @异常检测
    def 运行JS代函数(self,*args):
        '没有返回,运行JS代函数(方法名 参数1 参数2~~~)'
        self.浏览器.ExecuteFunction(*args)
        return True

    def 循环消息(self):
        while True:
            self.cef.MessageLoopWork() # 消息循环：监听信号和处理事件
            time.sleep(0.05)

    def 结束(self):
        self.cef.Shutdown()  # 结束所有进程
        return True