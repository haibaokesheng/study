'''
@Author: your name
@Date: 2020-03-23 20:34:03
@LastEditTime: 2020-03-24 15:16:40
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \刷题人生\python学习\继承.py
'''
import random
class Road:
    def __init__(self,name,len):
        self.name = name
        self.len = len
class Car:
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed

    def get_time(self,road): # road = r, road 与r指向同一个地址空间
        ran_time = random.randint(1,10)
        msg = "{}品牌的车在{}以上{}速度行驶{}小时"\
            .format(self.brand,road.name,self.speed,ran_time)
        print(msg)

    def __str__(self):
        return '{}品牌的,速度:{}'.format(self.brand,self.speed)

#创建实例化对象
r = Road('京广高速',12000)
r.name = '京哈高速'
print(r.name)
audi = Car('奥迪',120)
#print(audi)
audi.get_time(r)

'''
is a  base class 父类 基类
继承:
    Student,Employee,Doctor --->都属于人类
    相同代码---> 代码冗余，可读性不高
    将相同代码提取 ---> Person 类
    Student,Employee,Doctor ---> 继承Person
    class Student(Person):
        pass
    特点
    1.如果类中不定义__init__,调用父类 super class的__init__
    2.如果类继承父类也需要定义自己的__init__,就需要在当前类的__init调用一下父类的__init__
    3.如何调用父类__init__:
        super().__init__(参数)
        super(类名，对象).__init__(参数)
    4.如果父类有eat(),子类也定义一个eat()方法，默认搜索的原则：先搜当前类，再去找父类
    s.eat()
    override:重写（覆盖）
    父类提供的方法不能满足子类的需求，就需要在子类中定义一个同名的方法，这种行为：重写
    5.子类的方法中也可以调用父类的方法
        super().方法名(参数) 
'''
# 多继承
class A:
    def test(self):
        print("-->AAAAAAAAAA")
class B:
    def test(self):
        print("-->BBBBBBBBBB")
class C(A,B):
    def test(self):
        print("-->CCCCCCCC")
c =C()
c.test()
#c.test()
