# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 22:27:23 2020
@author: haibao
2020.3.21 对象学习 类 对象 属性 方法
"""
"""
#类中方法 种类:普通方法、类方法、静态方法、魔术方法
一 普通方法格式
"""
class Phone:
    # 魔术方法之一：__名字__()
    def __init__(self):
        print("----------init")
    
    brand ="xiaomi"
    price = 4999
    type ="10"
    # phone类里的方法call
    def call(self):
        print(self)
        print("正在打电话")

phone = Phone()
#print(phone.brand)
#print(phone.call())
"""
二 类方法
    1.定义需要依赖装饰器@classmethod
    2.类方法中参数不是一个对象，而是类
    3.类方法中只可以使用类属性
    4.类方法中不可以使用普通方法
作用：
    因为只能访问类属性和类方法，所以可以在对象创建之前，如果完成一些动作（功能）
三 静态方法：很类似类方法
    1.需要装饰器staticmethod
    2.静态方法是无需传递参数（cls,self）
    3.也只能访问类的属性和方法，对象的是无法访问的
    4.加载时机同类方法
summary
不同
    1.装饰器不同
    2.类方法是有参数的，静态方法无参数
相同
    1.只能访问类的属性和方法，对象的无法访问
    2.都可以通过类名调用访问
    3.都可以在创建对象之前访问，因为是不依赖于对象
普通方法与 两者的区别
    1.每天装饰器
    2.普通方法永远是依赖对象，因为每个普通方法都有一个self
    3.只有创建了对象，才可以调用普通方法，否则无法使用
""" 
class Person:
    __age =18
    def __init__():
        self.name = name
    def show(self):
        print("---->",Person.age)
    @classmethod
    def update_age(cls):
        cls.__age=20
        print("---->类方法")
        
    @classmethod
    def show_age(cls):
        print('修改后的age is：',cls.__age)
    
    @staticmethod
    def test():
        print('--->静态方法')
        print(Person.__age)

Person.update_age()        
Person.show_age()   
Person.test()

'''
四 魔术方法
4.1 __init__ 初始化魔术方法
触发时机：初始化对象时触发（不是实例化触发，但是和实例化在一个操作中）
4.2 __new__  实例化的魔术方法
触发时机：在实例化触发
4.3 __call__ 对象调用方法
将对象当成函数使用的时候，会默认调用此函数的中的内容
4.4 __del__  
    1.对象赋值
        p = Person()
        p1 = p 说明p和p1共同指向同一个地址
    2.删除地址的引用
        del p1 删除p1对地址的引用
    3.查看对地址的引用次数
        import sys
        sys.getrefcount(p)
    4.当一块空间没有了任何引用，默认执行__del__
4.5__str__
打印对象名，自动触发去调用__str__里面的内容，要+return
return后面的内容就是打印对象看到的内容
'''
class Person:
    def __init__(self,name):
        print('--->init')
        self.name = name
    # def __new__(cls):
    #     print('--->new')
    #     position = object.__new__(cls)
    #     print(position)
    #     return position #地址
    def __call__(self,*args,**kwargs):
        print('--------->call')
        print("执行对象得到参数是",*args)

p = Person('jack')
print(p)
p('jack','hep')
