# -*- coding:utf-8 -*-
from PIL import Image, ImageDraw, ImageFont, ImageFilter,ImageEnhance,ImageSequence
from .共用 import *
from io import BytesIO
import random

def 图片_生成验证码(内容,宽度=118,高度=46):
    '返回二进制验证码图片内容'
    width = 宽度
    height = 高度
    image = Image.new('RGB', (width, height), (255, 255, 255))
    font = ImageFont.truetype('simsun.ttc', 36)
    draw = ImageDraw.Draw(image)
    # 随机生成两条直线（一条贯穿上半部，一条贯穿下半部）
    draw.line((0, 0 + random.randint(0, height // 2),
               width, 0 + random.randint(0, height // 2)),
              fill=(random.randint(0, 245), random.randint(0, 245), random.randint(0, 245)))
    draw.line((0, height - random.randint(0, height // 2),
               width, height - random.randint(0, height // 2)),
              fill=(random.randint(0, 245), random.randint(0, 245), random.randint(0, 245)))

    for t in range(len(内容)):
        tmp = str(内容[t])
        if '(' in 内容 and t != 0:
            距离 = 宽度/len(内容) + t * 17
            draw.text((距离,  高度 - 40), tmp, font=font,fill=(255,0,0))
        else:
            距离 = 宽度/len(内容) * t + random.randint(-5,5)
            draw.text((距离, random.randint(0, 高度-33)), tmp, font=font, fill=(random.randint(0, 245), random.randint(0, 245), random.randint(0, 245)))

    # 模糊处理
    # image = image.filter(ImageFilter.BLUR)
    img = BytesIO()
    image.save(img, 'png')
    return img.getvalue()



@异常检测
def  图片_新建(尺寸=(100,100),颜色='#FF0000',模式='RGB'):
    '默认创建一张100*100的红色图'
    img = Image.new(模式, 尺寸, 颜色)
    if img:
        return 图片类(img)

@异常检测
def  图片_打开(文件名):
    img = Image.open(文件名, "r")
    if img:
        return 图片类(img)

@异常检测
def  图片_打开_从二进制(二进制):
    p = BytesIO(二进制)
    img = Image.open(p)
    if img:
        return 图片类(img)


class 图片类():
    def __init__(self,img):
        self.img = img

    @异常检测
    def 取宽高(self):
        '(宽,高)'
        return self.img.size

    @异常检测
    def 取类型(self):
        '如：JPEG'
        return self.img.format

    @异常检测
    def 取模式(self):
        '如：RGB'
        return self.img.mode

    @异常检测
    def 保存(self,文件名,类型=''):
        '保存指定格式的图像,类型如：png'
        if 类型:
            self.img.save(文件名,类型)
        else:
            self.img.save(文件名)
        return True

    @异常检测
    def 取二进制(self,类型=None):
        '返回图片字节集,类型如：png,jpeg'
        s = BytesIO()
        if not 类型:
            类型 = self.img.format
        self.img.save(s, 类型, quality=95)
        return s.getvalue()

    @异常检测
    def 转缩略图(self,宽,高,采样=0):
        '''
        创建一个指定大小(size)的缩略图,需要注意的是，thumbnail方法是原地操作，
        :param 宽:
        :param 高:
        :param 采样: 0:Image.BICUBIC,  1:Image.LANCZOS,  2:Image.BILINEAR,  3:Image.NEAREST
        :return: 返回值是None
        '''
        字典 = {0:Image.BICUBIC,1:Image.LANCZOS,2:Image.BILINEAR,3:Image.NEAREST}
        self.img.thumbnail((宽,高),resample=字典[采样])
        return True

    @异常检测
    def 裁剪(self,左边,顶边,右边,底边):
        '返回的仍然是一个Image对象'
        img = self.img.crop((左边,顶边,右边,底边))
        if img:
            return 图片类(img)

    @异常检测
    def 翻转(self,类型=0):
        '类型：0.左右翻转   1.上下翻转'
        fl = Image.FLIP_TOP_BOTTOM if 类型 else Image.FLIP_LEFT_RIGHT
        img = self.img.transpose(fl)
        if img:
            return 图片类(img)

    @异常检测
    def 旋转(self,类型=0):
        '类型：0.顺时针旋转90°  1.逆时针旋转90°  2.逆时针旋转180°  3.逆时针旋转270°  '
        字典 = {0:Image.TRANSPOSE,1:Image.ROTATE_90,2:Image.ROTATE_180,3:Image.ROTATE_270}
        img = self.img.transpose(字典[类型])
        if img:
            return 图片类(img)

    @异常检测
    def 显示(self):
        self.img.show()
        return True

    @异常检测
    def 粘贴图片(self,图片,左边,顶边):
        '将一个图像粘贴到另一个图像,将图像粘贴到左上角为(左边,顶边)的位置'
        self.img.paste(图片,(左边,顶边),None)
        return True

    @异常检测
    def 合并图片(self,图片,透明度=0.5):
        '若透明度为0.0，返回第一张图像的拷贝。为1.0，将返回第二张图像的拷贝,透明度为0.4表示第一张图透明度为40%第二张图透明度为60%'
        img = Image.blend(self.img,图片,透明度)
        if img:
            return 图片类(img)

    @异常检测
    def 颜色通道分离(self):
        '返回R,G,B三个颜色道的图片'
        return [图片类(x) for x in self.img.split()]

    @异常检测
    def 颜色通道合并(self,img=[],模式='RGB'):
        'Image.merge("RGB",[b,r,g]),其将多个单一通道的序列合并起来，组成一个多通道的图像'
        im = self.img.merge(模式,img)
        if im:
            return 图片类(im)

    @异常检测
    def 修改尺寸(self, 宽, 高,指定区域=(),采样=0):
        '''
        将原始的图像转换大小,并返回新图片
        :param 宽:新宽
        :param 高:新高
        :param 指定区域: (0,0,100,100)  指定将这块区域裁剪出来修改尺寸
        :param 采样: 0: Image.NEAREST, 1: Image.BICUBIC, 2: Image.LANCZOS, 3: Image.BILINEAR
        :return: 返回新图片
        '''
        字典 = {0: Image.NEAREST, 1: Image.BICUBIC, 2: Image.LANCZOS, 3: Image.BILINEAR}
        imt = self.img.resize((宽, 高), resample=字典[采样],box=指定区域)
        if imt:
            return 图片类(imt)

    @异常检测
    def 转真彩图(self):
        '将图片模式(mode)转为RGB'
        img = self.img.convert("RGB")
        if img:
            return 图片类(img)

    @异常检测
    def 转灰度图(self):
        '将图片模式(mode)转为L'
        img = self.img.convert("L")
        if img:
            return 图片类(img)

    @异常检测
    def 转压缩图(self):
        '将图片模式(mode)转为CMYK'
        img = self.img.convert("CMYK")
        if img:
            return 图片类(img)

    @异常检测
    def 转模糊图(self):
        img = self.img.filter(ImageFilter.BLUR)
        if img:
            return 图片类(img)

    @异常检测
    def 转高斯模糊图(self):
        img = self.img.filter(ImageFilter.GaussianBlur)
        if img:
            return 图片类(img)

    @异常检测
    def 转轮廓图(self):
        img = self.img.filter(ImageFilter.CONTOUR)
        if img:
            return 图片类(img)

    @异常检测
    def 转边缘检测图(self):
        img = self.img.filter(ImageFilter.FIND_EDGES)
        if img:
            return 图片类(img)

    @异常检测
    def GIF_逐帧分割(self):
        '遍历gif图像中的所有帧'
        return [图片类(frame) for i, frame in enumerate(ImageSequence.Iterator(self.img), 1)]

    @异常检测
    def GIF_取指定帧图片(self,位置):
        img = self.img.seek(位置)
        if img:
            return 图片类(img)

    @异常检测
    def GIF_取图片帧位置(self,位置):
        '返回当前帧所处位置，从0开始计算'
        return self.img.tell()

    @异常检测
    def 修改亮度(self,数值=1.0):
        '0.0是黑白图,1.0是原始亮度'
        img = ImageEnhance.Color(self.img).enhance(数值)
        if img:
            return 图片类(img)

    @异常检测
    def 修改对比度(self,数值=1.0):
        '1.0是原始对比度'
        img = ImageEnhance.Contrast(self.img).enhance(数值)
        if img:
            return 图片类(img)

    @异常检测
    def 修改锐度(self, 数值=1.0):
        '1.0是原始锐度'
        img = ImageEnhance.Sharpness(self.img).enhance(数值)
        if img:
            return 图片类(img)