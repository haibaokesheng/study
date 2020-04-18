'''
@Author: your name
@Date: 2020-03-23 15:36:45
@LastEditTime: 2020-04-08 21:27:36
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \刷题人生\python学习\私有化_2.py
'''
#在开发中看到一些私有化处理，装饰器
class Student:
   # __age = 18 #类属性
    def __init__(self,name,age):
        self.name = name #长度必须6位
        self.__age = age
      
   # 定义公有 set 和 get 方法
#    # set是为了赋值
#     def setAge(self,age):
#         if age>0 and age<=120:
#             self.__age = age
#         else:
#             print('年龄不在规定的范围内')
#     # get是为了取值 
#     def getAge(self):
#         return self.__age
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self,age):
        if age>0 and age<=120:
            self.__age = age
        else:
            print('年龄不在规定的范围内')

    def __str__(self):
        return "姓名:{},年龄:{}".format(self.__name,self.__age)
s = Student('haibao',20)
s.name = 'kesheng'
print(s.name)

# 私有化赋值
#s.setAge(30)
#print(s.getAge()) 
s.age = 10000
print(s.age) 