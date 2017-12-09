#coding: euc-kr

#함수 예제

def myaverage(a, b):
    return (a+b)/2
print(myaverage(10, 100))

print()


def get_max_min(data_list):
    max_price = max(data_list)
    min_price = min(data_list)
    return (max_price, min_price)

(a, b) = (get_max_min([1,2,3,4,5,6,7]))

print (a+b)
print(a,",", b)
print(a)

print()

def get_max_min(data_list):
    max_price = max(data_list)
    min_price = min(data_list)
    return (max_price + min_price)

(a) = (get_max_min([1,2,3,4,5,6,7]))
print(a)

print()

import os
def get_txt_list(path):
    org_list = os.listdir(path)
    ret_list = []
    for x in org_list:
        if x.endswith('txt'):
            ret_list.append(x)
    return ret_list
print(get_txt_list('c:/'))




