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
        print("执行对象得到参数是",name)

p = Person('jack')
print(p)
p()        