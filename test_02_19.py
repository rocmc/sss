#coding: euc-kr

#모듈 생성

def plus(a, b):
    return a + b
def minus(a, b):
    return a - b
def div(a, b):
    return a / b
def mul(a, b):
    return a * b


def cal_upper(price):
    increment = price * 0.3
    upper_price = price + increment
    return upper_price

def cal_lower(price):
    decrement = price * 0.3
    lower_price = price - decrement
    return lower_price

author = "pystock"

