# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 12:29:22 2020

@author: haibao
"""
#定义一个装饰器
def decorate(func):
    a = 100
    print("wrapper外层打印测试")
    def wrapper():
        func() #调用原函数 
        print("--->刷漆")     
        print("--->铺地板",a)
    return wrapper
#使用装饰器
@decorate 
def house():
    print("我是毛坯房")
'''
1.house 被装饰器函数
2.将被装饰函数作为参数传给装饰器decorate
3.执行decorate函数
4.将返回赋值给house
'''
#调用函数 house
house()    
print()

#多层装饰器
def decorate_1(func):
    print("--->1 start")
    def wrapper(*args,**kwargs):
        func()
        print("--->刷漆")
    return wrapper

def decorate_2(func):
    print("--->2 start")
    def wrapper(*args,**kwargs):
        func()
        print("--->铺地板")
    return wrapper

@decorate_2
@decorate_1  #先装近的
def house():
    print("我是毛坯房")
house()

print()
#带参数的decorate
def outer(a): #第一层、负责接收装饰器参数
    def decorate_3(func): #第二层、负责接收函数
        def wrapper(*args,**kwargs): #第三层、负责解释函数的参数
            func(*args,**kwargs)
            print("--->铺地板 {} 块 ".format(a))
        return wrapper
    return decorate_3

@outer(a=10)
def house(time):
    print("我{}日期拿到房子的钥匙，是毛坯房".format(time))
house("2020-3-20")

@outer(100)
def street():
    print("新修的路是大马路")
street()    

