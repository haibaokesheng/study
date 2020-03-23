# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 14:21:31 2020

@author: haibao
"""

# 开发，登录验证
print()
import time
def login():
    username = input('输入用户名:')
    password = input('输入密码:')
    if username =="admin" and password=="123456":
        return True
    else:
        return False

islogin = False # 默认没登录
# 定义decorate,进行付款验证
def login_required(func):
    print("---付款---")
    def wrapper(*args,**kwarge):
        global islogin
        #验证用户是否登录
        if islogin:
            func(*args,**kwarge)
        else:#跳转到登录页面
            print("用户未登录,不能付款!")
            islogin = login()
            print("result:",islogin)
    return wrapper

@login_required
def pay(money):
    print('正在付款,金额是:{}'.format(money))
    print("付款中")
    time.sleep(2)
    print("付款完成！")
    
pay(10000) 

pay(8000)