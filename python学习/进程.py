'''
@Author: your name
@Date: 2020-03-25 21:26:04
@LastEditTime: 2020-03-25 22:29:15
@LastEditors: Please set LastEditors
@Description: 进程学习
@FilePath: \刷题人生\python学习\进程.py
'''

'''
目的是快速完成事情
from multiprocessing import Process
process = Process(target=函数,name=进程的名字,args=(给函数传递的参数))
process  对象
process.start() 启动进程并执行任务
process.run() 只是执行了任务但是没有启动进程
process.terminate() 终止 
多进程对于全局变量访问，在每一个全局变量里面都放一个m变量
保证每个进程访问变量互不干扰
'''
#进程创建
from multiprocessing import Process
from time import sleep
import os
m = 1
def task1(s,name):
    global m
    while True:
        sleep(s)
        m+=1
        print('这是任务1。。。。',os.getpid(),'----',os.getppid(),name)

def task2(s,name):
    global m
    while True:
        sleep(s)
        m+=1
        print('这是任务2。。。。',os.getpid(),'----',os.getppid(),name)        
num = 1
if __name__ == "__main__":
    print(os.getpid())
    # 子进程
    p = Process(target=task1,name='任务1',args=(1,'aa'))
    p.start()
    print(p.name)
    p1 = Process(target=task2,name='任务2',args=(2,'bb'))
    p1.start()
    print(p1.name)

    while True:
        num+=1
        sleep(0.2)
        if num==100:
            p.terminate()
            p1.terminate()
            break
        print(num)
    print('-----------')
    print('***********')

   
            