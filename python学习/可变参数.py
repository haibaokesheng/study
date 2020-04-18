'''
@Author: your name
@Date: 2020-03-19 19:35:19
@LastEditTime: 2020-04-07 22:56:09
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \刷题人生\python学习\可变参数.py
'''
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 19:35:04 2020

@author: haibao
"""
# 可变参数  元组
def add(name,*args):
    sum = 0
    if len(args)>0:
        for i in args:
            sum+=i
    print("%s 累加和是 %s"%(name,sum))
add('菲菲',4,6,8)
# 可变参数  关键字参数 字典
def func(**kwargs):
    print(kwargs)
func(a=1,b=2)
dict1 = {'1':'python','2':'C语言'}
func(**dict1) #**拆包，将字典拆成关键字参数的形式

def bb(a,b,*c,**d):
    print(a,b,c,d)
bb(1,2)             # 1 2 () {}
bb(1,2,3,4)         # 1 2 (3, 4) {}
bb(1,2,x=100,y=200) # 1 2 () {'x': 100, 'y': 200}
bb(1,2,3,x=100)     # 1 2 (3,) {'x': 100}
#bb(1,2,x=500,5,6)   # 报错
