# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 15:19:24 2020

@author: haibao
"""
'''
生成器:generator
定义生成器方式
1.通过列表推导式
    g =(x+1 for x in range(6))
2.函数 + yield

'''
#方式1
g = (x*3 for x in range(5))
#print(g)

print(g.__next__())
#方式2   next(生成器对象)builtins系统内置函数
# 每调用一次next则会产生一个元素
while True:
    try:
        e = next(g)
        print(e)
    except:
        print("没有更多元素了")
        break
# 定义生成器方式二:借助函数完成
# 只要函数中出现 yield 关键字，说明函数不再是函数了，变成生成器了         
'''
步骤：
1.定义一个函数,加 yield 关键字
2.调用函数，接收调用的结果
3.得到的结果就是生成器
4.借助于next()，__next__()得到元素
'''
print()
def fib(L):
    a,b = 0,1
    n = 0
    while n<L:
        #print(b)
        yield b  # return b + 暂停
        n+=1
        a,b = b,a+b
    return "无元素了"  # return 就是在得到StopInteration后的提示信息
g = fib(8) 
print(next(g))
print(next(g)) 
print(next(g)) 
print(next(g))         
print()
'''
生成器方法
__next__():获取下一个元素
send(value):向每次生成器调用中传值value，第一次调用send(None)
'''
def gen():
    i = 0
    while i<5:
        temp = yield i
        print("temp:",temp)
        for x in range(temp):
            print("--->",x)
        print("***")
        i+=1
    return "无元素了"
g = gen()
print(g.send(None))
n1 = g.send(3)
print("n1",n1)
n2 = g.send(5)
print("n2",n2)

'''
生成器应用
进程->线程->协程
'''
print()
def task1(n):
    for i in range(n):
        print("正在搬第{}块砖".format(i+1))
        yield
        
def task2(n):
    for i in range(n):
        print("正在听第{}首歌".format(i+1))
        yield 

g1 = task1(5)
g2 = task2(5)

while True:
    try:
        g1.__next__()
        g2.__next__()
    except:
        break     
# 可迭代的对象：1 生成器 2 元组 列表 集合 字典 字符串(iter)
# 判断一个对象是否可
from collections import Iterable
list1 =[1,2,3] 
print(isinstance(list1,Iterable))
g =(x+1 for x in range(10))
print(isinstance(g,Iterable))

'''
迭代器：可以被next()函数调用并不断返回下一个值的对象,只能往前
称为迭代器 Iterator
生成器是可迭代的，也是迭代器
list是可迭代的，不是迭代器
list-->iter(list)-->迭代器 next()
'''
list1=[1,2,3]
list1 = iter(list1) #通过iter()函数将可迭代的变成了一个迭代器
print(next(list1))
