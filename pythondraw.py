'''import turtle#绘图库  #不出现函数重名
turtle.setup(650,350,0,0)#初始化画布
turtle.penup()
turtle.fd(-250)#前进
turtle.pendown()
turtle.pensize(25)
turtle.colormode(1)
turtle.pencolor(0.5,0.3,0.1)
turtle.seth(-40)#改变方向
for i in range(4):
	turtle.circle(40,80) #圆心默认左侧r的地方
	turtle.circle(-40,80)#负数默认为右侧r的地方
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)
turtle.done()
#from turtle import *#可能出现重复
'''
import turtle as t
for i in range(4):
    t.circle(i*10 + 50)