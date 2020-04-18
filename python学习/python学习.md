<!--
 * @Author: your name
 * @Date: 2020-03-24 13:36:36
 * @LastEditTime: 2020-03-26 13:22:33
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \刷题人生\python学习\python学习.md
 -->
```python
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
```
## 继承
Student,Employee,Doctor --->都属于人类
相同代码---> 代码冗余，可读性不高
将相同代码提取 ---> Person 类
Student,Employee,Doctor ---> 继承Person
class Student(Person):
&emsp;&emsp;pass
### 特点
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