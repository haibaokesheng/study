'''
@Author: your name
@Date: 2020-03-25 22:29:43
@LastEditTime: 2020-03-26 11:43:37
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \刷题人生\python学习\自定义进程.py
'''
from multiprocessing import Process

class MyProcess(Process):
    def __init__(self,name):
        super(MyProcess,self).__init__()
        self.name =name
    # 重写run方法
    def run(self):
        n=1
        while True:
            print('{}---->自定义进程，n:{}'.format(n,self.name))
            n+=1
if __name__=='__main__':
    p = MyProcess('小名')
    p.start()

    p1 = MyProcess('小大')
    p1.start()

    
         