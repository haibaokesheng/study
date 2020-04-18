'''
@Author: your name
@Date: 2020-03-20 17:30:00
@LastEditTime: 2020-04-08 17:01:09
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \python学习\匿名函数.py
'''
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 17:29:48 2020

@author: haibao
"""
s = lambda a,b:a+b
a = s(1,3)

#匿名函数作为参数
def func(x,y,func):
    print(x,y)
    print(func)   
    print (func(x,y))   
func(1,2,lambda a,b:a+b)

#匿名函数与内置函数结合使用
list1=[1,2,3,4,5,6]
m = max(list1)
# 找到 a 数值最大的字典
list2= [{'a':10,'b':12},{'a':1,'b':11}]
m = max(list2,key=lambda x:x['a'])
print(m)


from functools import reduce
tuple1=(1,2,3,4)
result = reduce(lambda x,y:x+y,tuple1)
print(result)
tuple2=(1,)
print(reduce(lambda x,y:x+y,tuple2,10))

list1= [12,143,1,2,4,133,45,231,0]
print(list(filter(lambda x:x>10,list1)))
#找出所以年龄大于20岁的人
student = [{'name':'bob','age':12},
          {'name':'Alice','age':19},
          {'name':'Joe','age':55},
          {'name':'Tom','age':22}]
result = filter(lambda x:x['age']>20,student)
print(list(result))
a = sorted(student,key=lambda x:x['age'])
print(a)