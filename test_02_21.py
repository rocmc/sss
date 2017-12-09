#coding: euc-kr

#�ź��� ����
#
# import random
#
# import turtle
# t1=turtle.Turtle()
# t2=turtle.Turtle()
#
# t1.color("pink")
# t1.shape("turtle")
# t1.shapesize(5)
# t1.pensize(5)
#
# t2.color("blue")
# t2.shape("turtle")
# t2.shapesize(5)
# t2.pensize(5)
#
# t1.penup()
# t1.goto(-300, 0)
#
# t2.penup()
# t2.goto(-300, -100)
#
# for i in range(100):
#     d1=random.randint(1, 60)
#     t1.forward(d1)
#     d2=random.randint(1, 60)
#     t2.forward(d2)

# import turtle
# import random
#
# screen = turtle.Screen()
# image1 = "C:\\turtle.GIF"
# image2 = "C:\\rabbit.GIF"
# screen.addshape(image1)
# screen.addshape(image2)
#
# t1=turtle.Turtle()
# t1.shape(image1)
#
# t2=turtle.Turtle()
# t2.shape(image2)


import turtle
import random

screen = turtle.Screen()
image1 = "c:\\rabbit.gif"
image2 = "c:\\turtle.gif"
screen.addshape(image1)
screen.addshape(image2)

t1 = turtle.Turtle()
t1.shape(image1)
t1.pencolor("pink")
t1.pensize(5)
t1.penup()
t1.goto(-300, 0) # (-300, 0)

t2 = turtle.Turtle()
t2.shape(image2)
t2.pencolor("blue")

t2.pensize(5)
t2.penup()
t2.goto(-300, -200) # (-300, 0)

t1.pendown() # ù ��° �ź����� ���� ������.
t2.pendown() # ù ��° �ź����� ���� ������.
t1.speed(1)
t2.speed(1)

for i in range(100): # 100�� �ݺ��Ѵ�.
	d1 = random.randint(1, 100) # 1���� 60 ������ ������ .
	t1.forward(d1) # ������ŭ .
	d2 = random.randint(1, 60) # 1���� 60 ������ ������ .
	t2.forward(d2)

