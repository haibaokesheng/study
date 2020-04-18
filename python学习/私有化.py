'''
@Author: your name
@Date: 2020-03-23 10:17:38
@LastEditTime: 2020-04-08 20:47:11
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \刷题人生\python学习\私有化.py
'''
'''
私有化
封装 1.私有化属性，2定义共有set和get方法
__属性：就是将属性私有化，访问范围仅仅限于类中
好处
1.隐藏属性不被外界随意修改
2.也可以修改，通过函数
    def setXXX(self,xxx):
        3.筛选赋值的内容
            if xxx 是否符合条件
                赋值
            else
                不赋值
3.如果想要获取具体的某一个属性
使用get函数
def getXXX(self):
    return self._xxx
'''
class Student:
   # __age = 18 #类属性
    def __init__(self,name,age):
        self.__name = name #长度必须6位
        self.__age = age
        self.__score = 59
   # 定义公有 set 和 get 方法
   # set是为了赋值
    def setAge(self,age):
        if age>0 and age<=120:
            self.__age = age
        else:
            print('年龄不在规定的范围内')
    # get是为了取值 
    def getAge(self):
        return 
    def __str__(self):
        return "姓名:{},年龄:{},分数:{}".format(self.__name,self.__age,self.__score)
haibao = Student('haibao',18)
print(haibao)

haibao.setAge(20)
print(haibao)