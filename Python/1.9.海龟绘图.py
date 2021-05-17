# -*- coding: utf-8 -*-

from turtle import *

def drawRectangle(x, y):
    penup() # pu()
    goto(x, y)
    pendown()
    seth(0) # 朝向
    # 设置笔刷宽度:
    width(4)
    # 前进: 
    forward(200)
    # 右转90度:
    right(90)
    # 笔刷颜色:
    pencolor('red')
    forward(100)
    right(90)
    pencolor('green')
    forward(200)
    right(90)
    pencolor('blue')
    forward(100)
    right(90)

def drawStar(x, y):
    pu()
    goto(x, y)
    pd()
    # set heading: 0
    seth(0)
    for i in range(5):
        fd(40)
        rt(144)

for x in range(0, 250, 50):
    drawStar(x, 0)
drawRectangle(0,0)

done()